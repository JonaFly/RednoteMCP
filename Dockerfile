FROM python:3.9-slim

WORKDIR /app

# 安装系统依赖和浏览器
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libwayland-client0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 复制需要的文件
COPY requirements.txt .
COPY xiaohongshu_mcp.py .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 安装Playwright浏览器
RUN playwright install chromium

# 创建必要的目录
RUN mkdir -p browser_data data

# 暴露端口（FastMCP默认端口为8000）
EXPOSE 8000

# 运行应用
CMD ["python", "xiaohongshu_mcp.py"] 