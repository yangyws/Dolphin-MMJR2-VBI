import urllib.request
import json
import ssl
import time
import os
import zipfile
import subprocess
import sys

# 輔助函式：從 git credential fill 取得 Token
def get_git_token():
    try:
        p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        out, _ = p.communicate('protocol=https\nhost=github.com\n\n')
        for line in out.splitlines():
            if line.startswith('password='):
                tok = line.split('=', 1)[1].strip()
                if len(tok) >= 20:
                    return tok
    except Exception:
        pass
    return ""

token = os.getenv("GITHUB_TOKEN", "")
if not token:
    token = get_git_token()

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/vnd.github+json"
}
if token:
    headers["Authorization"] = f"token {token}"
ctx = ssl.create_default_context()

repo = "yangyws/Dolphin-MMJR2-VBI-zh"
branch = "main-zh"

print("==========================================================")
print("  Dolphin-MMJR2-VBI-zh 掌機 / Android 自動建置與部署管線")
print("  套件識別碼: org.dolphinemu.mmjr.zh")
print("==========================================================")

# 1. 尋找最新執行的工作流程 run
print(f"[*] 正在尋找 {repo} 分支 {branch} 的最新工作流程執行記錄...")
run_id = None
for attempt in range(15):
    try:
        runs_req = urllib.request.Request(f"https://api.github.com/repos/{repo}/actions/runs?branch={branch}&per_page=5", headers=headers)
        with urllib.request.urlopen(runs_req, context=ctx) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            runs = data.get('workflow_runs', [])
            if runs:
                latest = runs[0]
                commit_msg = latest.get('head_commit', {}).get('message', '').split('\n')[0]
                print(f"[*] 找到最新 Run ID: {latest['id']} | 狀態: {latest['status']} | 結果: {latest['conclusion']} | Commit: {commit_msg}")
                run_id = latest['id']
                break
    except Exception as e:
        print(f"[!] 查詢工作流程記錄失敗：{e}")
    time.sleep(3)

if not run_id:
    print("[!] 未找到正在執行的工作流程 ID。")
    sys.exit(1)

# 2. 輪詢直到編譯完成
print(f"[*] 開始監控 Run {run_id} 編譯進度...")
start_time = time.time()
while True:
    try:
        run_req = urllib.request.Request(f"https://api.github.com/repos/{repo}/actions/runs/{run_id}", headers=headers)
        with urllib.request.urlopen(run_req, context=ctx) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            status = data.get('status')
            conclusion = data.get('conclusion')
            elapsed = int(time.time() - start_time)
            print(f"[{time.strftime('%H:%M:%S')} | 已監控 {elapsed}s] Run {run_id}: 狀態={status}, 結果={conclusion}")
            if status == 'completed':
                if conclusion != 'success':
                    print(f"[!] 編譯未成功結束：{conclusion}")
                    # 若最新 run 失敗，檢查是否有前一個成功的 run
                    sys.exit(1)
                print("[+] 編譯成功完成！")
                break
    except Exception as e:
        print(f"[!] 狀態檢查異常：{e}")
    time.sleep(15)

# 3. 下載 Artifact
print(f"[*] 正在獲取 Run {run_id} 的產物列表...")
art_req = urllib.request.Request(f"https://api.github.com/repos/{repo}/actions/runs/{run_id}/artifacts", headers=headers)
with urllib.request.urlopen(art_req, context=ctx) as resp:
    art_data = json.loads(resp.read().decode('utf-8'))
    artifacts = art_data.get('artifacts', [])
    if not artifacts:
        print("[!] 未找到任何產物！")
        sys.exit(1)
    artifact = artifacts[0]
    dl_url = artifact['archive_download_url']
    print(f"[*] 正在下載產物：{artifact['name']} ({round(artifact['size_in_bytes'] / (1024*1024), 2)} MB)...")

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

opener = urllib.request.build_opener(NoRedirect, urllib.request.HTTPSHandler(context=ctx))
dl_req = urllib.request.Request(dl_url, headers=headers)
redirect_url = None
try:
    resp = opener.open(dl_req)
    redirect_url = resp.getheader('Location')
except urllib.error.HTTPError as e:
    if e.code in (301, 302, 303, 307, 308):
        redirect_url = e.headers.get('Location')
    else:
        raise

base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output_apks")
os.makedirs(base_dir, exist_ok=True)
zip_path = os.path.join(base_dir, f"dolphin_artifact_{run_id}.zip")

blob_req = urllib.request.Request(redirect_url)
with urllib.request.urlopen(blob_req, context=ctx) as resp, open(zip_path, "wb") as f:
    f.write(resp.read())

print(f"[*] 正在解壓縮產物至 {base_dir}...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(base_dir)
os.remove(zip_path)

apk_files = []
for root, _, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.apk'):
            apk_files.append(os.path.join(root, f))

if not apk_files:
    print("[!] 解壓後未找到任何 APK 檔案！")
    sys.exit(1)

target_apk = apk_files[0]
print(f"[+] APK 準備就緒：{target_apk}")

# 4. 檢查 ADB 設備並嘗試安裝
print("[*] 正在檢查 ADB 連接設備...")
adb_cmd = "adb"
res_devices = subprocess.run([adb_cmd, "devices"], capture_output=True, text=True)
device_lines = [l for l in res_devices.stdout.splitlines() if l.strip() and not l.startswith("List of")]

connected_devices = [l.split()[0] for l in device_lines if '\tdevice' in l]
if not connected_devices:
    print("[!] 目前未檢測到已授權連線的 Android 設備。")
    print(f"[+] APK 已妥善保存在：{target_apk}")
    print("[+] 當您連接好掌機或手機後，隨時可雙擊 deploy.bat 進行部署安裝！")
    sys.exit(0)

device_id = connected_devices[0]
package_name = "org.dolphinemu.mmjr.zh"
main_activity = "org.dolphinemu.dolphinemu.ui.main.MainActivity"

print(f"[*] 正在部署 APK 至設備 {device_id}...")
res_install = subprocess.run([adb_cmd, "-s", device_id, "install", "-r", "-d", target_apk], capture_output=True, text=True)
print(res_install.stdout)
if res_install.stderr:
    print(res_install.stderr)

if "INSTALL_FAILED_UPDATE_INCOMPATIBLE" in res_install.stdout or "INSTALL_FAILED_UPDATE_INCOMPATIBLE" in res_install.stderr:
    print("[提示] 檢測到簽章不相符，正在自動解除安裝舊版本並重新安裝...")
    subprocess.run([adb_cmd, "-s", device_id, "uninstall", package_name], capture_output=True)
    res_retry = subprocess.run([adb_cmd, "-s", device_id, "install", "-r", "-d", target_apk], capture_output=True, text=True)
    print(res_retry.stdout)

# 5. 喚醒設備並啟動 App
print(f"[*] 正在喚醒設備螢幕並啟動 {package_name}...")
subprocess.run([adb_cmd, "-s", device_id, "shell", "input", "keyevent", "224"], capture_output=True)
subprocess.run([adb_cmd, "-s", device_id, "shell", "wm", "dismiss-keyguard"], capture_output=True)

res_start = subprocess.run([adb_cmd, "-s", device_id, "shell", "am", "start", "-n", f"{package_name}/{main_activity}"], capture_output=True, text=True)
print(res_start.stdout)

print("==========================================================")
print("  [完成] Dolphin-MMJR2-VBI-zh 掌機部署全部順利完成！")
print("==========================================================")
