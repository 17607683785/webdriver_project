FROM python:3.8-slim

# 安装依赖
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 复制应用程序代码
COPY . .

# 暴露端口
EXPOSE 10000

# 启动应用程序
CMD ["python", "app.py"]
