#!/usr/bin/env python
"""
quick_export.py

Exports the currently selected objects from maya to a folder next to the saved maya file.

README.md:
# Quick Export

A tool for quickly exporting the selected objects to the `{current_scene}/exports` folder.

## Instructions

1. Select file format.

1. Add a suffix. If you don't enter any suffix it will use the currently opened scene's name with an increment.

1. Press **Export**.

The full path to the file should fill the text field in the *Output* section.
Just select it and copy or you can press **Open folder** to open the exports folder.

![Quick export window](https://i.imgur.com/18tpqyC.png)
"""
import os
import sys
import subprocess
import string
import maya.cmds as cmds
from sys import platform
from PySide2.QtWidgets import *


class QuickExport(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Quick Export")
        self.setGeometry(0, 0, 294, 228)

        # Create the central widget and grid layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout(central_widget)

        # Create the Quick export group box
        group_box = QGroupBox("Quick export")
        group_box_layout = QGridLayout(group_box)
        grid_layout.addWidget(group_box, 0, 0)

        # Add the file format label and combo box to the Quick export group box
        label_format = QLabel("File format:")
        combo_format = QComboBox()
        group_box_layout.addWidget(label_format, 0, 0)
        group_box_layout.addWidget(combo_format, 0, 1)

        # Add the suffix label and line edit to the Quick export group box
        label_suffix = QLabel("Suffix (optional):")
        line_suffix = QLineEdit()
        group_box_layout.addWidget(label_suffix, 1, 0)
        group_box_layout.addWidget(line_suffix, 1, 1)

        # Create the Output group box
        group_box_2 = QGroupBox("Output")
        group_box_2_layout = QGridLayout(group_box_2)
        grid_layout.addWidget(group_box_2, 1, 0)

        # Add the output line edit and open folder button to the Output group box
        line_output = QLineEdit()
        button_open = QPushButton("Open folder")
        group_box_2_layout.addWidget(line_output, 0, 0)
        group_box_2_layout.addWidget(button_open, 0, 1)

        # Add the Export button to the grid layout
        button_export = QPushButton("Export")
        grid_layout.addWidget(button_export, 2, 0)

        # Create the menu bar and status bar
        menu_bar = QMenuBar()
        status_bar = QStatusBar()
        self.setMenuBar(menu_bar)
        self.setStatusBar(status_bar)


class QuickExport(object):
    def __init__(self):
        """Setup ui"""
        script_path = os.path.split(__file__)[0]

        ui_file = os.path.join(script_path, '..', '.ui', 'quick_export.ui')

        # Load window
        qt_win = cmds.loadUI(uiFile=ui_file)

        # Format dropdown
        self.dropdown_format = 'combo_format'
        cmds.optionMenu(self.dropdown_format, edit=True, enable=True)
        file_formats = ['Maya Ascii', 'Maya Binary', 'OBJ', 'FBX']
        for f in file_formats:
            cmds.menuItem(label=f, parent=self.dropdown_format)

        # Output section
        self.line_output = 'line_output'
        cmds.textField(
            self.line_output, edit=True, tx='Press export to get path')

        cmds.button('button_open', edit=True, command=self.open_folder)

        # Export button
        cmds.button('button_export', edit=True, command=self.main)

        cmds.showWindow(qt_win)

    def format_filename(self, name):
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        filename = ''.join(c for c in name if c in valid_chars)
        filename = filename.replace(' ', '_')
        return filename

    def open_folder(self, *args):
        exports_path = os.path.dirname(
            cmds.textField(self.line_output, q=True, tx=True))
        if platform == "win32":
            subprocess.Popen('explorer "{}"'.format(exports_path))
        else:
            exports_path_slash = exports_path.replace('\\', '/')
            subprocess.call(["open", "-R", exports_path_slash])

    def enable_obj_plugin(self):
        # List the plugins that are currently loaded
        plugins = cmds.pluginInfo(query=True, listPlugins=True)
        # Load obj export
        if 'objExport' not in plugins:
            cmds.loadPlugin('objExport')

    def enable_fbx_plugin(self):
        # List the plugins that are currently loaded
        plugins = cmds.pluginInfo(query=True, listPlugins=True)
        # Load fbx maya
        if 'fbxmaya' not in plugins:
            cmds.loadPlugin('fbxmaya')

    def main(self, *args):
        """docstring for main"""
        if cmds.ls(sl=True):
            # 1. Get current file name and directory
            maya_file = cmds.file(q=True, sn=True, shn=True)
            maya_file_path = os.path.dirname(cmds.file(q=True, sn=True))
            maya_filename, maya_file_ext = os.path.splitext(maya_file)

            if not maya_file:
                maya_file = cmds.ls(sl=True)[0]
                maya_filename = maya_file
                maya_file_path = cmds.workspace(q=True, dir=True)
                print(
                    "File not saved. Using workspace directory and object name instead."
                )

            export_name = maya_filename
            export_suffix = cmds.textField('line_suffix', q=True, text=True)
            export_format = cmds.optionMenu(
                self.dropdown_format, q=True, value=True)

            if export_format == 'Maya Ascii':
                print
                export_format
                file_type = 'mayaAscii'
                export_extension = 'ma'

            elif export_format == 'Maya Binary':
                file_type = 'mayaBinary'
                export_extension = 'mb'

            elif export_format == 'OBJ':
                self.enable_obj_plugin()
                file_type = 'OBJexport'
                export_extension = 'obj'

            elif export_format == 'FBX':
                self.enable_fbx_plugin()
                file_type = 'Fbx'
                export_extension = 'fbx'

            # elif export_format == 'Alembic':
            #     file_type = 'Alembic'
            #     export_extension = 'abc'

            if export_suffix:
                export_name = '{}_{}'.format(export_name, export_suffix)

            # Format filename and remove weird characters
            export_name = self.format_filename(export_name)

            export_filename = '{}.{}'.format(export_name, export_extension)

            increment = 1

            # 2. Check if exports folder exists, otherwise create it
            exports_folder = os.path.join(maya_file_path, 'exports')
            if not os.path.exists(exports_folder):
                os.makedirs(exports_folder)

            # 3. Check if filename already exists, if so version up

            if os.path.exists(os.path.join(exports_folder, export_filename)):
                export_filename = '{}_{:03}.{}'.format(
                    export_name, increment, export_extension)
                while os.path.exists(os.path.join(exports_folder, export_filename)):
                    increment += 1
                    export_filename = '{}_{:03}.{}'.format(
                        export_name, increment, export_extension)

            export_file = os.path.join(exports_folder, export_filename)

            # 4. export file
            cmds.file(export_file, type=file_type, es=True)

            if platform == "win32":
                cmds.textField(self.line_output,
                               edit=True,
                               tx=export_file.replace('/', '\\'),
                               en=True)
            else:
                cmds.textField(
                    self.line_output, edit=True, tx=export_file, en=True)

            font_color = '#0cf'
            message = 'Exported'
            cmds.inViewMessage(smg='<font color={}>{}</font>'.format(font_color,
                                                                     message), bkc=0x00262626, pos='topRight',
                               fade=True, a=0.5)
        else:
            cmds.warning("No objects selected!")


def main():
    QuickExport()


if __name__ == '__main__':
    main()
