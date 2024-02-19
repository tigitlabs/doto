# doto
Dotfiles management with Python and Ansible

## Setup for development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ansible

### Creating a new role

```bash
ansible-galaxy role init <role_name>
cd <role_name>
molecule init scenario
```

## TODO
[ ] Add roles from github: 
    https://blog.ruanbekker.com/blog/2022/04/19/publish-and-use-your-ansible-role-from-git/