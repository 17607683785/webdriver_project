# 使用官方的 Python 镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . .

# 安装项目依赖
RUN pip install -r requirements.txt

# 暴露端口
EXPOSE 4444

# 运行应用
CMD ["python", "app.py"]
