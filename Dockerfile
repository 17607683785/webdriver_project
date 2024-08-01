FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装依赖
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 复制应用程序代码
COPY . .

# 暴露端口
EXPOSE 10000

# 设置环境变量供 Render 识别
ENV PORT=10000

# 启动应用程序
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:$PORT", "app:app"]

