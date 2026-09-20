@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ========================================================
echo   Dolphin-MMJR2-VBI-zh - Android 掌機部署腳本
echo ========================================================
echo.

rem 1. 偵測 ADB 路徑
set "ADB=adb"
where adb >nul 2>nul
if %errorlevel% neq 0 (
    if exist "C:\platform-tools\adb.exe" (
        set "ADB=C:\platform-tools\adb.exe"
    ) else if exist "%LOCALAPPDATA%\Android\Sdk\platform-tools\adb.exe" (
        set "ADB=%LOCALAPPDATA%\Android\Sdk\platform-tools\adb.exe"
    ) else (
        echo [錯誤] 找不到 adb 指令！請確認已安裝 Android SDK Platform Tools。
        pause
        exit /b 1
    )
)

echo [*] 使用 ADB 工具：%ADB%

rem 2. 檢查連線裝置
echo [*] 正在檢查已連線之 Android 掌機/設備...
%ADB% devices
for /f "tokens=1,2" %%i in ('%ADB% devices ^| findstr /v "List" ^| findstr "device"') do (
    set "DEVICE_ID=%%i"
)

if "%DEVICE_ID%"=="" (
    echo [警告] 未偵測到已連線並開啟 USB 除錯之 Android 設備！
    echo 請確認：
    echo   1. 掌機已開啟「開發人員選項」與「USB 除錯」。
    echo   2. 已使用傳輸線連接電腦，並於掌機螢幕上點選「一律允許此電腦進行除錯」。
    echo.
    pause
    exit /b 1
)

echo [+] 偵測到目標設備：%DEVICE_ID%
echo.

rem 3. 搜尋 APK 檔案
set "APK_FILE="

rem 優先搜尋本機 Gradle 建置產物
if exist "Source\Android\app\build\outputs\apk\release\app-release.apk" (
    set "APK_FILE=Source\Android\app\build\outputs\apk\release\app-release.apk"
) else if exist "Source\Android\app\build\outputs\apk\debug\app-debug.apk" (
    set "APK_FILE=Source\Android\app\build\outputs\apk\debug\app-debug.apk"
) else (
    rem 搜尋 output_apks 或目前目錄下之 APK
    for %%f in (output_apks\*.apk *.apk) do (
        if exist "%%f" (
            set "APK_FILE=%%f"
            goto :found_apk
        )
    )
)

:found_apk
if "%APK_FILE%"=="" (
    echo [提示] 尚未找到已編譯的 APK 檔案。
    echo 若您已從 GitHub Actions 下載產物，請將 .apk 放置於專案根目錄或 output_apks 資料夾後重新執行。
    echo 若欲在本機編譯，請先執行：
    echo   cd Source\Android
    echo   gradlew.bat assembleRelease
    echo.
    pause
    exit /b 1
)

echo [+] 準備安裝 APK：%APK_FILE%
echo [*] 正在推送並安裝至設備 %DEVICE_ID% (保留應用程式資料 -r -d)...
%ADB% -s %DEVICE_ID% install -r -d "%APK_FILE%"

if %errorlevel% equ 0 (
    echo.
    echo ========================================================
    echo   [成功] Dolphin-MMJR2-VBI-zh 已成功安裝！
    echo ========================================================
    echo.
    set /p LAUNCH="請問是否要立即在掌機上啟動 Dolphin-MMJR2-VBI-zh？(Y/N): "
    if /i "!LAUNCH!"=="Y" (
        echo [*] 正在啟動應用程式...
        %ADB% -s %DEVICE_ID% shell am start -n org.dolphinemu.mmjr.zh/org.dolphinemu.dolphinemu.ui.main.MainActivity 2>nul
        if %errorlevel% neq 0 (
            %ADB% -s %DEVICE_ID% shell am start -n org.dolphinemu.mmjr/org.dolphinemu.dolphinemu.ui.main.MainActivity 2>nul
        )
        if %errorlevel% neq 0 (
            %ADB% -s %DEVICE_ID% shell am start -n org.dolphinemu.mmjr.debug/org.dolphinemu.dolphinemu.ui.main.MainActivity 2>nul
        )
    )
) else (
    echo.
    echo [失敗] 安裝過程發生錯誤，請檢查上方 ADB 報錯訊息。
)

echo.
pause
