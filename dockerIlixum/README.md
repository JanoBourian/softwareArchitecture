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

## Some instalations
    - docker pull postgres
    or
    - docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
    - docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
    - docker run --name postgresqa -p 5433:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres

## Mariadb
    - docker pull mariadb
    - docker run --detach --name some-mariadb -p 3306:3306 --env MARIADB_USER=username --env MARIADB_PASSWORD=password --env MARIADB_ROOT_PASSWORD=password  mariadb:latest

## Mongo
    - docker pull mongo
    - docker run --name some-mongo -p 27017:27017 -d mongo:tag

## DockerIMG
    - docker build -t healt . 
    - docker run -d --name healt -p 3001:3001 healt
    - docker run --restart=always -dti --name "resthellowworld" -p 3001:3001 --env="PORT=3001" resthellowworld:1.0
    - docker logs CONTAINER_ID

## Server instance
    - ssh root@public_ip
    - natural_process
    - sudo apt-get update

## Server conection
    - ssh-keygen -t rsa (/root/.ssh/id_rsa)
    - /home/ubuntu#
    - cd .ssh
    - type or cat id_rsa.pub
    - go to github
    - To add public key
    - curl https://localhost:3001/hello

## Make Volume
```
docker run -d \
	--name dbvolumen \
	-e POSTGRES_PASSWORD=mysecretpassword \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v /custom/mount:/var/lib/postgresql/data \
	-p 5432:5432 \
	postgres
```

```
docker run -d --name dbvolumen -e POSTGRES_PASSWORD=mysecretpassword -e PGDATA=/var/lib/postgresql/data/pgdata -v C:\Users\super\Documents\dockerVolumen:/var/lib/postgresql/data -p 5432:5432 postgres
```

## up.sh file

```
docker rm -f resthellowworld
docker rmi resthellowworld
docker build -t "resthellowworld:1.0" .
docker run -dti --name "resthellowworld" -p 3001:3001 --env="PORT=3001" resthellowworld:1.0
docker run --restart=always -d --name "resthellowworld" -p 3001:3001 --env="PORT=3001" resthellowworld:1.0
``` 

## Amazon Web Services
    - To create AWS instances
    - Set up Docker in the new instances
        - https://docs.docker.com/engine/install/ubuntu/
    - 

## Github Actions
    - https://medium.com/intelligentmachines/github-actions-basics-40a4d9b417f8
    - Secrets in the project

## Instalations 

https://github.com/comodorop/holaMundoRestNode

https://robomongo.org/

https://docs.docker.com/engine/install/ubuntu/

https://dbeaver.io/

## Aditionals resources

https://ascodecodigo.github.io/docker-fundamentals/

https://www.vultr.com/

