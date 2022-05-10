#!/usr/bin/env python3
"""set_system_file_dialog.py
Description of set_system_file_dialog.py.
"""
from maya import cmds


def main():
    """docstring for main"""
    cmds.optionVar(iv=('FileDialogStyle', 1))


if __name__ == '__main__':
    main()
