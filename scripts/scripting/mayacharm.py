#!/usr/bin/env python3
"""mayacharm.py
Description of mayacharm.py.
"""

from maya import cmds


def main():
    """docstring for main"""

    if not cmds.commandPort(":4435", query=True):
        cmds.commandPort(name=":4435")


if __name__ == '__main__':
    main()
