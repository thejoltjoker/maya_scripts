#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds
from pprint import pprint


def main():
    """docstring for main"""
    types = []
    for node in cmds.ls():
        types.append(str(cmds.nodeType(node)))
    return types


if __name__ == '__main__':
    pprint({x: x for x in main()})
