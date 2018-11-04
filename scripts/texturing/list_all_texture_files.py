#!/usr/bin/env python
"""
list_all_texture_files.py
Description of list_all_texture_files.py.
"""
import os
import maya.cmds as cmds


def main():
    """docstring for main"""
    textures = [
        cmds.getAttr('%s.fileTextureName' % x) for x in cmds.ls(type='file')
    ]

    for texture in textures:
        path, file_name = os.path.split(texture)
        print path
        print file_name


if __name__ == '__main__':
    main()
