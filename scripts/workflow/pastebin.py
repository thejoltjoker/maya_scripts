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
        subprocess.call(["open", "-R", CACHE_FOLDER_PATH])


import maya.cmds as cmds
from PySide2 import QtCore, QtGui, QtWidgets


class PastebinWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(PastebinWindow, self).__init__(parent)

        # Set window properties
        self.setWindowTitle('Pastebin')
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTitleHint)
        self.setMinimumSize(250, 100)

        # Create button widgets
        self.label_path = QtWidgets.QLabel(CACHE_FOLDER_PATH)
        self.label_path.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_path.setStyleSheet('color: #48cae4; text-decoration: underline')
        # self.label_path.setOpenExternalLinks(False)
        # self.label_path.linkActivated.connect(open_folder)
        self.label_path.mousePressEvent = open_folder

        self.btn_copy = QtWidgets.QPushButton('Copy')
        self.btn_paste = QtWidgets.QPushButton('Paste')
        self.btn_open = QtWidgets.QPushButton('Open cache folder')

        # Create button layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.btn_copy)
        button_layout.addWidget(self.btn_paste)

        # Main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.btn_open)
        main_layout.addWidget(QtWidgets.QLabel('Cache folder:'))
        main_layout.addWidget(self.label_path)
        self.setLayout(main_layout)

        # Connect button signals to slots
        self.btn_copy.clicked.connect(copy)
        self.btn_paste.clicked.connect(paste)
        self.btn_open.clicked.connect(open_folder)


def main():
    # Create and show the popup dialog
    popup = PastebinWindow()
    popup.exec_()


if __name__ == '__main__':
    main()
