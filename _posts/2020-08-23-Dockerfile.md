---
layout: post
title:  "How to write a Dockerfile"
author: sotf
categories: [ docker, backend ]
image: assets/images/whatisdocker/cover.png
beforetoc: "Multiple languages, frameworks, architectures, and discontinuous interfaces between tools for each lifecycle stage creates huge complexity. Docker simplifies and accelerates your workflow while giving developers the freedom to innovate with their choice of tools, application stacks, and deployment environments for each project."
toc: true
---

## Dockerfile

With each separate app, in addition to the code, there are many things attached: Execution environment, libraries, packages ... Thus, for the app to always be able to execute at its best, the accompanying things are indispensable... So when building an image, we need to show the Docker API what extra this app needs. Dockerfile is a document instructing Docker to do that.
For more information:
[Docker file reference](https://docs.docker.com/engine/reference/builder/)

Docker builds an image based on Dockerfile and context. The context here is PATH (to the project) or URL (to git repo). The Docker build process is run by the Docker daemon. The first thing a build process does is send the entire context of the working directory. So, you should avoid using the root directory because it can send the content of your hard drive to Docker daemon (lower and bigger).

To use a file in the build context, the Dockerfile refers to the file specified in the instruction, for example, a COPY instruction. To increase the build’s performance, exclude files and directories by adding a .dockerignore file (It is like the .gitignore file in git) to the context directory. For information about how to create a .dockerignore file see the documentation.

Traditionally, the Dockerfile is called Dockerfile and is located at the root of the context. You use the -f flag with docker build to point to a Dockerfile anywhere in your file system.

```bash
docker build -f /path/to/a/Dockerfile .
```

We can specify that the repo will store this new image if it is successfully built.

```bash
docker build -t sotf/myapp .
```

To build the image, Docker will run each line in Dockerfile step-by-step, commit the result if necessary, and finally return the ID of the image

Note that each instruction is run independently, and causes a new image to be created - so RUN cd /home will not have any effect on the next instructions.

## Some instruction in a Dockerfile

* **FROM** - The base image for building a new image. This instruction must be the first non-comment instruction in the Dockerfile. The only exception from this rule is when you want to use a variable in the FROM argument. In this case, FROM can be preceded by one or more ARG instructions.

```Dockerfile
FROM [--platform=<platform>] <image> [AS <name>]
FROM [--platform=<platform>] <image>[:<tag>] [AS <name>]
FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]
```

* **ARG** - This instruction allows you to define variables that can be passed at build-time. You can also set a default value.

```Dockerfile
ARG  CODE_VERSION=latest
FROM base:${CODE_VERSION}
CMD  /code/run-app

FROM extras:${CODE_VERSION}
CMD  /code/run-extras
```

* **LABEL** - Used to add metadata to an image, such as description, version, author ..etc. You can specify more than one LABEL, and each LABEL instruction is a key-value pair.

```Dockerfile
LABEL <key>=<value> <key>=<value> <key>=<value> ...
```

For example:

```Dockerfile
LABEL "com.example.vendor"="ACME Incorporated"
LABEL com.example.label-with-value="foo"
LABEL version="1.0"
LABEL description="This text illustrates \
that label-values can span multiple lines."
```

* **RUN** - The commands specified in this instruction will be executed during the build process. Each RUN instruction creates a new layer on top of the current image.

```Dockerfile
RUN /bin/bash -c 'source $HOME/.bashrc; echo $HOME'
```

In case you do not ensure that your image has /bin/bash as the default command line:

```Dockerfile
RUN ["/bin/bash", "-c", "echo hello"]
```

* **ADD** - Used to copy files and directories from the specified source to the specified destination on the docker image. The source can be local files or directories or an URL. If the source is a local tar archive, then it is automatically unpacked into the Docker image.

```Dockerfile
ADD [--chown=<user>:<group>] <src>... <dest>
ADD [--chown=<user>:<group>] ["<src>",... "<dest>"]

ADD *.class /mydir/
```

* **COPY** - Similar to ADD but the source can be only a local file or directory.

```Dockerfile
COPY [--chown=<user>:<group>] <src>... <dest>
COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]

COPY *.py /mydir/
```

* **ENV** - This instruction allows you to define an environment variable.

```Dockerfile
ENV <key> <value>
ENV <key>=<value> ...

ENV myName="John Doe" myDog=Rex\ The\ Dog
```

* **CMD** - Used to specify a command that will be executed when you run a container. You can use **only one** CMD instruction in your Dockerfile.

```Dockerfile
CMD ["executable", "param1", "param2"]
# exec form, this is the preferred form)

CMD ["param1","param2"]
# as default parameters to ENTRYPOINT

CMD command param1 param2
# shell form
```

```Dockerfile
FROM ubuntu
CMD echo "This is a test." | wc -
```

* **ENTRYPOINT** - Similar to CMD, this instruction defines what command will be executed when running a container.

The table below shows what command is executed for different ENTRYPOINT / CMD combinations:
Both CMD and ENTRYPOINT instructions define what command gets executed when running a container. There are a few rules that describe their co-operation.

1. Dockerfile should specify at least one of CMD or ENTRYPOINT commands.

2. ENTRYPOINT should be defined when using the container as an executable.

3. CMD should be used as a way of defining default arguments for an ENTRYPOINT command or for executing an ad-hoc command in a container.

4. CMD will be overridden when running the container with alternative arguments.

The table below shows what command is executed for different ENTRYPOINT / CMD combinations:

||No ENTRYPOINT|ENTRYPOINT exec_entry p1_entry|ENTRYPOINT [“exec_entry”, “p1_entry”]|
|---|---|---|---|
|No CMD|error, not allowed|/bin/sh -c exec_entry p1_entry|exec_entry p1_entry|
| CMD [“exec_cmd”, “p1_cmd”]  | exec_cmd p1_cmd  |  /bin/sh -c exec_entry p1_entry | exec_entry p1_entry exec_cmd p1_cmd  |
| CMD [“p1_cmd”, “p2_cmd”]  | p1_cmd p2_cmd  |  /bin/sh -c exec_entry p1_entry |  exec_entry p1_entry p1_cmd p2_cmd |
| CMD exec_cmd p1_cmd  |  /bin/sh -c exec_cmd p1_cmd |  /bin/sh -c exec_entry p1_entry |  exec_entry p1_entry /bin/sh -c exec_cmd p1_cmd |

* **WORKDIR** - This directive sets the current working directory for the RUN, CMD, ENTRYPOINT, COPY, and ADD instructions. (The directory is on Docker image)

```Dockerfile
WORKDIR /path/to/workdir
```

```Dockerfile
WORKDIR /a
RUN pwd
```

* **USER** - Set the username or UID to use when running any following RUN, CMD, ENTRYPOINT, COPY, and ADD instructions.

```Dockerfile
USER <user>[:<group>]
USER <UID>[:<GID>]
```

```Dockerfile
FROM microsoft/windowsservercore
# Create Windows user in the container
RUN net user /add sotf
# Set it for subsequent commands
USER sotf
```

* **VOLUME** - Enables you to mount a host machine directory to the container.

```Dockerfile
VOLUME ["/data"]
```

```Dockerfile
FROM ubuntu
RUN mkdir /myvol
RUN echo "hello world" > /myvol/greeting
VOLUME /myvol
```

* **EXPOSE** - Used to specify the port on which the container listens at runtime.

```Dockerfile
EXPOSE <port> [<port>/<protocol>...]

EXPOSE 80
EXPOSE 80/udp
```

## Format of Dockerfile

As mentioned above, the Docker daemon will run each line in Dockerfile, so every line in Dockerfile must follow some rules that ensure Docker daemon can execute.

```Dockerfile
# Comment
INSTRUCTION arguments
```

Instruction of Dockerfile is not case-sensitive. However, conventional, the instruction should be UPPERCASE to distinguish with the args.
[Check all the definition](https://docs.docker.com/glossary/)

Docker runs instructions in a Dockerfile in order. A Dockerfile must begin with a FROM instruction. This may be after parser directives, comments, and globally scoped ARGs. The FROM instruction specifies the Parent Image from which you are building. FROM may only be preceded by one or more ARG instructions, which declare arguments that are used in FROM lines in the Dockerfile.

```Dockerfile
FROM ubuntu:18.04
```

Docker treats lines that begin with # as a comment unless the line is a valid parser directive. A # marker anywhere else in a line is treated as an argument. This allows statements like:

```Dockerfile
# Comment
RUN echo 'we are running some # of cool things'
```

## Conclusion

Now, you can write a Dockerfile for yourself with all the above knowlegde. Go to the next post for how to build and run an image.
