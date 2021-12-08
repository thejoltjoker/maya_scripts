#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import sys
import shiboken2
import maya.cmds as cmds
import maya.OpenMayaUI as mui
from PySide2 import QtWidgets
from PySide2.QtWidgets import QFormLayout


class Window(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        # self.mainLayout = QFormLayout()
        self.table = QtWidgets.QTableWidget(1, 3)
        self.columnLabels = ["Make", "Model", "Price"]
        self.table.setHorizontalHeaderLabels(self.columnLabels)
        self.setCentralWidget(self.table)
        self.setGeometry(50, 50, 700, 400)
        self.setWindowTitle("My GUI Program")


def get_maya_window():
    """Get maya main window"""
    ptr = mui.MQtUtil.mainWindow()
    maya_window = shiboken2.wrapInstance(int(ptr), QtWidgets.QWidget)

    return maya_window


def show():
    win = Window(parent=get_maya_window())
    win.show()
    win.raise_()
    return win


if __name__ == '__main__':
    show()
