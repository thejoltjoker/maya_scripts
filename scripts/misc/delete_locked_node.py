sel = cmds.ls(sl=True)
for i in sel:
    cmds.lockNode(i, lock=False)
    cmds.delete(i)