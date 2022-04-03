
# 说明

1. **如何启动该容器**

	- 安装docker，进入到含有`Dockerfile`, `setup.sh`, `worker.sh`三个文件的目录下。
	- 构建image: `docker build -t="worker:v2" ./`
	- 构建container: `docker run --privileged=true --name anyname -it worker:v2`


