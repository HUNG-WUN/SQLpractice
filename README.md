<h1>SQLpractice 🗄️⚡</h1>

<p>A Web application built with Python Flask, SQLAlchemy, and relational/NoSQL database integration (MySQL & MongoDB) deployed for database practice and backend operations.</p>

<p>
  <a href="https://github.com/HUNG-WUN/SQLpractice"><img src="https://img.shields.io/badge/GitHub-Repository-blue?logo=github" alt="GitHub Repo"></a>
  <img src="https://img.shields.io/badge/Python-3.9+-green?logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.0+-000000?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/MySQL-PyMySQL-4479A1?logo=mysql" alt="MySQL">
  <img src="https://img.shields.io/badge/MongoDB-PyMongo-47A248?logo=mongodb" alt="MongoDB">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

<hr>

<h2>📌 專案簡介 (Overview)</h2>
<p><b>SQLpractice</b> 是一個結合關聯式資料庫（Relational DB）與 NoSQL 資料庫實作的 Flask Web 應用專案。本專案旨在提供完整的 ORM（Object-Relational Mapping）資料存取實作、資料庫連線池調校，以及使用者 CRUD 操作，適合進行資料庫後端開發與部署實務演練。</p>

<hr>

<h2>✨ 核心功能 (Key Features)</h2>
<ul>
  <li>🗄️ <b>雙資料庫架構 (Dual DB Integration)</b>：整合 MySQL 關聯式結構與 MongoDB 非關聯式文件資料庫。</li>
  <li>🔄 <b>ORM 資料庫操作 (SQLAlchemy ORM)</b>：透過 SQLAlchemy 物件化操作資料庫，提升程式碼安全與維護性。</li>
  <li>⚡ <b>連線池優化 (Connection Pooling)</b>：搭配 PyMySQL 與 PyMongo 管理資料庫連線，確保高效率存取。</li>
  <li>🌐 <b>RESTful API & Web UI</b>：提供前端互動頁面與後端 REST API 進行資料寫入、查詢與更新。</li>
  <li>🚀 <b>雲端部署 (Cloud Deployment)</b>：配置與驗證於 Render 平台，支援雲端資料庫串接。</li>
</ul>

<hr>

<h2>🛠️ 技術棧 (Tech Stack)</h2>

<table border="1">
  <thead>
    <tr>
      <th>領域</th>
      <th>技術 / 套件</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>後端框架 (Backend)</b></td>
      <td>Python 3.9+, Flask, Werkzeug</td>
    </tr>
    <tr>
      <td><b>關聯式資料庫 (SQL)</b></td>
      <td>MySQL, SQLAlchemy, PyMySQL</td>
    </tr>
    <tr>
      <td><b>NoSQL 資料庫</b></td>
      <td>MongoDB, PyMongo</td>
    </tr>
    <tr>
      <td><b>部署與運營 (DevOps)</b></td>
      <td>Render, Git</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>📁 專案目錄結構 (Directory Structure)</h2>

<pre><code>SQLpractice/
├── app/                  # 應用程式主要邏輯目錄
│   ├── routes/           # Web 與 API 路由定義
│   ├── models/           # SQLAlchemy & MongoDB 資料模型定义
│   └── static/           # 前端靜態資源 (CSS / JS)
├── app.py                # 應用程式執行進入點
├── config.py             # 資料庫連線設定與環境變數配置
├── requirements.txt      # Python 專案依賴清單
└── README.md             # 專案說明文件
</code></pre>

<hr>

<h2>🚀 快速開始 (Quick Start)</h2>

<h3>前置需求 (Prerequisites)</h3>
<ul>
  <li><a href="https://git-scm.com/">Git</a></li>
  <li><a href="https://www.python.org/">Python 3.9+</a></li>
  <li><a href="https://www.mysql.com/">MySQL Database</a></li>
</ul>

<h3>1. 克隆儲存庫 (Clone Repository)</h3>
<pre><code>git clone https://github.com/HUNG-WUN/SQLpractice.git
cd SQLpractice
</code></pre>

<h3>2. 建立並啟動虛擬環境 (Virtual Environment)</h3>
<pre><code>python -m venv venv

# Windows 啟動虛擬環境：
# venv\Scripts\activate

# macOS / Linux 啟動虛擬環境：
source venv/bin/activate
</code></pre>

<h3>3. 安裝依賴與設定環境變數 (Install Dependencies)</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>4. 啟動服務 (Run Application)</h3>
<pre><code>python app.py
</code></pre>

<p>💡 服務啟動後，開啟瀏覽器造訪：<code>http://localhost:5000</code></p>

<hr>

<h2>🤝 貢獻指南 (Contributing)</h2>
<p>歡迎提交 Pull Request 或開立 Issues 提出建議與改善方案！</p>
<ol>
  <li>Fork 本專案</li>
  <li>建立功能分支 (<code>git checkout -b feature/AmazingFeature</code>)</li>
  <li>提交變更 (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
  <li>推送至分支 (<code>git push origin feature/AmazingFeature</code>)</li>
  <li>開啟 Pull Request</li>
</ol>

<hr>

<h2>📜 授權條款 (License)</h2>
<p>本專案採用 <a href="LICENSE">MIT License</a> 授權條款。</p>
