"""
create_playblast.py
Description of create_playblast.py.
"""
import os
import re
import subprocess
import sys
from datetime import datetime
from pprint import pprint

from PySide2 import QtWidgets, QtCore
from maya import cmds

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s: %(message)s')
logger = logging.getLogger()


def open_folder(path):
    cmd = None
    if sys.platform == 'darwin':
        cmd = ['open', path]
    elif sys.platform == 'win32':
        cmd = ['start', path]
    if cmd:
        subprocess.Popen(cmd)


class Window(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        # Main layout
        self.layout_main = QtWidgets.QVBoxLayout()

        # Description name layout
        self.layout_description = QtWidgets.QHBoxLayout()
        self.line_description = QtWidgets.QLineEdit()
        self.fill_description()
        self.layout_description.addWidget(self.line_description)

        # Name fill
        self.button_description_fill = QtWidgets.QPushButton('<<')
        self.button_description_fill.clicked.connect(self.fill_description)
        self.layout_description.addWidget(self.button_description_fill)

        # Project layout
        self.layout_project = QtWidgets.QHBoxLayout()

        # Workspace dropdown
        self.combo_workspace = QtWidgets.QComboBox()
        self.combo_workspace.addItem('No workspaces')
        self.update_workspaces()
        self.combo_workspace.currentTextChanged.connect(self.update_projects)
        self.layout_project.addWidget(self.combo_workspace)

        # Project dropdown
        self.combo_project = QtWidgets.QComboBox()
        self.combo_project.addItem('No projects')
        self.init_projects()
        self.combo_project.currentTextChanged.connect(self.store_dropdown_to_file)
        self.layout_project.addWidget(self.combo_project)

        # Start button
        self.button_start = QtWidgets.QPushButton('Start')
        self.button_start.clicked.connect(self.start_timer)
        self.layout_project.addWidget(self.button_start)

        # Add layouts to main layout
        self.layout_main.addLayout(self.layout_description)
        self.layout_main.addLayout(self.layout_project)

        self.widget_main = QtWidgets.QWidget()
        self.widget_main.setWindowFlags(self.windowFlags() | QtCore.Qt.Dialog)
        self.widget_main.setLayout(self.layout_main)
        self.setCentralWidget(self.widget_main)
        # self.setGeometry(50, 100, 500, 50)
        self.setWindowTitle("Start timer")


def active_camera():
    panel = cmds.getPanel(withFocus=True)
    cam_shape = cmds.modelEditor(panel, q=1, av=1, cam=1)

    if cmds.listRelatives(cam_shape, p=True):
        return cmds.listRelatives(cam_shape, p=True)[0]
    return None


def playblast(*args, **kwargs):
    scene_path, scene_name = os.path.split(cmds.file(sn=True, q=True))
    today = datetime.today().strftime('%y%m%d')
    new_dailies_folder = os.path.abspath(os.path.join(scene_path, '..', 'playblast', today))

    if not os.path.exists(new_dailies_folder):
        os.makedirs(new_dailies_folder)

    filename = '_'.join([today, os.path.splitext(scene_name)[0]])
    if re.findall('_v\d\d\d', filename):
        filename = filename[:-4] + active_camera() + filename[-5:len(filename)]

    out_file = os.path.join(new_dailies_folder, filename)
    out_file = os.path.abspath("{0}.mov".format(out_file))
    print(out_file)
    params = {'filename': out_file,
              'clearCache': True,
              'orn': False,
              'v': False,
              'percent': 100,
              'quality': 100,
              'width': 1920,
              'height': 1080,
              'fo': True
              }
    pprint(params)
    if sys.platform == 'win32':
        params['format'] = 'qt'
        params['compression'] = 'Animation'
    elif sys.platform == 'darwin':
        params['format'] = 'avfoundation'
        params['compression'] = 'H.264'

    cmds.playblast(**params)
    cmds.warning("{0} created in {1}".format(filename, new_dailies_folder))

    # Open folder after creation
    open_folder(os.path.dirname(params['filename']))


def main():
    """docstring for main"""
    playblast()


if __name__ == '__main__':
    main()
