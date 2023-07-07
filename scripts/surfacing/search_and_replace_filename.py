#!/usr/bin/env python
"""
search_and_replace_filename.py
Does a search and replace on selected file nodes.
"""
import json

from maya import cmds, mel
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QSizePolicy
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance


def search_replace_filename(input_string, output_string):
    sel_nodes = cmds.ls(sl=True, type='file')

    search_for = input_string.replace('\\', '/')
    replace_with = output_string.replace('\\', '/')

    for node in sel_nodes:
        texture_path = cmds.getAttr(node + ".fileTextureName").replace('\\', '/')

        new_texture_path = texture_path.replace(search_for, replace_with)
        cmds.setAttr("{}.fileTextureName".format(node),
                     new_texture_path,
                     type='string')

        print("Path changed from " + texture_path + " to " + new_texture_path + " on node " + node)


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # Set window properties
        self.setWindowTitle('Search and replace')
        self.setWindowFlags(QtCore.Qt.Window)
        self.setMinimumSize(400, 40)

        # Main layout
        main_layout = QtWidgets.QVBoxLayout()

        # Form
        form_layout = QtWidgets.QFormLayout()
        self.search_line = QtWidgets.QLineEdit()
        self.replace_line = QtWidgets.QLineEdit()

        form_layout.addRow('Search for:', self.search_line)
        form_layout.addRow('Replace with:', self.replace_line)

        # Buttons
        self.ok_button = QtWidgets.QPushButton('OK')
        self.ok_button.clicked.connect(self.ok_action)
        self.cancel_button = QtWidgets.QPushButton('Cancel')
        self.cancel_button.clicked.connect(self.close)  # Connect cancel_button to close the window
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        # Fill layout
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def ok_action(self):
        search_replace_filename(self.search_line.text(), self.replace_line.text())


def main():
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    ui = Window(mayaMainWindow)
    ui.show()
    return ui


# def main():
#     input_string = cmds.promptDialog(
#         title='Search and Replace',
#         message='Search for:',
#         button=['OK...', 'Cancel'],
#         defaultButton='OK...',
#         cancelButton='Cancel',
#         dismissString='Cancel')
#
#     if input_string == 'OK...':
#         input_string = cmds.promptDialog(query=True, text=True)
#         if not input_string:
#             cmds.warning('You must enter a search string')
#             exit()
#
#     output_string = cmds.promptDialog(
#         title='Search and Replace',
#         message='Replace with:',
#         button=['OK', 'Cancel'],
#         defaultButton='OK',
#         cancelButton='Cancel',
#         dismissString='Cancel')
#
#     if output_string == 'OK':
#         output_string = cmds.promptDialog(query=True, text=True)
#     else:
#         output_string = ''
#
#     search_replace_filename(input_string, output_string)


if __name__ == '__main__':
    main()
