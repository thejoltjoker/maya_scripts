#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
change_attribute_multiple_nodes.py
Description of change_attribute_multiple_nodes.py.
"""
import maya.cmds as cmds
from maya import OpenMayaUI as omui
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QSizePolicy
from shiboken2 import wrapInstance

class PastebinWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PastebinWindow, self).__init__(parent)
        # self.setParent(mayaMainWindow)

        # Set window properties
        self.setWindowTitle('Pastebin')
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumSize(250, 200)

        font = QtGui.QFont("Jetbrains Mono")
        font.setStyleHint(QtGui.QFont.Monospace)
        self.setFont(font)

        # Create button widgets
        self.label_path = QtWidgets.QLabel(CACHE_FOLDER_PATH)
        self.label_path.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_path.setStyleSheet(
            'color: #48cae4;'
            'text-decoration: underline;'
            'cursor: pointer;'
            'font-family: Jetbrains Mono, monospace;')
        self.label_path.mousePressEvent = open_folder

        self.btn_copy = QtWidgets.QPushButton('Copy')
        self.btn_copy.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.btn_paste = QtWidgets.QPushButton('Paste')
        self.btn_paste.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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


def set_attr():
    """docstring for main"""
    sel = cmds.ls(sl=True)

    attribute = 'refr_weight'
    value = 0
    # shape = cmds.listRelatives(sel[1], shapes=True)[0]

    for node in sel:
        if cmds.attributeQuery(attribute, node=node, ex=True):
            node_attr = '.'.join([node, attribute])
            cmds.setAttr(node_attr, value)

            print("{attr} was set to {val}".format(attr=node_attr, val=value))


def main():
    # mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    # mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    # ui = PastebinWindow(mayaMainWindow)
    # ui.show()
    # return ui
    set_attr()


if __name__ == '__main__':
    set_attr()
