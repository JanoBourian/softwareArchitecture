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

## Aditionals resources

https://ascodecodigo.github.io/docker-fundamentals/

https://www.vultr.com/

