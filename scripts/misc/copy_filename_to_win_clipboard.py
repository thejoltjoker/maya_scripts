#!/usr/bin/env python
"""
copy_filename_to_win_clipboard.py
Description of copy_filename_to_win_clipboard.py.
"""
import maya.cmds as cmds
import os

def copy_folder():
    """docstring for copy_folder"""

    cur_file = cmds.file(q=True, sn=True)
    cur_file_folder = os.path.dirname(cur_file)

    command = 'echo ' + cur_file_folder.strip() + '| clip'
    os.system(command)

def copy_filename():
    """docstring for copy_filename"""

    cur_file = cmds.file(q=True, sn=True)

    command = 'echo ' + cur_file.strip() + '| clip'
    os.system(command)
