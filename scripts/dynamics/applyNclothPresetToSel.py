def applyNclothPreset():
allObjs = cmds.ls(sl=True)
for obj in allObjs:
    execStr = 'applyPresetToNode "%s" "" "" "glasssss" 1;' %(obj)

applyNclothPreset()