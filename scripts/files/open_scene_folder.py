#!/usr/bin/env python
"""
open_scene_folder.py

Open the folder of the currently open scene.
"""
import os
import subprocess
import sys

import maya.cmds as cmds


def main():
    cur_file = cmds.file(q=True, sn=True)
    cur_file_folder = os.path.dirname(cur_file)
    cmd = None
    if sys.platform == 'darwin':
        cmd = ['open', cur_file_folder]
    elif sys.platform == 'win32':
        cmd = 'start "{}"'.format(cur_file_folder)
    if cmd:
        subprocess.Popen(cmd)


if __name__ == '__main__':
    main()
