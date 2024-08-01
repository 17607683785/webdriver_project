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

# 启动应用程序
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:10000", "app:app"]
