#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds
import os
import os.path


def main():
    """docstring for main"""
    new_list = []
    texture_filename_list = []
    # Gets all 'file' nodes in maya
    fileList = cmds.ls(type='file')

    # For each file node..
    for f in fileList:
        # Get the name of the image attached to it
        texture_filename = cmds.getAttr(f + '.fileTextureName')
        texture_filename_list.append(texture_filename)

    for each in texture_filename_list:
        file_name = os.path.basename(each)
        new_list.append(file_name)
        print(file_name)


if __name__ == '__main__':
    main()
