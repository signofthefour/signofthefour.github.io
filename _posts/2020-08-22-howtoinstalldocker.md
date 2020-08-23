---
layout: post
title:  "How to Install Docker"
author: sotf
categories: [ docker, backend ]
image: assets/images/whatisdocker/cover.png
beforetoc: "Multiple languages, frameworks, architectures, and discontinuous interfaces between tools for each lifecycle stage creates huge complexity. Docker simplifies and accelerates your workflow while giving developers the freedom to innovate with their choice of tools, application stacks, and deployment environments for each project."
toc: true
---

In this post, I will cover how to install Docker. You need to read the [previous post](https://signofthefour.github.io/whatisdocker/) in order to be clear with all the needed definitions for today's post.

First of all, containers are part of the Linux ecosystem, not Windows. Linux is a better OS than Windows, its architecture, especially the Kernel and file system is much better than Windows. Containers take advantage of the process isolation in Linux alongside the namespaces to create isolated processes. So I recommend you to install and use Docker in Linux. Here, I will introduce Docker's installation step by step.

***Prerequisite:*** Docker Engine is supported on x86_64 (or amd64),  armhf, and arm64 architectures.

## Uninstall old version of Docker in the current OS

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

## Setup the repository

Update the apt package index and install packages to allow apt to use a repository over HTTPS:

```bash
sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```

## Add Docker’s official GPG key

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Check if your computer recognizes the repository of Docker

```bash
sudo apt-key fingerprint 0EBFCD88
```

The result should be:

```bash
pub   rsa4096 2017-02-22 [SCEA]
      9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid           [ unknown] Docker Release (CE deb) <docker@docker.com>
sub   rsa4096 2017-02-22 [S]
```

## Setup stable reposity

Use the following command to set up the stable repository. To add the nightly or test repository, add the word nightly or test (or both) after the word stable in the commands below.

```bash
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

## Install Docker engine

Update the apt package index, and install the latest version of Docker Engine and containerd, or go to the next step to install a specific version:

```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

List all version available in your repo:

```bash
apt-cache madison docker-ce

docker-ce | 5:19.03.12~3-0~ubuntu-focal | https://download.docker.com/linux/ubuntu focal/stable amd64 Packages
docker-ce | 5:19.03.11~3-0~ubuntu-focal | https://download.docker.com/linux/ubuntu focal/stable amd64 Packages
docker-ce | 5:19.03.10~3-0~ubuntu-focal | https://download.docker.com/linux/ubuntu focal/stable amd64 Packages
docker-ce | 5:19.03.9~3-0~ubuntu-focal | https://download.docker.com/linux/ubuntu focal/stable amd64 Packages
```

To install the specific version:

```bash
sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
```

For example:

```bash
sudo apt-get install docker-ce=5:19.03.12~3-0~ubuntu-focal docker-ce-cli=5:19.03.12~3-0~ubuntu-focal containerd.io
```

Wait for install completion, the check if your docker is installed successfully:

```bash
sudo docker run hello-world
```

This is the result in my computer:

```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

Go to next post for deployment of an app in Docker.
