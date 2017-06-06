sel = cmds.ls()
for i in sel:
    if i.endswith('RN'):
        cmds.lockNode(i, lock=False)
        cmds.delete(i)