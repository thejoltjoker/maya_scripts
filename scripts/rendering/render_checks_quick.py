import maya.cmds as cmds

print('### RENDER CHECKS ###')


def check_renderable_camera():
    camera = ''
    return camera


def check_frame_range():
    start = cmds.getAttr("defaultRenderGlobals.startFrame")
    end = cmds.getAttr("defaultRenderGlobals.endFrame")
    return start, end


def check_resolution():
    resolution = ''
    return resolution


def check_gi():
    return


def check_motion_blur():
    return


print('### DONE ###')
