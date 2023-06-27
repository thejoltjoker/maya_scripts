#!/usr/bin/env python3
"""add_selected_to_set.py
Description of add_selected_to_set.py.
"""
from maya import cmds


def set_exists(set: str):
    return set in cmds.ls(sets=True)


def add_to_set(nodes: list, set: str):
    if set_exists(set):
        set = cmds.sets(nodes, include=set)
    else:
        set = cmds.sets(nodes, name=set)
    cmds.select(set)
    print(f'Added {", ".join(nodes)} to {set}')
    return set


def prompt(nodes, placeholder=None):
    dialog_title = 'Add to set'
    dialog_message = 'Enter set name:'
    default_button = 'OK'
    cancel_button = 'Cancel'
    dialog = cmds.promptDialog(
        title=dialog_title,
        text=placeholder,
        message=dialog_message,
        button=[default_button, cancel_button],
        defaultButton=default_button,
        cancelButton=cancel_button,
        dismissString=cancel_button)

    if dialog == default_button:
        output = cmds.promptDialog(query=True, text=True)
        if output:
            # Do stuff here
            add_to_set(nodes, output)
        else:
            # If input is blank
            cmds.warning(dialog_title + ": The input can't be blank")
    else:
        # If dialog is cancelled
        print('User cancelled ' + dialog_title)


def main():
    """docstring for main"""
    selection = cmds.ls(sl=True)
    if cmds.nodeType(selection[-1]) == 'objectSet':
        set = selection[-1]
        selection.pop(-1)
        prompt(selection, set)
    else:
        prompt(selection)


if __name__ == '__main__':
    main()
