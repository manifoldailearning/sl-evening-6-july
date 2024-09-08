# Docker Installation

https://docs.docker.com/desktop/

# Commands on Hands On

```
docker --version
docker run hello-world
docker pull busybox
docker images
docker run busybox
docker run busybox echo "hello from busybox learning"
docker ps
docker ps -a
docker run -it busybox sh
docker rm <container_id>
```
# 1.1 Docker installation commands in EC2

```
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo systemctl start docker
sudo service docker status
sudo groupadd docker
sudo usermod -a -G docker ec2-user
newgrp docker
docker —-version
```

# 2. Hands On


```
docker build -t manifoldailearning/nginxdemo .


docker run -d -P --name catgif manifoldailearning/catgif
docker ps
docker port catgif
docker stop catgif
docker run -p 8888:5000 manifoldailearning/catgif
docker build -t catgifv2 .
docker run -p 8888:5000 catgifv2
docker login
docker build -t yourusername/catgif .
docker push yourusername/catgif
```
