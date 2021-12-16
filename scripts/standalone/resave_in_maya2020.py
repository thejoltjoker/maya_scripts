#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import sys
import os
import subprocess


def main(path):
    """docstring for main"""
    import maya.standalone
    import maya.cmds as cmds
    new_name = os.path.join(os.path.dirname(path), '_' + str(os.path.basename(path)))

    maya.standalone.initialize(name='python')
    cmds.file(path, o=True)
    cmds.file(rename=new_name)
    cmds.file(save=True, force=True, type='mayaAscii')


if __name__ == '__main__':
    main(sys.argv[1])
