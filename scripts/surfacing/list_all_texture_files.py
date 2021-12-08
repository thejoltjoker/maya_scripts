#!/usr/bin/env python
"""
list_all_texture_files.py
Description of list_all_texture_files.py.
"""
import os
import maya.cmds as cmds

from pprint import pprint


def main():
    """docstring for main"""
    files = []
    nodes = cmds.ls(type='file', long=True)
    for node in nodes:
        file = {
            'node': node,
            'path': cmds.getAttr(f'{node}.fileTextureName'),
            'filename': os.path.basename(cmds.getAttr(f'{node}.fileTextureName')),
            'color_space': cmds.getAttr(f'{node}.colorSpace'),
            'descendants': cmds.listRelatives(node, ad=True),
            'connected_to': list(dict.fromkeys(cmds.listConnections(node))),
            'parents': cmds.listRelatives(node, ap=True)
        }
        files.append(file)
    return files


# os.environ['TMPDIR'] = r'C:\temp'
if __name__ == '__main__':
    pprint(main())
