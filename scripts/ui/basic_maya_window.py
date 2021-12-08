#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds


def action():
    print(True)


def main(title):
    """docstring for main"""
    window = cmds.window(title=title)

    # Create layout
    cmds.formLayout()

    # Add elements
    cmds.text(label='Attribute')
    attribute = cmds.textField()
    cmds.text(label='Value')
    value = cmds.textField()

    # Add actions to elements
    cmds.textField(attribute, edit=True, enterCommand=('cmds.setFocus("{0}")'.format(value)))
    cmds.textField(value, edit=True, enterCommand=action)

    # A button that does nothing
    cmds.button(label='Apply', command=action)

    cmds.button(label='Close', command=('cmds.deleteUI("{0}", window=True)'.format(window)))

    # Set its parent to the Maya window (denoted by '..')
    cmds.setParent('..')

    # Show the window that we created (window)
    cmds.showWindow(window)

    #    Attach commands to pass focus to the next field if the Enter
    #    key is pressed. Hitting just the Return key will keep focus
    #    in the current field.
    #

    window = cmds.window()
    form = cmds.formLayout(numberOfDivisions=100)
    b1 = cmds.button()
    b2 = cmds.button()
    column = cmds.columnLayout()
    cmds.button()
    cmds.button()
    cmds.button()

    cmds.formLayout(form, edit=True,
                    attachForm=[(b1, 'top', 5),
                                (b1, 'left', 5),
                                (b2, 'left', 5),
                                (b2, 'bottom', 5),
                                (b2, 'right', 5),
                                (column, 'top', 5), (column, 'right', 5)],
                    attachControl=[(b1, 'bottom', 5, b2), (column, 'bottom', 5, b2)],
                    attachPosition=[(b1, 'right', 5, 75), (column, 'left', 0, 75)], attachNone=(b2, 'top'))

    cmds.showWindow(window)


if __name__ == '__main__':
    main('window')
