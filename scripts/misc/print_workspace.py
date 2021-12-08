#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds
def main():
    """docstring for main"""
    rules = cmds.workspace(fileRule=True, q=True)
    for n in range(len(rules)):
        if n % 2 == 0:
            print(rules[n] + ': ' + rules[n+1])


if __name__ == '__main__':
    main()