#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import os
import maya.cmds as cmds

SUFFIXES = {'RedshiftCurvature': 'rsCurvature',
            'RedshiftMatteParameters': 'rsMatteParameters',
            'RedshiftCurveSet': 'rsCurveSet',
            'RedshiftDomeLight': 'lgt',
            'RedshiftIESLight': 'lgt',
            'RedshiftMeshParameters': 'rsMeshParameters',
            'RedshiftObjectId': 'rsObjectId',
            'RedshiftOptions': 'RedshiftOptions',
            'RedshiftPhysicalLight': 'lgt',
            'RedshiftPortalLight': 'lgt',
            'RedshiftPostEffects': 'rsPostEffects',
            'RedshiftTraceSet': 'rsTraceSet',
            'RedshiftVisibility': 'rsVisibility',
            'RedshiftVolumeShape': 'rsVolumeShape',
            'ambientLight': 'lgt',
            'areaLight': 'lgt',
            'camera': 'cam',
            'colorManagementGlobals': 'colorManagementGlobals',
            'defaultLightList': 'defaultLightList',
            'defaultRenderUtilityList': 'defaultRenderUtilityList',
            'defaultRenderingList': 'defaultRenderingList',
            'defaultShaderList': 'defaultShaderList',
            'defaultTextureList': 'defaultTextureList',
            'directionalLight': 'lgt',
            'displayLayer': 'displayLayer',
            'displayLayerManager': 'displayLayerManager',
            'dof': 'dof',
            'dynController': 'dynController',
            'globalCacheControl': 'globalCacheControl',
            'group': 'grp',
            'hardwareRenderGlobals': 'hardwareRenderGlobals',
            'hardwareRenderingGlobals': 'hardwareRenderingGlobals',
            'hikSolver': 'hikSolver',
            'hwRenderGlobals': 'hwRenderGlobals',
            'hyperGraphInfo': 'hyperGraphInfo',
            'hyperLayout': 'hyperLayout',
            'ikRPsolver': 'ikRPsolver',
            'ikSCsolver': 'ikSCsolver',
            'ikSplineSolver': 'ikSplineSolver',
            'ikSystem': 'ikSystem',
            'lambert': 'lambert',
            'lightLinker': 'lightLinker',
            'lightList': 'lightList',
            'locator': 'locator',
            'lookAt': 'lookAt',
            'makeNurbSphere': 'makeNurbSphere',
            'materialInfo': 'materialInfo',
            'mesh': 'geo',
            'nurbsCurve': 'crv',
            'nurbsSurface': 'nurbsSurface',
            'objectMultiFilter': 'objectMultiFilter',
            'objectNameFilter': 'objectNameFilter',
            'objectSet': 'objectSet',
            'particleCloud': 'particleCloud',
            'partition': 'partition',
            'pointLight': 'lgt',
            'polySphere': 'polySphere',
            'poseInterpolatorManager': 'poseInterpolatorManager',
            'postProcessList': 'postProcessList',
            'renderGlobals': 'renderGlobals',
            'renderGlobalsList': 'renderGlobalsList',
            'renderLayer': 'renderLayer',
            'renderLayerManager': 'renderLayerManager',
            'renderQuality': 'renderQuality',
            'renderSphere': 'renderSphere',
            'resolution': 'resolution',
            'sequenceManager': 'sequenceManager',
            'shaderGlow': 'shaderGlow',
            'shadingEngine': 'shadingEngine',
            'shapeEditorManager': 'shapeEditorManager',
            'spotLight': 'lgt',
            'standardSurface': 'standardSurface',
            'strokeGlobals': 'strokeGlobals',
            'time': 'time',
            'RedshiftMaterial': 'shd',
            'transform': 'transform',
            'viewColorManager': 'viewColorManager',
            'volumeFog': 'volumeFog',
            'volumeLight': 'lgt'}


def name_from_connections(node):
    for n in cmds.ls(sl=True):
        print(cmds.listConnections(n))


def name_from_filename(node):
    if cmds.nodeType(node) == 'file':
        texturePath = cmds.getAttr(node + ".fileTextureName")
        filenameExt = os.path.basename(texturePath)
        filename = os.path.splitext(filenameExt)[0] + '_FILE'
        cmds.rename(node, filename)


def get_suffix(node):
    print(node)
    node_type = cmds.nodeType(node)
    if node_type == 'transform':
        node_shapes = cmds.listRelatives(node, s=True, path=True)
        if node_shapes is not None:
            for shape in node_shapes:
                node_type = cmds.nodeType(shape)
        else:
            node_type = 'group'
    return SUFFIXES.get(node_type, node_type)


def increment_name(name, suffix):
    inc = 1
    while True:
        new_name = '{name}{inc:03d}_{suffix}'.format(name=name, inc=inc, suffix=suffix)
        if not cmds.objExists(new_name):
            return new_name
        inc += 1


def clean_name(name):
    return name.replace(' ', '_')


def rename_selection(name):
    renamed = []
    # Get selection and sort it
    nodes = cmds.ls(sl=True, l=True)
    sorted_sel = sorted(nodes, key=len, reverse=True)

    # Loop through selected objects
    for node in sorted_sel:
        print('Renaming {0}'.format(node))
        suffix = get_suffix(node)

        if len(sorted_sel) > 1:
            new_name = increment_name(name, suffix)
        else:
            new_name = '_'.join([name, suffix])
            if cmds.objExists(new_name):
                new_name = increment_name(name, suffix)

        # Rename nodes
        renamed_node = cmds.rename(node, new_name)
        renamed.append(renamed_node)

    return renamed


def blank_rename():
    # Get selection
    renamed = []
    sel = cmds.ls(sl=True)

    # Loop through selected objects
    for node in sel:
        node_type = cmds.nodeType(node)
        suffix = get_suffix(node)
        name = name_from_connections(node)

        if len(sel) > 1:
            new_name = increment_name(name, suffix)
        else:
            new_name = '_'.join([name, suffix])
            if cmds.objExists(new_name):
                new_name = increment_name(name, suffix)

        # Rename nodes
        renamed_node = cmds.rename(node, new_name)
        renamed.append(renamed_node)
    return renamed


def main():
    name_dialog = cmds.promptDialog(
        title='Rename',
        message='Enter new name:',
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel')

    if name_dialog == 'OK':
        name = cmds.promptDialog(query=True, text=True)
        if name:
            rename_selection(name)
        else:
            cmds.warning("The name can't be blank")
    else:
        print('User cancelled renaming')


if __name__ == '__main__':
    main()
