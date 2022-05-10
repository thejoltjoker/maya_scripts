#!/usr/bin/env python
"""
cam_loc_scale.py
Description of Description of cam_loc_sca.py.
"""
import maya.cmds as cmds


def main():
    """docstring for function"""
    sel = cmds.ls(selection=True)

    for i in sel:
        cam = cmds.listRelatives(shapes=True)

        for c in cam:
            curVal = cmds.getAttr(c + '.locatorScale')
            newVal = curVal * 1.25
            print(newVal)
            cmds.setAttr(c + '.locatorScale', newVal)


if __name__ == '__main__':
    dialog_title = 'Camera Locator Scale'
    dialog_message = 'New size:'
    default_button = 'OK'
    cancel_button = 'Cancel'
    dialog = cmds.promptDialog(
        title=dialog_title,
        message=dialog_message,
        button=[default_button, cancel_button],
        defaultButton=default_button,
        cancelButton=cancel_button,
        dismissString=cancel_button)

    if dialog == default_button:
        output = cmds.promptDialog(query=True, text=True)
        if output:
            # Do stuff here
            main()
        else:
            # If input is blank
            cmds.warning(dialog_title + ": The input can't be blank")
    else:
        # If dialog is cancelled
        print('User cancelled ' + dialog_title)

