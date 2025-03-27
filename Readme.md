# ToDo 應用程式 Docker 專案

這是一個使用 Django 和 PostgreSQL 構建的待辦事項應用程式，採用 Docker 容器化部署。

## 專案概述

此專案是一個完整的待辦事項管理系統，允許使用者創建、編輯、刪除和標記待辦事項的完成狀態。整個應用程式使用 Docker 和 Docker Compose 進行容器化，確保開發和部署環境的一致性。

## 技術堆疊

- **後端框架**: Django 5.1.7
- **資料庫**: PostgreSQL 14
- **容器化**: Docker & Docker Compose
- **資料庫管理**: pgAdmin 4 (選配)
- **程式語言**: Python 3.9

## 系統架構

專案包含三個主要的 Docker 容器：

1. **Web 應用程式 (web)**: 運行 Django 應用程式
2. **資料庫 (db)**: PostgreSQL 資料庫服務
3. **資料庫管理介面 (pgadmin)**: 提供 PostgreSQL 的 Web 管理界面 (選配)

## 功能特點

- 使用者註冊與登入系統
- 待辦事項的 CRUD 操作 (創建、讀取、更新、刪除)
- 待辦事項狀態管理 (完成/未完成)
- 待辦事項優先級設定
- 待辦事項分類與標籤
- 響應式設計，適配桌面和移動設備

## 安裝與設置

### 前置需求

- Docker Desktop
- Docker Compose

### 安裝步驟

1. 克隆此專案到本地:
   ```
   git clone <repository-url>
   cd todo_docker_project
   ```

2. 啟動 Docker 容器:
   ```
   docker-compose up -d
   ```

3. 初始化資料庫:
   ```
   docker-compose exec web python manage.py migrate
   ```

4. 創建超級使用者 (可選):
   ```
   docker-compose exec web python manage.py createsuperuser
   ```

5. 訪問應用程式:
   - Web 應用程式: http://localhost:8000/
   - Django 管理介面: http://localhost:8000/admin/
   - pgAdmin 介面: http://localhost:5050/ (使用 admin@example.com / adminpassword 登入)

## 專案結構

```
todo_docker_project/
├── docker-compose.yml        # Docker Compose 配置文件
├── Dockerfile                # Web 服務的 Docker 配置
├── manage.py                 # Django 專案管理腳本
├── requirements.txt          # Python 依賴包列表
├── todo_project/            # Django 專案主目錄
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Django 設定檔
│   ├── urls.py              # URL 路由配置
│   └── wsgi.py
└── todo_app/                # Django 應用程式
    ├── __init__.py
    ├── admin.py             # 管理介面配置
    ├── apps.py
    ├── forms.py             # 表單定義
    ├── migrations/          # 資料庫遷移文件
    ├── models.py            # 資料模型定義
    ├── templates/           # HTML 模板
    ├── tests.py             # 單元測試
    ├── urls.py              # 應用程式 URL 路由
    └── views.py             # 視圖函數
```

## 環境變數

專案使用以下環境變數，可在 `docker-compose.yml` 中配置：

**DEBUG**
- 描述: 是否啟用調試模式
- 預設值: 1 (開發環境)

**SECRET_KEY**
- 描述: Django 密鑰
- 預設值: django-insecure-key-for-development-only

**POSTGRES_DB**
- 描述: 資料庫名稱
- 預設值: todo_db

**POSTGRES_USER**
- 描述: 資料庫使用者
- 預設值: postgres

**POSTGRES_PASSWORD**
- 描述: 資料庫密碼
- 預設值: postgres

**POSTGRES_HOST**
- 描述: 資料庫主機
- 預設值: db

**POSTGRES_PORT**
- 描述: 資料庫端口
- 預設值: 5432

## 資料庫設計

### Task (待辦事項) 模型

- **title**: 待辦事項標題
- **description**: 詳細描述
- **created_at**: 創建時間
- **due_date**: 截止日期
- **completed**: 完成狀態
- **priority**: 優先級 (高/中/低)
- **user**: 關聯的使用者 (外鍵)

## API 端點

**首頁/待辦事項列表**
- 端點: `/`
- 方法: GET

**創建新待辦事項**
- 端點: `/task/new/`
- 方法: GET/POST

**查看待辦事項詳情**
- 端點: `/task/<id>/`
- 方法: GET

**編輯待辦事項**
- 端點: `/task/<id>/edit/`
- 方法: GET/POST

**刪除待辦事項**
- 端點: `/task/<id>/delete/`
- 方法: GET/POST

**標記待辦事項為完成**
- 端點: `/task/<id>/complete/`
- 方法: POST

**使用者登入**
- 端點: `/accounts/login/`
- 方法: GET/POST

**使用者登出**
- 端點: `/accounts/logout/`
- 方法: GET/POST

**使用者註冊**
- 端點: `/accounts/register/`
- 方法: GET/POST

## 開發指南

### 添加新功能

1. 在 `todo_app/models.py` 中定義新的資料模型
2. 創建並應用遷移:
   ```
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```
3. 在 `todo_app/views.py` 中添加相應的視圖函數
4. 在 `todo_app/urls.py` 中添加新的 URL 路由
5. 在 `todo_app/templates/` 中創建必要的 HTML 模板

### 運行測試

```
docker-compose exec web python manage.py test
```

## 常見問題排解

### Docker 容器無法啟動

- 檢查 Docker Desktop 是否正在運行
- 確保端口 8000、5432 和 5050 未被其他應用程式佔用
- 查看容器日誌以獲取詳細錯誤信息:
  ```
  docker-compose logs
  ```

### 資料庫連接問題

- 確保 PostgreSQL 容器已啟動並健康運行
- 檢查 `settings.py` 中的資料庫配置是否正確
- 嘗試重新啟動 web 容器:
  ```
  docker-compose restart web
  ```

### 權限問題

- 確保 Docker 容器內的文件權限設置正確
- 如果在 Linux 系統上運行，可能需要調整宿主機上的文件權限

## 部署到生產環境

生產環境部署需要額外的安全配置：

1. 修改 `settings.py`:
   - 設置 `DEBUG = False`
   - 更新 `ALLOWED_HOSTS`
   - 配置安全的 `SECRET_KEY`

2. 使用環境變數而非硬編碼的敏感信息

3. 配置 HTTPS

4. 考慮使用 Nginx 作為反向代理

## 貢獻指南

1. Fork 此專案
2. 創建您的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 開啟一個 Pull Request

## 授權

此專案採用 MIT 授權 - 詳見 LICENSE 文件

## 系統畫面截圖

![image](https://github.com/user-attachments/assets/88bb2e11-3956-4bc3-b573-16b6d6b5caf2)

![image](https://github.com/user-attachments/assets/a974ad2d-d17a-418e-be1e-b9f7482b8391)

---

*注意：此 README 僅供參考，請根據您的實際專案情況進行調整和補充。*
