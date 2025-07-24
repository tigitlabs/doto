FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
  && apt-get -y install --no-install-recommends \
  bash-completion \
  git \
  git-lfs \
  tmux \
  vim \
  python3 \
  python3-pip \
  python3-apt \
  pipx \
  # Clean up
  && apt-get autoremove -y && apt-get clean -y

# Install Poetry and pip packages
USER vscode
RUN pipx install \
  poetry \
  && pipx ensurepath
ENV POETRY_HOME=/home/vscode/.local/bin
ENV POETRY_VIRTUALENVS_OPTIONS_SYSTEM_SITE_PACKAGES=true
ENV PATH="${PATH}:${POETRY_HOME}"

WORKDIR  /workspaces/doto/
COPY pyproject.toml poetry.lock .
RUN poetry install --no-root --no-interaction
