"""
apply_ncloth_preset_to_sel.py

Apply a nCloth preset to selected ncloth nodes.
"""


def apply_ncloth_preset(preset_name):
    allObjs = cmds.ls(sl=True)
    for obj in allObjs:
        execStr = 'applyPresetToNode "%s" "" "" "concrete" 1;' % (obj)
