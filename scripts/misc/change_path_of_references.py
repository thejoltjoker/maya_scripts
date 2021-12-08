#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
change_path_of_references.py
Change the file path to the references in a scene
"""
import maya.cmds as cmds


def main():
    """docstring for main"""

    reference_nodes = cmds.ls(references=True)
    search_for = '/Volumes/macpath'
    replace_with = 'P:'

    for node in reference_nodes:
        id_exists = cmds.attributeQuery('fileNames', node=node, exists=True)
        if id_exists:
            print(cmds.getAttr(node + '.fileNames'))


if __name__ == '__main__':
    main()
