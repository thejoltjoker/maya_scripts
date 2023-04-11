# !/usr/bin/env python3
"""viewport_to_desktop.py
Description of viewport_to_desktop.py.
"""
import os.path
from maya import cmds
from pathlib import Path


def output_path():
    current_camera = 'persp'
    for vp in cmds.getPanel(type="modelPanel"):
        current_camera = cmds.modelEditor(vp, q=1, av=1, cam=1)
    if '|' in current_camera:
        current_camera = current_camera.split('|')[-2]

    filename = Path(cmds.file(q=True, sn=True))
    # desktop = Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
    desktop = Path(r'C:\Users\JohannesAndersson\OneDrive - Frank Valiant AB\Desktop')
    return desktop / f'{filename.stem}_{current_camera}.png'


def thumbnail():
    """Create a thumbnail from the viewport"""
    cur_frame = cmds.currentTime(query=True)
    cmds.playblast(fr=cur_frame, fmt='image', compression='png',
                   cf=cache_file_thumb, orn=False, v=False)


def save_viewport(path: Path):
    current_frame = cmds.currentTime(query=True)
    cmds.playblast(format='image',
                   frame=current_frame,
                   completeFilename=str(path.resolve()),
                   showOrnaments=0,
                   compression='png',
                   percent=100,
                   widthHeight=(1920, 1080))
    return path


def path_dialog(placeholder=None):
    text = placeholder if placeholder else os.path.dirname(cmds.file(q=True, exn=True))
    dialog_title = 'Output Path'
    dialog_message = 'Output path:'
    default_button = 'OK'
    cancel_button = 'Cancel'
    dialog = cmds.promptDialog(
        title=dialog_title,
        message=dialog_message,
        text=text,
        button=[default_button, cancel_button],
        defaultButton=default_button,
        cancelButton=cancel_button,
        dismissString=cancel_button)

    if dialog == default_button:
        output = cmds.promptDialog(query=True, text=True)
        if output:
            # Do stuff here
            save_viewport(text)
        else:
            # If input is blank
            cmds.warning(dialog_title + ": The input can't be blank")
    else:
        # If dialog is cancelled
        print('User cancelled ' + dialog_title)


def main():
    """docstring for main"""
    path_dialog(output_path())


if __name__ == '__main__':
    main()
