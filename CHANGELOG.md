# 修改紀錄與索引追溯日誌 (Changelog & Modification Index)

本檔案記錄 Dolphin-MMJR2-VBI 專案之重大架構變更、在地化多語系支援與各項客製化維護紀錄。

---

## [MOD-20260920-18] Android 前端完整 100% 台灣繁體在地化與原生語系架構支援

- **索引編號**：`[MOD-20260920-18]`
- **日期**：2026-09-20
- **類別**：功能新增 / 國際化在地化 (Feature / i18n)
- **作者**：yangyws

### 1. 修改動機與原本問題 (Why)
- 開源模擬器專案 **Dolphin-MMJR2-VBI**（GameCube / Wii 掌機熱門效能增強分支）在 Android 前端一直未提供繁體中文介面，過去僅具備英文資源檔（`res/values/strings.xml`），導致繁體中文使用者在掌機操作與進階效能設定（如 VBI Skip、EFB/XFB 快取、著色器編譯、按鍵映射等）時面臨語言障礙。
- 遵循專案規範與 Android 原生在地化架構，以官方主開發分支 `rolling-dev` 為基礎建立完整的台灣繁體中文在地化資源，並準備向作者發起 Pull Request (PR)。

### 2. 涉及檔案與模組清單 (Where)
- 新增：[`Source/Android/app/src/main/res/values-zh-rTW/strings.xml`](file:///D:/github/Dolphin-MMJR2-VBI/Source/Android/app/src/main/res/values-zh-rTW/strings.xml)（完整 602 條字串 100% 台灣繁體中文在地化）
- 新增：[`Source/Android/app/src/main/res/xml/locales_config.xml`](file:///D:/github/Dolphin-MMJR2-VBI/Source/Android/app/src/main/res/xml/locales_config.xml)（Android 13+ 官方標準應用程式專用偏好語言宣告清單）
- 修改：[`Source/Android/app/src/main/AndroidManifest.xml`](file:///D:/github/Dolphin-MMJR2-VBI/Source/Android/app/src/main/AndroidManifest.xml)（在 `<application>` 標籤中註冊 `android:localeConfig="@xml/locales_config"`）
- 新增：[`CHANGELOG.md`](file:///D:/github/Dolphin-MMJR2-VBI/CHANGELOG.md)（變更紀錄與追溯索引檔）

### 3. 具體技術解法與決策細節 (How)
1. **官方 PO 核心術語對齊**：
   - 參照 Dolphin 官方 C++ 核心語系字典 `Languages/po/zh_TW.po`（包含 11,780 行翻譯資料庫），嚴格統一模擬器核心專業名詞（如：EFB、XFB、VBI Skip、JIT、逐像素光照、內部算繪解析度、非等方性過濾、全景反鋸齒、金手指作弊碼等）。
2. **嚴格符合台灣繁體中文 (zh-TW) 語系與科技標準用語**：
   - 杜絕中國大陸習慣用語與簡體字（如全面轉換：项目→專案、代码→程式碼、仓库→儲存庫、默认→預設、支持→支援、服务器→伺服器、内存→記憶體、屏幕→螢幕、分辨率→解析度、着色器/渲染器→著色器/算繪、手柄→搖桿/控制器、优化→最佳化）。
3. **Android XML 特殊字元與 AAPT 嚴格跳脫**：
   - 嚴格檢查並跳脫所有單引號（`\'`）與雙引號（`\"`），杜絕 AAPT2 單引號編譯中斷。
   - 所有純百分比標記（如 `0%`、`100%`、`%`）均標註 `formatted="false"`，防止資源編譯器將其誤判為格式化預留位置。
   - 妥善保留路徑中的角括號轉義（`&lt;game_id&gt;`）與 HTML 連結標籤（`<a href="...">`）。
4. **Android 13+ 原生多語系配置**：
   - 建立 `res/xml/locales_config.xml` 並支援 `en` 與 `zh-TW`，在 `AndroidManifest.xml` 完成配置，完美相容 Android 13+ 系統層級的個別應用程式語言動態熱切換。

### 4. 測試驗證結果 (Verification)
- **Python `xml.etree.ElementTree` 解析驗證**：成功解析，全數 602 條字串節點結構完整無誤。
- **PowerShell `[xml]` 驗證**：602 個字串資源全部通過驗證，無任何 XML 語法錯誤。
- **特殊符號與跳脫驗證**：未跳脫單引號計數為 0，異常 `&` 符號計數為 0，所有 XML 標籤均合規。
- **語系用語檢查**：簡體字與大陸用語偵測結果為 0，100% 通過台灣繁體用語規範。
