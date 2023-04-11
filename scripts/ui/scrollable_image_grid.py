#!/usr/bin/env python3
"""scrollable_image_grid.py
Description of scrollable_image_grid.py.
"""
import os
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore
import maya.cmds as cmds
import os
from PySide2 import QtGui, QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QGridLayout, QLabel, QWidget
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                               QHBoxLayout, QVBoxLayout, QMainWindow)


class ScrollPanelWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ScrollPanelWidget, self).__init__(parent)

        # formatting
        self.setWindowFlags(QtCore.Qt.Window)
        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle("Scroll Panel Widget")
        self.main_layout = QVBoxLayout()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.scroll_area_widget = QWidget()
        # self.scroll_area_widget.setGeometry(QtCore.QRect(0, 0, 240, 160))
        self.scroll_area_widget_layout = QVBoxLayout(self.scroll_area_widget)

        self.grid_layout = QGridLayout()

        grid_width = 3
        img = QtGui.QPixmap(
            r'C:\Users\JohannesAndersson\AppData\Local\Temp\pastebin\vlcsnap-2022-05-25-18h54m43s070.png')
        for i in range(100):
            label = QtWidgets.QLabel()
            label_size = QtWidgets.QSizePolicy()
            # sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
            label_size.setHorizontalStretch(0);
            label_size.setVerticalStretch(0);
            label_size.setHeightForWidth(label.sizePolicy().hasHeightForWidth());
            # label->setSizePolicy(sizePolicy);
            label.setSizePolicy(label_size)
            # label->setMinimumSize(QSize(16, 9));
            w = label.width()
            h = label.height()
            ratio = w / h
            w = self.width() / 3.5
            h = w / ratio
            label.setPixmap(img.scaled(w, h, Qt.KeepAspectRatio))
            label.setScaledContents(True)

            row = i // grid_width
            col = i % grid_width
            self.grid_layout.addWidget(label, row, col)

        self.scroll_area_widget_layout.addLayout(self.grid_layout)
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.main_layout.addWidget(self.scroll_area)
        self.setLayout(self.main_layout)
        # widgets
        # self.scroll_panel = QtWidgets.QWidget()
        # self.grid_layout = QtWidgets.QGridLayout(self.scroll_panel)
        # self.grid_layout.setAlignment(Qt.AlignTop)
        #
        # # Set up image folder path
        # self.image_folder_path = r'C:/Users/JohannesAndersson/AppData/Local/Temp/pastebin'
        # # Define the number of columns in the grid
        # num_cols = 3
        #
        # # Load images from folder
        # self.images = []
        # for image_file_name in os.listdir(self.image_folder_path):
        #     if image_file_name.endswith('.png'):
        #         image_path = os.path.join(self.image_folder_path, image_file_name)
        #         self.images.append(QtGui.QPixmap(image_path))
        #
        # # Add images to layout
        # for i, img in enumerate(self.images):
        #     label = QtWidgets.QLabel()
        #     label.setPixmap(img)
        #     row = i // num_cols
        #     col = i % num_cols
        #     print(row, col)
        #     self.grid_layout.addWidget(label, row, col)
        #
        #
        #
        # # self.scroll_panel_layout.setContentsMargins(0, 0, 0, 0)
        # self.scroll_area = QtWidgets.QScrollArea()
        # self.scroll_area.setWidgetResizable(True)
        # self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # # self.scroll_area.setWidget(self.scroll_panel)
        # self.scroll_area.setWidget(self.scroll_panel)
        # # layout
        # self.mainLayout = QtWidgets.QGridLayout(self)
        # self.mainLayout.setContentsMargins(0, 0, 0, 0)
        # self.mainLayout.addWidget(self.scroll_area)


def main():
    """docstring for main"""
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    # ui = ImageGrid(mayaMainWindow)
    # ui.show()
    # return ui

    # app = QtGui.QApplication(sys.argv)
    ex = ScrollPanelWidget(mayaMainWindow)
    ex.show()
    # sys.exit(app.exec_())


if __name__ == '__main__':
    main()
