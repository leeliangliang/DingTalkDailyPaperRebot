# 使用官方 Python 镜像作为基础
FROM python:3.10.11

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器的 /app 目录下
COPY . /app

# 安装所需的依赖
RUN pip install --no-cache-dir -r requirements.txt

# 运行 Python 脚本
CMD [ "python", "app.py" ]
