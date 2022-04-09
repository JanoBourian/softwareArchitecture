# Docker

## Docker hub 

https://hub.docker.com/

## Docker file

```
from node:10.13-alpine

RUN mkdir app
WORKDIR /app
COPY .  .
ENV PORT = 3000
RUN npm install
EXPOSE $PORT
CMD node app.js
```

## Commands
    - images
    - ps
    - ps -a

## Do Docker Desktop
    - docker images 
    - docker ps # Contenedores activos
    - docker ps -a # Todos los contenedores
    - docker pull hello-world # Download some image
    - docker run hello-world # Run image
    - docker start CONTAINER_ID # Started
    - docker stop CONTAINER_ID # Exited status
    - docker rm CONTAINER_ID # Deleted container
    - docker rmi IMAGE_ID # Deleted image

## Server instance
    - ssh root@public_ip
    - natural_process
    - sudo apt-get update

## Instalations 

https://docs.docker.com/engine/install/ubuntu/

## Aditionals resources

https://ascodecodigo.github.io/docker-fundamentals/

https://www.vultr.com/

