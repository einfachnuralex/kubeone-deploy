#!/usr/bin/env python3
#
import os
import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

if __name__ == '__main__':
    with open("kubeoneconfig.yaml", "wb") as fh:
        text = env.get_template('kubeoneconfig.yaml.j2').render(env=os.environ)
        fh.write(text.encode('utf-8'))
