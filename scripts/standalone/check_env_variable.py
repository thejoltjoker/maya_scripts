#!/usr/bin/env python3
"""check_env_variable.py
Description of check_env_variable.py.
"""
import platform
import sys
import os
from pprint import pprint

from maya import standalone, cmds


def write_to_file(path, data):
    with open(path, 'a') as txt_file:
        txt_file.write(data + '\n')


def main():
    """docstring for main"""
    text_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'hosts.txt'))
    standalone.initialize(name='python')

    write_to_file(text_file, platform.node())
    write_to_file(text_file, 'ACTIVE_LIBRARY_PATH: ' + os.getenv('ACTIVE_LIBRARY_PATH'))
    write_to_file(text_file, '\n')


if __name__ == '__main__':
    main()
