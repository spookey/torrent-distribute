# -.- coding: utf-8 -.-

from os import path
from json import dumps, loads

configfile = path.join(path.abspath(path.dirname(__file__)), 'config.json')

def write_file(filename, content):
    with open(filename, 'w') as f:
        try:
            f.write(content)
        except Exception as ex:
            print('warning: could not write file %s: %s' %(filename, ex))

def write_json(filename, content):
    try:
        write_file(filename, dumps(content, indent=2))
    except Exception as ex:
        print('warning: could not write json file %: %s' %(filename, ex))

def read_file(filename):
    if path.exists(filename):
        with open(filename, 'r') as f:
            try:
                return f.read()
            except Exception as ex:
                print('warning: could not read file %s: %s' %(filename, ex))
    else:
        print('Error: file %s does not exist' %(filename))

def read_json(filename):
    try:
        return loads(read_file(filename))
    except Exception as ex:
        print('warning: could not read json file %s: %s' %(filename, ex))
