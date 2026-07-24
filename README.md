# 浪誌 TIDELOG

衝浪部落格網站草稿。

## 資料夾結構（v3・多頁＋分頁版）

```
tidelog-site/
├── index.html              首頁（hero 影片、本週精選 4 篇、浪點資料庫）
├── articles.html           衝浪文章列表頁，內建分頁功能（每頁 4 篇，共 10 篇示範）
├── articles/
│   ├── wushi-gang.html     唯一一篇有實際內容的文章（烏石港攻略）
│   └── (其餘 9 個).html     示範用佔位文章，內容都寫「之後要補的內容」
├── css/
│   └── styles.css          全站共用樣式（原本寫在 <style> 裡，現在抽出來一個檔案）
├── videos/
│   └── hero-surf.mp4       首頁背景影片
├── images/                 文章配圖放這裡（目前是空的，補圖片直接丟進來即可）
└── README.md
```

### 分頁功能怎麼運作
`articles.html` 用最簡單的**前端 JavaScript** 做分頁：所有文章卡片其實都在同一個網頁裡，
JS 只是控制「目前顯示第幾頁的卡片、隱藏其他頁」，配合底部的頁碼按鈕切換。
好處是不用後端、不用重新整理網頁；缺點是文章一多（例如上百篇），全部卡片都要載入，
到時候如果文章量變大，可以考慮換成真正的「多頁實體檔案」或接資料庫。

### 新增一篇文章的流程
1. 打開 `gen_site.py`（如果你想用產生器）或直接手動複製 `articles/wushi-gang.html` 當模板
2. 複製一份到 `articles/你的文章id.html`，改標題／內文／圖片路徑（注意文章頁要用 `../images/...`，多一層 `../`）
3. 到 `articles.html` 的卡片列表裡新增一張卡片（複製現有一張，改連結、標題、摘要）
4. 存檔，`git add . && git commit -m "新增文章：xxx" && git push`

所有頁面的圖片、影片、CSS 都用**相對路徑**，只要檔名對得上、資料夾結構不變，
不管在本機打開還是部署到網路上都能正常顯示。

---

## 第一次上傳到 GitHub

### 前置需求
- 有 GitHub 帳號（https://github.com 註冊）
- 電腦裝好 git（終端機打 `git --version` 看有沒有反應，Mac/大多數 Linux 通常內建）

### 步驟

1. 到 GitHub 網站建立一個新的 repository（右上角 + → New repository），
   名字可以取 `tidelog`，不要勾選「加 README」（因為我們已經有了），建立完會看到一串指令。

2. 在這個資料夾（`tidelog-site/`）打開終端機，依序執行：

   ```bash
   git init
   git add .
   git commit -m "first commit: 首頁 + hero 影片"
   git branch -M main
   git remote add origin https://github.com/你的帳號/tidelog.git
   git push -u origin main
   ```

3. 到 GitHub repo 頁面 → Settings → 左側選單找 **Pages** →
   Source 選 `main` branch，資料夾選 `/ (root)` → Save。

4. 等 1–2 分鐘，頁面會出現網址，格式像：
   `https://你的帳號.github.io/tidelog/`
   打開就是你的網站正式上線版本。

---

## 之後要新增/修改內容（例如補圖片、換影片、加文章）

1. 直接在這個資料夾裡改檔案（例如把新圖片丟進 `images/`，改 `index.html`）
2. 打開終端機，切到這個資料夾，執行：

   ```bash
   git add .
   git commit -m "說明這次改了什麼，例如：補烏石港文章圖片"
   git push
   ```

3. 等 1 分鐘左右，GitHub Pages 網站會自動更新，不用手動重新部署。

---

## 注意事項

- **GitHub 對單一檔案有 100MB 限制**。目前 `hero-surf.mp4` 只有約 1.1MB 沒問題，
  但如果之後累積很多支高畫質影片，建議影片改放外部空間
  （例如 Cloudflare R2、Bunny.net，或 YouTube 不公開連結嵌入），
  `index.html` 裡改成指向外部影片網址即可，其他都不用動。
- 如果不想碰指令列，也可以改用 **GitHub Desktop**（圖形介面版），
  操作是「開資料夾 → 寫commit訊息 → 按 Push」，效果一樣。
- 圖片建議先壓縮過（網頁用圖通常抓 1MB 以內、寬度 1600px 以內就很夠），
  避免網站載入變慢。
