#!/usr/bin/env python3
"""export_to_afx.py
Description of export_to_afx.py.
"""
from maya import cmds


def set_unit(unit='mm'):
    """Set units to new units"""
    cmds.currentUnit(linear=unit)
    print("Units set to " + unit)
    return cmds.currentUnit(q=True)


def all_locators():
    """Get all locators"""
    locators = []
    transforms = cmds.ls(tr=True, l=True)
    for node in transforms:
        for shape in cmds.listRelatives(node, s=True):
            if cmds.nodeType(shape) == 'locator':
                locators.append(node)

    return locators

def bake_animation():
    """bakeResults -simulation true -t "0:120" -sampleBy 1 -oversamplingRate 1 -disableImplicitControl true -preserveOutsideKeys true -sparseAnimCurveBake false -removeBakedAttributeFromLayer false -removeBakedAnimFromLayer false -bakeOnOverrideLayer false -minimizeRotation true -controlPoints false -shape true {"camera1"};"""
    cmds.bakeResults(simulation=True,sampleBy=1,oversamplingRate=1,disableImplicitControl=True,preserveOutsideKeys=True,sparseAnimCurveBake=False,removeBakedAttributeFromLayer=False,removeBakedAnimFromLayer=False,bakeOnOverrideLayer=False,minimizeRotation=True,controlPoints=False,shape=True)
def renderable_cameras():
    """Get renderable cameras"""
    cameras = []
    for cam in cmds.ls(ca=True):
        if cmds.getAttr(cam + '.renderable'):
            cam_transform = cmds.listRelatives(cam, parent=True)
            cameras.append(cam_transform)

    return cameras


def baked_locators():
    locators = all_locators()
    return [x for x in locators if '_baked' in x]


def baked_cameras():
    cameras = renderable_cameras()
    return [x for x in cameras if '_baked' in x]


def main():
    """docstring for main"""
    pass


if __name__ == '__main__':
    main()
