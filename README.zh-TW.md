# Dolphin MMJR2 - VBI 分支

[English](README.md) | **台灣繁體中文**

---

本專案為 **Dolphin MMJR2** 的個人維護分支。此分支最初的目標是將 Sam Belliveau 所開發的 **VBI Skip (垂直消隱跳幀加速技術)** 移植整合至 MMJR2 程式碼庫中，現已發展為持續維護的模擬器專案。本分支的核心重點在於保留深受玩家喜愛的經典 MMJR2 使用者介面（在觸控螢幕與掌機操作上更直覺且易用），同時支援小數點細部倍率縮放 (Fractional Scaling)，並持續整合來自 Dolphin 官方儲存庫的新功能與修復補丁。

## 免責聲明
- **⚠️ 警告**：本分支基於較早期的原始碼架構！可能存在其自有的問題，且能提供的支援非常有限。若您是剛接觸模擬器的新手或追求最高穩定性，建議使用 [Dolphin 官方版本](https://dolphin-emu.org/)。

## Android 系統需求

* 作業系統 (OS)
    * Android 5.0 (Lollipop) 或更高版本 (SDK >= 21)。
* 處理器 (Processor)
    * 支援 `arm64-v8a` ABI 之 64 位元 ARM 處理器。
* 顯示晶片 (Graphics)
    * 支援 OpenGL ES 3.0 或更新版本之繪圖處理器。效能表現深受[驅動程式品質](https://dolphin-emu.org/blog/2013/09/26/dolphin-emulator-and-opengl-drivers-hall-fameshame/)影響。
    * 強烈建議使用支援標準桌面級 OpenGL 功能之繪圖處理器以獲得最佳效能。

Dolphin 僅能安裝於符合上述規格之裝置上，未達標準之裝置將無法完成安裝並會顯示錯誤提示。

## 其他資訊
- 本分支的使用者資料目錄建立於裝置內部儲存空間根目錄下的 `/mmjr2-vbi/`。
- 本分支的應用程式識別碼 (ID) 為 `org.dolphinemu.mmjr`。可與 Dolphin 官方版本共存安裝，但無法與其他同 ID 的 MMJR2 版本同時安裝。

## 資料夾結構
* `Cache`：遊戲封面、UID 快取與著色器快取 (Shader Cache)
* `Config`：設定檔
* `Dump`：自 Dolphin 傾印匯出的任何檔案
* `GameSettings`：針對個別遊戲的專屬自訂設定檔
* `GC`：虛擬記憶卡與系統 BIOS
* `Load`：繪圖 Mod、Riivolution 補丁、自訂高解析度材質包、WiiSDSync
* `Logs`：執行記錄檔（若有開啟）
* `ResourcePacks`：Android 版本不支援資源包 (Resource Packs)，請改用 `Load` 資料夾
* `ScreenShots`：透過 Dolphin 擷取的遊戲螢幕截圖
* `StateSaves`：即時存檔檔案（若有開啟）
* `Wii`：Wii 虛擬 NAND 內容

## 自訂高解析度材質包 (Custom Textures)
自訂材質圖檔必須放置於使用者目錄下的 `Load/Textures/[遊戲ID]/`。您可以在遊戲清單中長按該遊戲圖示並選擇「詳細資訊 (Details)」以查詢遊戲 ID。

## Riivolution 遊戲補丁 (Riivolution Patches)
Riivolution 補丁必須放置於使用者目錄下的 `Load/Riivolution/[遊戲ID]/`。將補丁解壓縮至該處後，長按遊戲並選擇「載入 Riivolution 補丁啟動 (Start with Riivolution Patches)」。

## 致謝 (Acknowledgments)
衷心感謝以下貢獻者：
- **Dolphin Team**：感謝官方團隊的卓越貢獻，讓模擬器得以在現代硬體上實現。你們的熱情與奉獻令人欽佩！🐬👏
- **原始 MMJR 與 MMJR2 開發者**：感謝建立並維護這些分支的先驅。
- **Lumince**：感謝長期維護 MMJR2 並無私開源讓成果得以延續。
- **Sam Belliveau**：感謝開發出開啟這一切的 VBI Skip 跳幀加速技術。

## 最後附註 (Last Notes)
我在業餘時間維護這個分支，雖然我不敢自稱是專業開發者，但這是學習程式碼與應用程式開發的有趣方式。

非常歡迎任何形式的協助。若您想參與貢獻，請在 [Discussions 討論區](https://github.com/Medard22/Dolphin-MMJR2-VBI/discussions) 留言。

您可以在[此處](https://github.com/Medard22/Dolphin-MMJR2-VBI/discussions/45)查閱最新的變更紀錄。

---

## Dolphin MMJR2 分支說明
本分支主要供個人使用。本儲存庫當前的主要功能是將 MMJR2 更新至最新的 Dolphin 官方開發版原始碼，且未合併分區儲存 (scoped storage) 的相關變更。
若您需要分區儲存，請使用 Dolphin 官方發布版本。我不需要分區儲存，亦不需要與其相關的任何改動，因此我不會合併這些變更。祝您使用愉快！

這是一款專注於效能的 Android 專用 Dolphin 分支，以最新的 Dolphin 開發版本為基礎進行 rebase 重整，重新實作了 MMJ 的使用者體驗與效能改進，並加入了我們自訂的功能。

請至 [Releases 發布頁面](https://github.com/Lumince/Dolphin-MMJR2/releases) 下載最新版本，或在應用程式內部的更新器中檢查新版本。舊版 MMJR v1.0 可至舊儲存庫[此處](https://github.com/Bankaimaster999/Dolphin-MMJR/releases)取得。1.0 與 2.0 版本使用不同資料夾，因此可共存安裝互不衝突，但**即時存檔並不相容**。我們懇請您避免濫用 GitHub Issues 與 Pull Requests。

如果沒有技術遠勝於我們的開發者們在 Dolphin 官方所傾注的龐大心血，這個分支根本不可能存在。

---

## Dolphin - GameCube 與 Wii 模擬器

[官方網站](https://dolphin-emu.org/) | [專案網站](https://github.com/dolphin-emu/dolphin) | [建置機器人](https://dolphin.ci/) | [官方論壇](https://forums.dolphin-emu.org/) | [官方 Wiki](https://wiki.dolphin-emu.org/) | [GitHub Wiki](https://github.com/dolphin-emu/dolphin/wiki) | [問題追蹤器](https://bugs.dolphin-emu.org/projects/emulator/issues) | [程式碼風格](https://github.com/dolphin-emu/dolphin/blob/master/Contributing.md) | [Transifex 頁面](https://app.transifex.com/delroth/dolphin-emu/dashboard/)

Dolphin 是一款可在 Windows、Linux、macOS 以及近代 Android 裝置上執行 GameCube 與 Wii 遊戲的模擬器。它採用 GNU General Public License, version 2 or later (GPLv2+) 授權條款開源釋出。

使用 Dolphin 之前，請先閱讀[常見問題 (FAQ)](https://dolphin-emu.org/docs/faq/)。

## 系統需求 (System Requirements)

### 電腦桌面端 (Desktop)

* 作業系統 (OS)
    * Windows (10 或更高版本)。
    * Linux。
    * macOS (10.15 Catalina 或更高版本)。
    * Linux 以外的類 Unix 系統雖未獲得官方正式支援，但仍可能可以運作。
* 處理器 (Processor)
    * 支援 SSE2 指令集的 CPU。
    * 強烈建議使用現代 CPU（3 GHz 且為雙核心以上，年份不早於 2008 年）。
* 顯示晶片 (Graphics)
    * 規格適度現代的獨立顯示卡（支援 Direct3D 11.1 / OpenGL 3.3）。
    * 建議使用支援 Direct3D 11.1 / OpenGL 4.4 的顯示卡。

### 行動裝置端 (Android)

* 作業系統 (OS)
    * Android (5.0 Lollipop 或更高版本)。
* 處理器 (Processor)
    * 支援 64 位元應用程式的處理器（ARMv8 或 x86-64 架構）。
* 顯示晶片 (Graphics)
    * 支援 OpenGL ES 3.0 或更新版本之繪圖處理器。效能表現深受[驅動程式品質](https://dolphin-emu.org/blog/2013/09/26/dolphin-emulator-and-opengl-drivers-hall-fameshame/)影響。
    * 強烈建議使用支援標準桌面級 OpenGL 功能之繪圖處理器以獲得最佳效能。

Dolphin 僅能安裝於符合上述規格之裝置上，未達標準之裝置將無法完成安裝並會顯示錯誤提示。

## Windows 建置指南 (Building for Windows)

在 Windows 上請使用方案檔 `Source/dolphin-emu.sln` 建置 Dolphin。
Dolphin 針對隨 Visual Studio 或 Build Tools 一併安裝的最新 MSVC 編譯器進行設計。其他編譯器或許也能在 Windows 上建置 Dolphin，但未經驗證且不建議使用。建置時必須安裝 Git 以及最新的 Windows SDK。

建置前請務必遞迴拉取 submodules：
```sh
git submodule update --init --recursive
```

「Release」方案組態包含供最佳使用者體驗的效能最佳化，但會增加偵錯 Dolphin 的難度。
「Debug」方案組態速度明顯較慢、輸出資訊更詳細且較不具容錯度，但讓偵錯 Dolphin 更為容易。

## Linux 與 macOS 建置指南 (Building for Linux and macOS)

在 Windows 以外的系統上，Dolphin 需要使用 [CMake](https://cmake.org/)。
您需要具備完善 C++20 支援的近期版本 GCC 或 Clang。若您的編譯器版本過舊，CMake 會給予提示。
許多函式庫已隨 Dolphin 一併封裝，若您的系統中未安裝則會直接使用內建函式庫。CMake 會回報是否使用了隨附的函式庫，或者您是否需要自行安裝任何缺少的相依套件。更多資訊可參閱 [Wiki](https://github.com/dolphin-emu/dolphin/wiki/Building-for-Linux)。

建置前請務必遞迴拉取 submodules：
```sh
git submodule update --init --recursive
```

### macOS 建置步驟：

建置支援單一架構的二進位檔案可依照以下步驟：

1. `mkdir build`
2. `cd build`
3. `cmake ..`
4. `make -j $(sysctl -n hw.logicalcpu)`

應用程式套件 (Application Bundle) 將產出於 `./Binaries`。

專案亦提供建置腳本，可透過以下步驟在同一個應用程式套件中建置支援 x64 與 ARM 雙架構的通用二進位檔案 (Universal Binary)：

1. `mkdir build`
2. `cd build`
3. `python ../BuildMacOSUniversalBinary.py`
4. 通用二進位檔案將存放於 `universal` 資料夾

此程序較為複雜，因為它需要安裝同時支援 x64 與 ARM 的函式庫相依套件（或同等的通用函式庫），並可能需要指定額外參數指向相應的函式庫路徑。執行 `BuildMacOSUniversalBinary.py --help` 可取得更多詳細資訊。

### Linux 全域安裝步驟：

若要安裝至您的作業系統：

1. `mkdir build`
2. `cd build`
3. `cmake ..`
4. `make -j $(nproc)`
5. `sudo make install`

### Linux 本機開發建置步驟：

適合開發使用，無需 root 權限：

1. `mkdir Build`
2. `cd Build`
3. `cmake .. -DLINUX_LOCAL_DEV=true`
4. `make -j $(nproc)`
5. `ln -s ../../Data/Sys Binaries/`

### Linux 可攜式建置步驟：

可儲存於外接式儲存裝置並在不同的 Linux 系統上執行。亦適用於維護多個獨立的 Dolphin 設定以進行測試、開發或 TAS 製作：

1. `mkdir Build`
2. `cd Build`
3. `cmake .. -DLINUX_LOCAL_DEV=true`
4. `make -j $(nproc)`
5. `cp -r ../Data/Sys/ Binaries/`
6. `touch Binaries/portable.txt`

## Android 建置指南 (Building for Android)

以下指示假設您已熟悉 Android 開發流程。若您尚未配置好 Android 開發環境，請參閱 [AndroidSetup.md](AndroidSetup.md)。

建置前請務必遞迴拉取 submodules：
```sh
git submodule update --init --recursive
```

若使用 Android Studio，請匯入位於 `./Source/Android` 的 Gradle 專案。

Android 應用程式使用名為 Gradle 的建置系統進行編譯。然而 Dolphin 的原生核心組件是使用 CMake 進行編譯。Gradle 腳本會在建置 Java 程式碼時自動嘗試執行 CMake 建置。

## 移除方式 (Uninstalling)

在 Windows 上，只需刪除解壓縮後的資料夾即可；若您是透過 NSIS 安裝程式安裝，則可像一般 Windows 應用程式一樣進行解除安裝。

Linux 使用者可從 build 目錄以 root 權限執行 `cat install_manifest.txt | xargs -d '\n' rm`，以從系統中移除 Dolphin。

macOS 使用者只需將 Dolphin.app 丟入垃圾桶刪除即可。

此外，若您不打算重新安裝 Dolphin，建議將全域使用者設定目錄一併刪除。

## 指令列使用方式 (Command Line Usage)

```text
用法: Dolphin.exe [選項]... [檔案]...

選項:
  --version             顯示程式版本號碼並結束
  -h, --help            顯示此說明訊息並結束
  -u USER, --user=USER  使用者資料夾路徑
  -m MOVIE, --movie=MOVIE
                        播放影片檔案
  -e <file>, --exec=<file>
                        載入指定的遊戲檔案
  -n <16字元ASCII識別碼>, --nand_title=<16字元ASCII識別碼>
                        啟動指定的 NAND 標題
  -C <System>.<Section>.<Key>=<Value>, --config=<System>.<Section>.<Key>=<Value>
                        設定組態設定選項
  -s <file>, --save_state=<file>
                        載入初始即時存檔檔案
  -d, --debugger        顯示偵錯面板與額外的「檢視」選單選項
  -l, --logger          開啟記錄器
  -b, --batch           在無使用者介面 (UI) 的情況下執行 Dolphin (需要 --exec 或 --nand-title)
  -c, --confirm         設定停止執行時進行確認
  -v VIDEO_BACKEND, --video_backend=VIDEO_BACKEND
                        指定繪圖後端
  -a AUDIO_EMULATION, --audio_emulation=AUDIO_EMULATION
                        選擇音訊模擬方式 [HLE|LLE]
```

可用的 DSP 模擬引擎為 HLE（高階模擬）與 LLE（低階模擬）。HLE 速度較快但精準度稍低；LLE 速度較慢但近乎完美。請注意，LLE 具備兩種子模式（直譯器 Interpreter 與 JIT 重新編譯器 Recompiler），但無法直接從指令列中進行挑選。

可用的繪圖後端包括「D3D」與「D3D12」（僅適用於 Windows）、「OGL」以及「Vulkan」。此外還有「Null」（不渲染任何畫面）以及「Software Renderer」（使用 CPU 進行軟體渲染，僅供除錯用途）。

## DolphinTool 使用方式 (DolphinTool Usage)

```text
用法: dolphin-tool 指令 -h

支援的指令: [convert, verify, header, extract]
```

```text
用法: convert [選項]... [檔案]...

選項:
  -h, --help            顯示此說明訊息並結束
  -u USER, --user=USER  使用者資料夾路徑，處理暫存檔案時所需。若未設定將自動建立。
  -i FILE, --input=FILE
                        光碟映像檔輸入路徑。
  -o FILE, --output=FILE
                        目標檔案輸出路徑。
  -f FORMAT, --format=FORMAT
                        欲使用的容器格式。預設為 RVZ。[iso|gcz|wia|rvz]
  -s, --scrub           轉換時一併清除無效垃圾資料。
  -b BLOCK_SIZE, --block_size=BLOCK_SIZE
                        GCZ/WIA/RVZ 格式的區塊大小（整數）。建議 RVZ 使用: 131072 (128 KiB)。
  -c COMPRESSION, --compression=COMPRESSION
                        轉換為 WIA/RVZ 格式時採用的壓縮演算法。建議 RVZ 使用: zstd [none|zstd|bzip|lzma|lzma2]。
  -l COMPRESSION_LEVEL, --compression_level=COMPRESSION_LEVEL
                        所選壓縮方法的等級。若為 'none' 則忽略。建議 zstd 使用: 5。
```

```text
用法: verify [選項]...

選項:
  -h, --help            顯示此說明訊息並結束
  -u USER, --user=USER  使用者資料夾路徑，處理暫存檔案時所需。若未設定將自動建立。
  -i FILE, --input=FILE
                        光碟映像檔輸入路徑。
  -a ALGORITHM, --algorithm=ALGORITHM
                        選用。使用指定的雜湊演算法計算並印出摘要值後結束。[crc32|md5|sha1]
```

```text
用法: header [選項]...

選項:
  -h, --help            顯示此說明訊息並結束
  -i FILE, --input=FILE
                        光碟映像檔輸入路徑。
  -b, --block_size      選用。印出 GCZ/WIA/RVZ 格式的區塊大小後結束。
  -c, --compression     選用。印出 GCZ/WIA/RVZ 格式的壓縮方法後結束。
  -l, --compression_level
                        選用。印出 WIA/RVZ 格式的壓縮等級後結束。
```

```text
用法: extract [選項]...

選項:
  -h, --help            顯示此說明訊息並結束
  -i FILE, --input=FILE
                        光碟映像檔輸入路徑。
  -o FOLDER, --output=FOLDER
                        目標資料夾輸出路徑。
  -p PARTITION, --partition=PARTITION
                        欲解壓縮的特定分割區。
  -s SINGLE, --single=SINGLE
                        欲解壓縮的特定檔案/目錄。
  -l, --list            列出磁區/分割區中的所有檔案。若有指定 --single 則印出該目錄/檔案。
  -q, --quiet           靜音所有訊息（錯誤除外）。
  -g, --gameonly        僅解壓縮 DATA 資料分割區。
```
