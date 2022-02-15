#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
create_control_offset.py
Description of create_control_offset.py.
"""
import maya.cmds as cmds


def set_attr(attribute, value):
    """docstring for main"""
    sel = cmds.ls(sl=True)

    for node in sel:
        if cmds.attributeQuery(attribute, node=node, ex=True):
            node_attr = '.'.join([node, attribute])
            cmds.setAttr(node_attr, value)

            print("{attr} was set to {val}".format(attr=node_attr, val=value))


def dialog_window(title, ):
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
    cmds.textField(value, edit=True, enterCommand=set_attr)

    # A button that does nothing
    cmds.button(label='Apply', command=set_attr)

    cmds.button(label='Close', command=('cmds.deleteUI("{0}", window=True)'.format(window)))

    # Set its parent to the Maya window (denoted by '..')
    cmds.setParent('..')

    # Show the window that we created (window)
    cmds.showWindow(window)

    #    Attach commands to pass focus to the next field if the Enter
    #    key is pressed. Hitting just the Return key will keep focus
    #    in the current field.
    #


if __name__ == '__main__':
    dialog_window('test')
    #     dialog_title = 'Set Attributes'
    # dialog_message = 'Attribute:'
    # default_button = 'OK'
    # cancel_button = 'Cancel'
    # dialog_attribute = cmds.promptDialog(
    #     title=dialog_title,
    #     message=dialog_message,
    #     button=[default_button, cancel_button],
    #     defaultButton=default_button,
    #     cancelButton=cancel_button,
    #     dismissString=cancel_button)
    #
    # if dialog == default_button:
    #     output = cmds.promptDialog(query=True, text=True)
    # if output:
    # # Do stuff here
    #     pass
    # else:
    # # If input is blank
    #     cmds.warning(dialog_title + ": The input can't be blank")
    # else:
    # # If dialog is cancelled
    # print 'User cancelled ' + dialog_title
    #
    # dialog_title = 'Set Attributes'
    # dialog_message = 'Value:'
    # default_button = 'OK'
    # cancel_button = 'Cancel'
    # dialog_value = cmds.promptDialog(
    #     title=dialog_title,
    #     message=dialog_message,
    #     button=[default_button, cancel_button],
    #     defaultButton=default_button,
    #     cancelButton=cancel_button,
    #     dismissString=cancel_button)
    #
    # if dialog == default_button:
    #     output = cmds.promptDialog(query=True, text=True)
    # if output:
    # # Do stuff here
    #     pass
    # else:
    # # If input is blank
    #     cmds.warning(dialog_title + ": The input can't be blank")
    # else:
    # # If dialog is cancelled
    # print 'User cancelled ' + dialog_title
