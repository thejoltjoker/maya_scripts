import maya.cmds as cmds

selectedObjs = cmds.ls(sl=True)

for obj in selectedObjs:

    cmds.setAttr(obj + ".visibility", l=True)

    if obj.endswith('_ctrl'):

        #scaleXAttr = cmds.getAttr( obj + ".scaleX", l=False )
        #scaleYAttr = cmds.getAttr( obj + ".scaleY", l=False )
        #scaleZAttr = cmds.getAttr( obj + ".scaleZ", l=False )

        #translateXAttr = cmds.getAttr( obj + ".translateY", l=False )
        #translateYAttr = cmds.getAttr( obj + ".translateZ", l=False )
        #translateZAttr = cmds.getAttr( obj + ".translateX", l=False )

        cmds.setAttr(obj + ".scaleX", k=True)
        cmds.setAttr(obj + ".scaleX", l=True)

        cmds.setAttr(obj + ".scaleY", k=True)
        cmds.setAttr(obj + ".scaleY", l=True)

        cmds.setAttr(obj + ".scaleZ", k=True)
        cmds.setAttr(obj + ".scaleZ", l=True)

        if obj.endswith('Fk_ctrl' or 'FkOffset_ctrl'):

            cmds.setAttr(obj + ".translateX", k=True)
            cmds.setAttr(obj + ".translateX", l=True)

            cmds.setAttr(obj + ".translateY", k=True)
            cmds.setAttr(obj + ".translateY", l=True)

            cmds.setAttr(obj + ".translateZ", k=True)
            cmds.setAttr(obj + ".translateZ", l=True)


########################################

attr = getattr(obj, 'attr', None)
if attr is not None:
    attr()
    # Do something, either attr(), or func(attr), or whatever
else:
    # Do something else
