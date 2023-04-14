#!/usr/bin/env python3
"""pyside2_template.py
A basic template for creating a pyside2 window in maya.
"""
from maya import cmds, mel
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QSizePolicy
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # Set window properties
        self.setWindowTitle('Window Title')
        self.setWindowFlags(QtCore.Qt.Window)
        self.setMinimumSize(240, 320)

        # Create button widgets
        self.button = QtWidgets.QPushButton('Button')

        # Main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.button)
        self.setLayout(main_layout)


def main():
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    ui = Window(mayaMainWindow)
    ui.show()
    return ui


if __name__ == '__main__':
    main()
