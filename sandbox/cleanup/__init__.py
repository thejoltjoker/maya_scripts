#!/usr/bin/env python
"""
Cleanup
Description of Cleanup.
"""
import maya.cmds as cmds
import maya.mel as mel

def cleanup():
    """docstring for cleanup"""

    all_nodes = cmds.ls()
    sel_nodes = cmds.ls(sl=True)

    # Delete history
    for node in all_nodes:
        cmds.delete(node, ch=True)

    # Delete unused nodes
    mel.eval('MLdeleteUnused;')

    # Delete render settings nodes
    cmds.delete('redshiftOptions')
    cmds.delete('vraySettings')
    miDefaultOptions
    miDefaultFramebuffer
    miContourPreset
    mentalrayItemsList
    mentalrayGlobals
    Draft
    DraftMotionBlur
    DraftRapidMotion
    Preview
    PreviewCaustics
    PreviewFinalGather
    PreviewGlobalIllum
    PreviewImrRayTracyOff
    PreviewImrRayTracyOn
    PreviewMotionblur
    PreviewRapidMotion
    Production
    ProductionFineTrace
    ProductionMotionblur
    ProductionRapidFur
    ProductionRapidHair
    ProductionRapidMotion
    surfaceSamplingMiOptionsNode
    sceneConfigurationScriptNode
    uiConfigurationScriptNode
    sequenceManager1

    # Delete foster parents
    for node in all_nodes:
        node_type = cmds.nodeType(node)
        if node_type == 'fosterParent'
            cmds.delete(node)

    # Delete render layers


    # Delete cameras

if __name__ == '__main__':
    cleanup()



# Render nodes
    # sceneConfigurationScriptNode
    # uiConfigurationScriptNode