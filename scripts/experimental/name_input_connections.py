#!/usr/bin/env python
"""
name_input_connections.py
Description of name_input_connections.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    sel = cmds.ls(sl=True)
    for i in sel:
        con = cmds.listConnections(i, c=True, d=True, s=False, scn=True)
        for l in con:
            print l


if __name__ == '__main__':
    main()
