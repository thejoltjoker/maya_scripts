#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
set_images_path.py
Set image path to match the pipeline and create output folder if it doesn't exist.
"""
import maya.cmds as cmds
import os


def path_dialog(placeholder=None):
    ph = placeholder if placeholder else os.path.dirname(cmds.file(q=True, exn=True))
    dialog_title = 'Images Path'
    dialog_message = 'Images path:'
    default_button = 'OK'
    cancel_button = 'Cancel'
    dialog = cmds.promptDialog(
        title=dialog_title,
        message=dialog_message,
        text=ph,
        button=[default_button, cancel_button],
        defaultButton=default_button,
        cancelButton=cancel_button,
        dismissString=cancel_button)

    if dialog == default_button:
        output = cmds.promptDialog(query=True, text=True)
        if output:
            # Do stuff here
            print(output)
            set_images_path(output)
            return output
        else:
            # If input is blank
            cmds.warning(dialog_title + ": The input can't be blank")
    else:
        # If dialog is cancelled
        print('User cancelled ' + dialog_title)


def main():
    """docstring for main"""
    file_path = cmds.file(q=True, exn=True)
    file_directory = os.path.dirname(file_path)

    # Construct output path
    render_path = os.path.abspath(os.path.join(file_directory, '..', '..', '..', 'published', 'render'))

    output = path_dialog(render_path)

    # Print workspace
    rules = cmds.workspace(fileRule=True, q=True)
    img_index = rules.index("images") + 1
    cmds.warning('Images path is {0}'.format(rules[img_index]))


def set_images_path(render_path):
    # Check if parent folder exists
    if os.path.isdir(os.path.dirname(render_path)):

        # Create output folder so Deadline won't complain
        if not os.path.isdir(render_path):
            os.mkdir(render_path)

        # Set images in workspace
        cmds.workspace(fileRule=['images', render_path])

        # Save workspace to disk
        cmds.workspace(saveWorkspace=True)


if __name__ == '__main__':
    main()
