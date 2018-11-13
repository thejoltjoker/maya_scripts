#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
constraint_and_delete.py
Moves an object in position and orients it. Using constraints, hence the name.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    cmds.pointConstraint(w=1, mo=False)
    cmds.orientConstraint(w=1, mo=False)
    cmds.delete(cn=True)


if __name__ == '__main__':
    main()
