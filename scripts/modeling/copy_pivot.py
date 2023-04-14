#!/usr/bin/env python3
"""copy_pivot.py
Description of copy_pivot.py.
"""

from maya import cmds, mel


def main():
    """Match all selected objects' pivot points (Rotation, Scale, Orientation)
    to the last chosen source's pivot, without moving the objects themselves. """
    selection = cmds.ls(sl=True)
    source = selection[1]
    target = selection[0]
    mel.eval('MatchPivots; performMatchPivots 0;')


if __name__ == '__main__':
    main()
