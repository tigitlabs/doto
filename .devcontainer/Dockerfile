# Note: You can use any Debian/Ubuntu based image you want. 
FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
  && apt-get -y install --no-install-recommends \
  bash-completion \
  tmux \
  vim \
  python3 \
  python3-pip \
  python3-venv \
  # Clean up
  && apt-get autoremove -y && apt-get clean -y

# Install Python packages
RUN python3 -m pip install --upgrade pip && pip3 install --no-cache-dir \
  docker \
  black \
  flake8 \
  isort \
  mypy \
  pipenv \
  pytest \
  pytest-cov \
  pytest-mock \
  wheel \
  ansible \
  ansible-lint \
  yamllint \
  molecule \
  molecule-plugins[docker]
