"""
apply_ncloth_preset_to_sel.py

Apply a nCloth preset to selected ncloth nodes.
"""
def applyNclothPreset():
    allObjs = cmds.ls(sl=True)
    for obj in allObjs:
        execStr = 'applyPresetToNode "%s" "" "" "glasssss" 1;' %(obj)