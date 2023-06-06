#!/usr/bin/env python3
"""create_playblast.py
Description of create_playblast.py.
"""
import maya.cmds as cmds
import os
import datetime
import subprocess
from pathlib import Path

def playblast_dialog(placeholder=None):
    ph = placeholder if placeholder else os.path.join(cmds.workspace(q=True, rd=True), "images")
    dialog_title = 'Create Playblast'
    dialog_message = 'Output path:'
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
            playblast(output)
            return output
        else:
            # If input is blank
            cmds.warning(dialog_title + ": The input can't be blank")
    else:
        # If dialog is cancelled
        print('User cancelled ' + dialog_title)


def playblast(folder=None):
    """docstring for main"""

    # Get the open scene name
    scene_name = cmds.file(q=True, sn=True, shn=True).split(".")[0]

    # Set the folder path
    folder = folder if folder else os.path.join(cmds.workspace(q=True, rd=True), "images")

    # Create the folder if it doesn't exist
    today = datetime.datetime.now().strftime("%y%m%d")
    folder = os.path.join(folder, today, scene_name)
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Set the file path
    filepath = os.path.join(folder, scene_name)

    # Set the playblast options
    width = 1920
    height = 1080
    format = "image"
    compression = "png"
    quality = 100

    # Set the time range
    current_frame = cmds.currentTime(query=True)

    # Create the playblast
    pb = cmds.playblast(
        filename=filepath,
        format=format,
        compression=compression,
        quality=quality,
        percent=100,
        width=width,
        height=height,
        fr=current_frame,
        viewer=False,
        showOrnaments=False,
        offScreen=True
    )
    print(Path(folder).resolve())
    subprocess.Popen(fr'explorer "{Path(folder).resolve()}"')
    return pb


def main():
    playblast_dialog()


if __name__ == '__main__':
    main()
