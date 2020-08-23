---
layout: post
title:  "Build and run an application in Docker"
author: sotf
categories: [ docker, backend ]
image: assets/images/whatisdocker/cover.png
beforetoc: "Multiple languages, frameworks, architectures, and discontinuous interfaces between tools for each lifecycle stage creates huge complexity. Docker simplifies and accelerates your workflow while giving developers the freedom to innovate with their choice of tools, application stacks, and deployment environments for each project."
toc: true
---

In this post, I will explain how to build and run an image in Docker by a tutorial provided by the original document of Docker.

## Prerequisite

To understand all the following steps and things that I say, you have to read all previous posts about Docker. Besides, you must ensure that you installed Docker successfully.

## Set up

First, let clone node-bulletin-board sample project:

```bash
git clone https://github.com/dockersamples/node-bulletin-board
cd node-bulletin-board/bulletin-board-app
```

See Dockerfile:

```Dockerfile
FROM node:current-slim

WORKDIR /usr/src/app
COPY package.json .
RUN npm install

EXPOSE 8080
CMD [ "npm", "start" ]

COPY .  .
```

This Dockerfile defines that it is base on node:current-slim. Then it set the working directory for the upcoming  CMD, RUN... instruction. The third command will run in the building process. This post will run in port 8080 of the container because of command EXPOSE 8080. When you run the container, the CMD instruction will run. Last instruction let the Docker daemon to copy all file in local to the working directory in Docker (/usr/src/app).

## Build the image

Make sure that you are in the correct directory which has the Docker file. Run the following command:

```bash
docker build --tag bulletinboard:1.0 .
```

You’ll see Docker step through each instruction in your Dockerfile, building up your image as it goes. If successful, the build process should end with a message Successfully tagged bulletinboard:1.0.

```bash
Successfully built 136c123b3d8c
Successfully tagged bulletinboard:1.0
```

## Run the image as a container

Run the following command:

```bash
sudo docker run --publish 8000:8080 --detach --name bb bulletinboard:1.0
```

There are a couple of common flags here:

* --publish: request Docker to forward traffic incoming on the host's port 8000 to port 8080 of the container. If your host's port is busy, the Docker will commit a message.
* -- detach: asks the Docker to run the container in the background
* --name specifies a name with which you can refer to your container in subsequent commands, in this case, it is bb

Finally, visit your localhost:8000/ to see the Bulletin Board app which is running in your Docker.

![alt text]({{base.url}}/assets/images/buildandrundocker/1.png)

If you can imagine how the app can work in Docker now, you can delete the container:

```bash
sudo docker stop bb
sudo docker rm bb
```

## Conclusion

You can figure out how to build the images, which contain your application and run it in Docker. There are many things beside but I think that you should work with Docker and find the solution for yourself by the original document of Docker.
