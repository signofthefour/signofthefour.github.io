---
layout: post
title:  "What is DOCKER?"
author: sotf
categories: [ docker, backend ]
image: assets/images/whatisdocker/cover.png
beforetoc: "Multiple languages, frameworks, architectures, and discontinuous interfaces between tools for each lifecycle stage creates huge complexity. Docker simplifies and accelerates your workflow while giving developers the freedom to innovate with their choice of tools, application stacks, and deployment environments for each project."
toc: true
---

Imagine that one day you are working on your python project with many packages, modules that were already installed. You share this project with your partner without any loss of a line in code. But, when your friend runs it, there are some troubles: the result has slightly different, and sometimes the code does not work.
![alt text]({{base.url}}/assets/images/whatisdocker/1.png "https://juststickers.in/wp-content/uploads/2018/01/works-on-my-machine-border.png")
**The Docker can solve it and many others**

## What is Docker

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.

* [Docker original website](https://www.docker.com/)
* [Docker original document](https://docs.docker.com/develop/)

In this post, I will try to combine all definitions about docker and explain how docker makes your deployment process be better.

## Docker Platform

Docker provides the ability to package and run an application in a loosely isolated environment called a container. The isolation and security allow you to run many containers simultaneously on a given host. Containers are lightweight because they don’t need the extra load of a hypervisor, but run directly within the host machine’s kernel. This means you can run more containers on a given hardware combination than if you were using virtual machines. You can even run Docker containers within host machines that are actually virtual machines!

Docker provides tooling and a platform to manage the lifecycle of your containers:

* Develop your application and its supporting components using containers.
* The container becomes the unit for distributing and testing your application.
* When you’re ready, deploy your application into your production environment, as a container or an orchestrated service. This works the same whether your production environment is a local data center, a cloud provider, or a hybrid of the two.

## Docker Engine

Docker Engine is a client-server application with these major components:

* A server which is a type of long-running program called a daemon process (the dockerd command).
* A REST API which specifies interfaces that programs can use to talk to the daemon and instruct it what to do.
* A command line interface (CLI) client (the docker command).

![alt text](https://docs.docker.com/engine/images/engine-components-flow.png "Engine Components flow")

## Docker architecture

Docker uses a client-server architecture where **Docker client** talks to **Docker daemon**, which does a heavy lifting of building, running, and distributing your **Docker containers**. The Docker client and daemon can run on the same system, or you can connect a docker to a remote Docker daemon. The Docker client and daemon communicate using a REST API, over UNIX sockets, or a network interface.

![alt text](https://docs.docker.com/engine/images/architecture.svg "Docker architecture")

## The Docker client

The Docker client (docker) is the primary way that many Docker users interact with Docker. When you use commands such as docker run, the client sends these commands to dockerd, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon.

## Docker registries

A Docker registry stores Docker images. Docker Hub is a public registry that anyone can use, and Docker is configured to look for images on Docker Hub by default. You can even run your own private registry.

When you use the docker pull or docker run commands, the required images are pulled from your configured registry. When you use the docker push command, your image is pushed to your configured registry.

## Docker object

When you use Docker, you are creating and using images, containers, networks, volumes, plugins, and other objects. This section is a brief overview of some of those objects.

## IMAGES

An image is a read-only template with instructions for creating a Docker container. Often, an image is based on another image, with some additional customization. For example, you may build an image which is based on the ubuntu image, but installs the Apache web server and your application, as well as the configuration details needed to make your application run.

You might create your own images or you might only use those created by others and published in a registry. To build your own image, you create a Dockerfile with a simple syntax for defining the steps needed to create the image and run it. Each instruction in a Dockerfile creates a layer in the image. When you change the Dockerfile and rebuild the image, only those layers which have changed are rebuilt. This is part of what makes images so lightweight, small, and fast, when compared to other virtualization technologies.

I will talk about some general images in another post.

## CONTAINER

A container is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI. You can connect a container to one or more networks, attach storage to it, or even create a new image based on its current state.

By default, a container is relatively well isolated from other containers and its host machine. You can control how isolated a container’s network, storage, or other underlying subsystems are from other containers or from the host machine.

A container is defined by its image as well as any configuration options you provide to it when you create or start it. When a container is removed, any changes to its state that are not stored in persistent storage disappear.

Example docker run command

```bash
docker exec -it container /bin/bash
```

This command runs an ubuntu container, attaches interactively to your local command-line session, and runs /bin/bash.

## Refference

* [Docker Overview](https://docs.docker.com/get-started/overview/)
* [Docker engine](https://docs.docker.com/engine/)
