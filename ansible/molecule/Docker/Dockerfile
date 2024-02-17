FROM geerlingguy/docker-ubuntu2204-ansible:latest

RUN apt-get update && apt-get install -y \
  curl \
  openssh-client \
  && apt-get autoremove -y && apt-get clean -y
