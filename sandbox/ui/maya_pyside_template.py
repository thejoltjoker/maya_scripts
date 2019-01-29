#!/usr/bin/env python
"""
maya_pyside_template.py
Basic UI template for PySide in Maya.
"""
from PySide import QtCore
from PySide import QtGui
import shiboken

import maya.cmds as cmds
import maya.OpenMayaUI as mui


class Window(QtGui.QDialog):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        # Custom code here
        self.resize(800, 600)
        self.setWindowTitle('Maya PySide template')


def getMainWindow():
    ptr = mui.MQtUtil.mainWindow()
    mainWin = shiboken.wrapInstance(long(ptr), QtGui.QMainWindow)
    return mainWin


def show():
    win = Window(parent=getMainWindow())
    win.show()
    win.raise_()
    return win


def main():
    show()


if __name__ == '__main__':
    main()
