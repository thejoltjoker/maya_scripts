#!/usr/bin/env python3
"""mayacharm.py
Description of mayacharm.py.
"""

from maya import cmds


def run_config():
    """The code to execute in pycharm configuration"""
    import maya.cmds as cmds
    from importlib import reload
    from my_module import object as my_obj
    reload(my_obj)
    my_obj.main()


def main():
    """docstring for main"""
    port = 4435
    if not cmds.commandPort(":{}".format(port), query=True):
        cmds.commandPort(name=":{}".format(port))
        cmds.warning('Command port open on {}'.format(port))


if __name__ == '__main__':
    main()
