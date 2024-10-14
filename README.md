# doto

Dotfiles management with Python and Ansible

## Setup for development

```bash
source setup.sh
```

## Ansible

Running ansible playbook
```bash
cd ansible
ansible-galaxy install -r requirements.yml
ansible-playbook -i inventory main.yml
```

## Vagrant

## VirtualBox

```bash
VBoxManage list runningvms | cut -d '"' -f 2 | xargs -I {} VBoxManage controlvm {} poweroff soft && VBoxManage list vms | cut -d '"' -f 2 | xargs -I {} VBoxManage unregistervm {} --delete
```


## TODO

- 2024-02-22:
  - molecule test does not create a box, I have to run molecule converge first.
  - virtulabox got installed and was signed automatically, need to figure out why. dpkg package?
