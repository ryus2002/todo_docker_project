# 使用 Python 3.9 作為基礎映像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# 設置環境變數
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 安裝系統依賴
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 安裝 Python 依賴
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 複製專案檔案
COPY . /app/

# 設置啟動命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
