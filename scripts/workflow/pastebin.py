#!/usr/bin/env python
"""
Pastebin

Credits to Martin Gunnarson for the great idea.
"""
import sys
import os
import time
import re
import subprocess
import tempfile
import maya.cmds as cmds
import maya.OpenMaya as om
from sys import platform as system_os

PRINT_PREFIX = '[pastebin] '
CACHE_FOLDER_NAME = 'pastebin'
CACHE_FOLDER_PATH = os.path.join(tempfile.gettempdir(), CACHE_FOLDER_NAME)


def copy(*args, **kwargs):
    """Copy selected object(s)"""

    # Set default file type and extension
    file_ext = '.mb'
    file_type = 'mayaBinary'

    # Get current file type and adjust accordingly
    current_file_type = cmds.file(q=True, type=True)
    current_file_name = cmds.file(q=True, sn=True)
    if current_file_type[0] != file_type:
        file_ext = os.path.splitext(current_file_name)[1]
        file_type = current_file_type[0]

    # Get selection
    sel = cmds.ls(sl=True)

    if sel:
        # Get current date
        cur_date = time.strftime("%y%m%d%H%M%S")

        # Get first selected object name
        obj_name = sel[0]

        # Create alphanumeric name without underscores
        obj_name_alpha_sub = re.sub(r'\W+', '_', obj_name)
        obj_name_alpha = obj_name_alpha_sub.replace('_', '')

        filename = '_'.join([cur_date, obj_name_alpha]) + file_ext

        thumb_filename = '_'.join([cur_date, obj_name_alpha, 'thumb']) + '.png'

        cache_file = os.path.join(CACHE_FOLDER_PATH, filename)
        cache_file_thumb = os.path.join(CACHE_FOLDER_PATH, thumb_filename)

        # Export objects
        cmds.file(cache_file, type=file_type, es=True)
        print
        PRINT_PREFIX + 'Selected objects exported to ' + cache_file

        # Generating a preview
        cur_frame = cmds.currentTime(query=True)
        # model_panel = cmds.paneLayout('viewPanes', q=True, pane1=True)
        # print model_panel
        # cmds.isolateSelect(model_panel, state=1)
        cmds.playblast(fr=cur_frame, fmt='image', compression='png',
                       cf=cache_file_thumb, orn=False, v=False)
        # cmds.isolateSelect(model_panel, state=0)

        if len(sel) > 1:
            font_color = '#0cf'
            message = 'Copied'
            cmds.inViewMessage(smg='<font color={}>{}</font>'.format(font_color,
                                                                     message), bkc=0x00262626, pos='topRight',
                               fade=True, a=0.5)
            om.MGlobal.displayInfo('Objects copied to {}'.format(cache_file))
        else:
            cmds.warning(obj_name + ' copied to ' + cache_file)

    else:
        cmds.warning('Nothing is selected.')


def paste(*args, **kwargs):
    """Paste latest copy"""

    # List all non png files in cache folder
    cached_files = []
    for filename in os.listdir(CACHE_FOLDER_PATH):
        if not filename.endswith('.png'):
            cached_files.append(os.path.join(CACHE_FOLDER_PATH, filename))

    # Sort newest first and get latest file
    cached_files.sort(reverse=True)
    latest_copy = cached_files[0]

    # Import file
    cmds.file(latest_copy, i=True, renameAll=False,
              returnNewNodes=True, options="v=0;")

    font_color = '#0cf'
    message = 'Pasted'
    cmds.inViewMessage(smg='<font color={}>{}</font>'.format(font_color,
                                                             message), bkc=0x00262626, pos='topRight', fade=True, a=0.5)
    om.MGlobal.displayInfo('Pasted object(s) from {}'.format(latest_copy))


def thumbnail():
    """Create a thumbnail from the viewport"""
    cur_frame = cmds.currentTime(query=True)
    model_panel = cmds.paneLayout('viewPanes', q=True, pane1=True)
    print
    model_panel
    cmds.isolateSelect(model_panel, state=1)
    cmds.playblast(fr=cur_frame, fmt='image', compression='png',
                   cf=cache_file_thumb, orn=False, v=False)
    cmds.isolateSelect(model_panel, state=0)


def open_folder(*args, **kwargs):
    if system_os == "win32":
        subprocess.Popen(r'explorer "' + CACHE_FOLDER_PATH + '"')
    elif system_os == "darwin":
        cache_path_slash = CACHE_FOLDER_PATH.replace('\\', '/')
        mac_cache_path = CACHE_FOLDER_PATH.replace('//SEQ-LIVE', '/volumes')
        subprocess.call(["open", "-R", mac_cache_path])


def window():
    window_name = "Pastebin"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)
    cmds.window(window_name, title="Pastebin")
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(CACHE_FOLDER_PATH)
    cmds.button(label="Copy", command=copy)
    cmds.button(label="Paste", command=paste)
    cmds.button(label="Open cache folder", command=open_folder)
    cmds.showWindow()


def main():
    window()


if __name__ == '__main__':
    main()
