#!/usr/bin/env python3
"""toggle_redraw.py
Description of toggle_redraw.py.
"""
from maya import cmds


def continue_button_callback(*args):
    # Code to execute when the "Continue" button is clicked
    print("Continuing redraw")
    cmds.refresh(suspend=True)


def suspend_button_callback(*args):
    # Code to execute when the "Suspend" button is clicked
    print("Suspending redraw")
    cmds.refresh(suspend=True)


def main():
    """docstring for main"""
    result = cmds.confirmDialog(
        title='Continue/Suspend View Redraw',
        message='Choose an action:',
        button=['Continue', 'Suspend'],
        defaultButton='Continue',
        cancelButton='Suspend',
        dismissString='Suspend'
    )

    # Check the result
    if result == 'Continue':
        continue_button_callback()
    else:
        suspend_button_callback()


if __name__ == '__main__':
    main()
