# Dolphin MMJR2 - VBI 分支 (繁體中文版)

[English](README.md) | **台灣繁體中文**

---

本專案為 **Dolphin MMJR2** 的個人維護分支。此分支最初的目標是將 Sam Belliveau 所開發的 **VBI Skip (垂直消隱跳幀加速黑客)** 技術移植整合至 MMJR2 程式碼庫中，現已發展為持續維護的熱門掌機模擬器專案。

本分支的核心目標在於保留深受玩家喜愛的**經典 MMJR2 使用者介面**（更直覺且易於在觸控螢幕與掌機操作），同時支援小數點細部倍率縮放 (Fractional Scaling)，並持續整合來自 Dolphin 官方儲存庫的新功能與修復補丁。

---

## 🇹🇼 繁體中文化版本特色 (`[MOD-20260920-18]`)

* **100% 完整台灣繁體中文 (zh-TW)**：
  - 全數 602 條介面與設定字串完整在地化。
  - 對齊 Dolphin 官方核心詞庫（`Languages/po/zh_TW.po`），嚴格採用台灣科技與遊戲術語（如：搖桿、板機鍵、內部解析度、著色器、畫面幀率、最佳化、儲存庫、專案、預設等），無任何簡體字與大陸用語。
* **原生 Android 13+ 語系動態切換**：
  - 導入原生 `res/xml/locales_config.xml`，支援在 Android 系統設定中針對個別應用程式自由切換語言。
* **一鍵 ADB 掌機部署腳本 (`deploy.bat`)**：
  - 支援自動偵測連線之 Android 掌機設備（如 Odin、Retroid Pocket、ANBERNIC 等），一鍵推送更新安裝並啟動。
* **GitHub Actions 雲端自動建置管線**：
  - 推送程式碼時自動觸發雲端編譯，免去本機繁重的 NDK/C++ 編譯環境配置即可取得最新 APK 產物。

---

## 免責聲明 (Disclaimer)

* ⚠️ **警告**：本分支基於 Dolphin 早期專案程式碼架構，可能存在其自有的未知問題，且社群支援資源有限。若您是剛接觸模擬器的新手或追求最高相容性與穩定性，建議使用 [Dolphin 官方版本](https://dolphin-emu.org/)。

---

## 📱 Android 系統與硬體需求

* **作業系統**：
  - Android 5.0 (Lollipop) 或更高版本 (API Level >= 21)。
* **處理器 (CPU)**：
  - 支援 `arm64-v8a` ABI 之 64 位元 ARM 處理器。
* **圖形處理器 (GPU)**：
  - 支援 OpenGL ES 3.0 或更新版本之 GPU（效能表現深受 GPU 驅動程式品質影響）。
  - 強烈建議搭配支援 Vulkan API 之硬體以獲得最佳畫面更新率。

> Dolphin 僅能安裝於符合上述規格之設備上，未達標準之設備將無法完成安裝並會顯示錯誤提示。

---

## 📂 儲存路徑與資料夾結構

本分支的應用程式套件識別碼 (Package ID) 為 `org.dolphinemu.mmjr`，可與 Dolphin 官方版共存安裝，但**不能**與其他同套件 ID 的 MMJR2 版本同時安裝。

專案使用者資料目錄建立於裝置內部儲存空間的根目錄：`/mmjr2-vbi/`。

### 目錄結構解析：
* `Cache/`：遊戲封面快取、UID 快取與著色器快取 (Shader Cache)。
* `Config/`：全域與核心配置設定檔 (INI)。
* `Dump/`：紋理、音訊或畫面傾印匯出檔。
* `GameSettings/`：針對個別遊戲的專屬自訂設定檔。
* `GC/`：GameCube 虛擬記憶卡存檔與系統 BIOS 檔案 (`ipl.bin`)。
* `Load/`：繪圖 Mod、Riivolution 補丁、自訂高解析度材質包、WiiSDSync。
* `Logs/`：執行除錯記錄檔（若有開啟記錄功能）。
* `ResourcePacks/`：資源套件目錄（Android 端請優先使用 `Load` 資料夾）。
* `ScreenShots/`：在模擬器中擷取的遊戲螢幕截圖。
* `StateSaves/`：即時存檔檔案。
* `Wii/`：Wii 虛擬 NAND 系統檔案與遊戲本體存檔。

---

## 🎨 高解析度自訂材質包 (Custom Textures)

欲使用高畫質自訂材質包，請將材質圖檔放置於使用者目錄下的：
```text
/mmjr2-vbi/Load/Textures/[遊戲ID]/
```
> **提示**：您可以在遊戲清單中長按該遊戲圖示，並選擇「遊戲詳細資訊 (Details)」以查詢該遊戲專屬的 Game ID（如 `GALE01`）。

---

## 🧩 Riivolution 遊戲補丁 (Riivolution Patches)

欲掛載 Riivolution 補丁（如繁體中文漢化補丁、大型 Mod），請將解壓縮後的補丁資料夾放置於：
```text
/mmjr2-vbi/Load/Riivolution/[遊戲ID]/
```
放置完成後，在主介面中長按該遊戲，並選取**「載入 Riivolution 補丁啟動」**即可。

---

## 🚀 取得與安裝方式

### 方式一：從 GitHub Actions 雲端下載預先編譯 APK（最方便）
1. 進入本專案 GitHub 儲存庫頁面，點選頂部 **Actions** 分頁。
2. 點選最新一次成功的 `Build Android APK` 工作流。
3. 於頁面下方的 **Artifacts** 區塊下載 `dolphin-mmjr2-vbi-android-apk`。
4. 解壓縮後將 APK 透過傳輸線或 `deploy.bat` 安裝至掌機。

### 方式二：使用一鍵 ADB 腳本部署至掌機 (`deploy.bat`)
1. 確保掌機已開啟「USB 除錯」並以傳輸線連接至電腦。
2. 將下載或編譯好的 `.apk` 放置於專案根目錄。
3. 雙擊執行根目錄下的 [`deploy.bat`](deploy.bat)，腳本將自動偵測設備、安裝並詢問是否立即在掌機上開啟。

### 方式三：本機自原始碼編譯
本專案已整合 Gradle 與 Android NDK C++ 編譯架構：
```pwsh
# 1. 遞迴同步所有 C++ submodules (重要)
git submodule update --init --recursive

# 2. 進入 Android 前端目錄
cd Source/Android

# 3. 執行 Gradle 編譯 Release APK
./gradlew.bat assembleRelease
```
編譯完成之 APK 位於：`Source/Android/app/build/outputs/apk/release/app-release.apk`。

---

## 👏 致謝與致敬 (Acknowledgments)

衷心感謝以下優秀的開發團隊與先驅貢獻者：
* **Dolphin Team**：感謝官方團隊數十年如一日的堅持與貢獻，讓經典遊戲能在現代硬體上完美重現！🐬
* **原始 MMJR 與 MMJR2 開發者**：感謝建立並維護這些掌機優化分支的開拓者。
* **Lumince**：感謝長期維護 MMJR2 並無私開源讓社群得以延續成果。
* **Sam Belliveau**：感謝開發出神奇的 VBI Skip 跳幀加速技術。
* **Bankaimaster999、sspacelynx 與 Weihuoya (偉哥)**：感謝對 Android 掌機模擬器生態的重要貢獻。

---

## 📜 授權條款 (License)

Dolphin 採用 **GNU General Public License, version 2 or later (GPLv2+)** 授權條款開源釋出。請參閱各模組中的 License 檔案以取得更多法律詳細資訊。
