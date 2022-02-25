"""update_frame_rate_keep_range.py
Description of update_frame_rate_keep_range.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""

    origStartFrame = cmds.getAttr('defaultRenderGlobals.startFrame')
    origEndFrame = cmds.getAttr('defaultRenderGlobals.endFrame')
    print("Original frame range")
    print(origStartFrame)
    print(origEndFrame)
    print("Original frame rate")
    print(cmds.currentUnit(query=True, time=True))

    cmds.currentUnit(time='pal')
    cmds.setAttr('defaultRenderGlobals.startFrame', origStartFrame)
    cmds.setAttr('defaultRenderGlobals.endFrame', origEndFrame)

    newStartFrame = cmds.getAttr('defaultRenderGlobals.startFrame')
    newEndFrame = cmds.getAttr('defaultRenderGlobals.endFrame')
    print("New frame range")
    print(origStartFrame)
    print(origEndFrame)
    print("New frame rate")
    print(cmds.currentUnit(query=True, time=True))


if __name__ == '__main__':
    main()
