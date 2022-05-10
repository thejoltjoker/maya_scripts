import maya.cmds as cmds

selectedObjs = cmds.ls(sl=True)

for obj in selectedObjs:
    if obj.endswith('_ctrl'):

        scaleXAttr = cmds.getAttr(obj + ".scaleX", l=False)
        scaleYAttr = cmds.getAttr(obj + ".scaleY", l=False)
        scaleZAttr = cmds.getAttr(obj + ".scaleZ", l=False)

        translateXAttr = cmds.getAttr(obj + ".translateY", l=False)
        translateYAttr = cmds.getAttr(obj + ".translateZ", l=False)
        translateZAttr = cmds.getAttr(obj + ".translateX", l=False)

        if scaleXAttr is True:
            cmds.setAttr(obj + ".scaleX", k=False)
            cmds.setAttr(obj + ".scaleX", l=True)
        else:
            cmds.setAttr(obj + ".scaleX", k=True)
            cmds.setAttr(obj + ".scaleX", l=False)

        if scaleYAttr is True:
            cmds.setAttr(obj + ".scaleY", k=False)
            cmds.setAttr(obj + ".scaleY", l=True)
        else:
            cmds.setAttr(obj + ".scaleY", k=True)
            cmds.setAttr(obj + ".scaleY", l=False)

        if scaleZAttr is True:
            cmds.setAttr(obj + ".scaleZ", k=False)
            cmds.setAttr(obj + ".scaleZ", l=True)
        else:
            cmds.setAttr(obj + ".scaleZ", k=True)
            cmds.setAttr(obj + ".scaleZ", l=False)

        if obj.endswith('Fk_ctrl' or 'FkOffset_ctrl'):
            if translateXAttr is True:
                cmds.setAttr(obj + ".translateX", k=False)
                cmds.setAttr(obj + ".translateX", l=True)
            else:
                cmds.setAttr(obj + ".translateX", k=True)
                cmds.setAttr(obj + ".translateX", l=False)

            if translateYAttr is True:
                cmds.setAttr(obj + ".translateY", k=False)
                cmds.setAttr(obj + ".translateY", l=True)
            else:
                cmds.setAttr(obj + ".translateY", k=True)
                cmds.setAttr(obj + ".translateY", l=False)

            if translateZAttr is True:
                cmds.setAttr(obj + ".translateZ", k=False)
                cmds.setAttr(obj + ".translateZ", l=True)
            else:
                cmds.setAttr(obj + ".translateZ", k=True)
                cmds.setAttr(obj + ".translateZ", l=False)


########################################
