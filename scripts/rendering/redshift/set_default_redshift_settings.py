#!/usr/bin/env python
"""
set_default_redshift_settings.py
Description of set_default_redshift_settings.py.
"""
import maya.cmds as cmds
import maya.mel as mel
def set_default_settings():
    # mel.eval('unifiedRenderGlobalsWindow')
    # List the plugins that are currently loaded
    plugins = cmds.pluginInfo(query=True, listPlugins=True)
    # Load Redshift
    if 'redshift4maya' in plugins:
        om.MGlobal.displayInfo("Redshift is already loaded.")
    else:
        cmds.loadPlugin('redshift4maya')
        om.MGlobal.displayInfo("Redshift is now loaded.")

    if cmds.getAttr('defaultRenderGlobals.currentRenderer') != 'redshift':
        cmds.setAttr('defaultRenderGlobals.currentRenderer', 'redshift', type='string')
        cmds.warning('Redshift was set as current renderer')

    mel.eval('redshiftGetRedshiftOptionsNode(true)')

    # File settings
    cmds.setAttr('redshiftOptions.imageFormat', 1)
    # cmds.setAttr('redshiftOptions.noSaveImage', 1)
    cmds.setAttr('redshiftOptions.exrMultipart', 0)
    cmds.setAttr('redshiftOptions.exrForceMultilayer', 0)
    cmds.setAttr('defaultRenderGlobals.ifp',
                 '<Scene>/<Scene>_<RenderLayer>', type='string')

    # Animation settings
    maxFrame = cmds.playbackOptions(q=True, max=True)
    minFrame = cmds.playbackOptions(q=True, min=True)
    cmds.setAttr('defaultRenderGlobals.animation', 1)
    cmds.setAttr('defaultRenderGlobals.byFrameStep', 1)
    cmds.setAttr('defaultRenderGlobals.extensionPadding', 4)

    # Output settings
    cmds.setAttr('defaultResolution.width', 1920)
    cmds.setAttr('defaultResolution.height', 1080)
    cmds.setAttr('defaultResolution.deviceAspectRatio', 1.777)
    cmds.setAttr('defaultResolution.pixelAspect', 1)

    # Sampler settings
    cmds.setAttr('redshiftOptions.autoProgressiveRenderingIprEnabled', 1)
    cmds.setAttr('redshiftOptions.unifiedRandomizePattern', 1)

    # Motion blur settings
    cmds.setAttr('redshiftOptions.motionBlurEnable', 0)
    cmds.setAttr('redshiftOptions.motionBlurFrameDuration', 0.5)
    cmds.setAttr('redshiftOptions.motionBlurShutterStart', 0.25)
    cmds.setAttr('redshiftOptions.motionBlurShutterEnd', 0.75)
    cmds.setAttr('redshiftOptions.motionBlurShutterEfficiency', 0.5)
    cmds.setAttr('redshiftOptions.motionBlurDeformationEnable', 1)


if __name__ == '__main__':
    setDefaultRedshiftSettings()
