#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
check_for_linked_files.py
Description of check_for_linked_files.py
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    attributes = ['fileName2',
                  'fileTextureName']
    for node in cmds.ls():
        for attr in attributes:
            if cmds.attributeQuery(attr, node=node, exists=True):
                attr_val = cmds.getAttr('{}.{}'.format(node, attr))
                print(attr_val + '\t|\t%s' % node)


if __name__ == '__main__':
    main()
