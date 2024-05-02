# Python_Devops

1. create a Python Virtual Environment `python3 -m venv /.venv` or `virtualenv ~/.venv`
2. pull this environment into our configurations
    `vim ~/.bashrc`
    add the below lines
    # sourcing python virtual environment
    `source ~/.venv/bin/activate`
    files will be saved in the below location
    `which python`
    `/home/codespace/.venv/bin/python`
    # commands
    touch requirements.txt
    touch Dockerfile
    touch Makefile
    mkdir mylib
    touch mylib/__init__.py
    touch mylib/logic.py
    touch main.py 

