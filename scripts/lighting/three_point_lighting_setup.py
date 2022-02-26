#!/usr/bin/env python3
""".py
Description of .py.
"""
import random

from maya import mel, cmds


def create_softbox_texture():
    # Create ramp node and change settings
    node_ramp = cmds.shadingNode('ramp', asTexture=True)
    cmds.setAttr(node_ramp + '.type', 6)  # UV box
    cmds.setAttr(node_ramp + '.interpolation', 2)  # Exponential up
    # Set colors
    cmds.setAttr(node_ramp + '.colorEntryList[0].position', 0)
    cmds.setAttr(node_ramp + '.colorEntryList[1].position', 1)
    cmds.setAttr(node_ramp + '.colorEntryList[0].color', 1, 1, 1, type='double3')
    cmds.setAttr(node_ramp + '.colorEntryList[1].color', 0, 0, 0, type='double3')

    # Create placement node
    node_2d_texture = cmds.shadingNode('place2dTexture', asUtility=True)

    # Add some noise for realism
    cmds.setAttr(node_2d_texture + '.noiseU', 0.003)
    cmds.setAttr(node_2d_texture + '.noiseV', 0.003)

    # Connect ramp to placement node
    cmds.connectAttr(node_2d_texture + '.outUV', node_ramp + '.uv')
    cmds.connectAttr(node_2d_texture + '.outUvFilterSize', node_ramp + '.uvFilterSize')

    return node_ramp


def create_physical_light(name='myLight', suffix='lgt'):
    light = cmds.shadingNode("RedshiftPhysicalLight", asLight=1)
    if name:
        light = cmds.rename(light, name + '_' + suffix)

    # Connect texture
    softbox_texture = create_softbox_texture()
    cmds.connectAttr(softbox_texture + '.outColor', light + '.color', force=True)

    # Set mode to temperature and color
    cmds.setAttr(light + ".colorMode", 2)
    cmds.setAttr(light + ".temperature", 5500)
    return light


def create_locator(name='myLocator', color=None, suffix='loc'):
    locator = cmds.spaceLocator(name=name + '_' + suffix)[0]
    if color:
        cmds.setAttr(locator + '.overrideEnabled', 1)
        cmds.setAttr(locator + '.overrideColor', color)
    return locator


def create_offset(name='myOffset', color=None, suffix='ctrl'):
    # offset = mel.eval(
    #     'curve -d 1 -p -1 1.5 0 -p -1.25 1.75 0 -p -1.75 1.25 0 -p -1.5 1 0 -p -1.5 -1 0 -p -1.75 -1.25 0 -p -1.25 -1.75 0 -p -1 -1.5 0 -p 1 -1.5 0 -p 1.25 -1.75 0 -p 1.75 -1.25 0 -p 1.5 -1 0 -p 1.5 1 0 -p 1.75 1.25 0 -p 1.25 1.75 0 -p 1 1.5 0 -p -1 1.5 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;')
    offset = mel.eval(
        'curve -d 1 -p -1.5 1.5 0 -p -1.5 -1.5 0 -p 1.5 -1.5 0 -p 1.5 1.5 0 -p -1.5 1.5 0 -k 0 -k 1 -k 2 -k 3 -k 4 ;')
    offset = cmds.rename(offset, name + '_' + suffix)
    if color:
        cmds.setAttr(offset + '.overrideEnabled', 1)
        cmds.setAttr(offset + '.overrideColor', color)

    return offset


def create_annotation(node, name, coord=(0, 1.25, 0)):
    annotation = cmds.annotate(node, tx=name, p=coord)
    annotation = cmds.listRelatives(p=True)
    annotation = cmds.rename(annotation, name + 'Label')
    return annotation


def create_single_light_rig(name='myLight', color=None, label_coord=(0, 1.25, 0)):
    if not color:
        color = random.randint(0, 31)
    # Create light
    light = create_physical_light(name)
    light_shape = cmds.listRelatives(light, shapes=True)[0]
    # cmds.move(0, 0, 0.25, light)
    # cmds.makeIdentity(light, apply=True)

    # Create offset control
    offset = create_offset(name + 'Offset', color=color)
    offset_shape = cmds.listRelatives(offset, shapes=True)[0]

    # Parent light to offset
    cmds.parent(light, offset)

    # Create locator
    locator = create_locator(name + 'Control', color=color, suffix='ctrl')

    # Parent offset to locator
    cmds.parent(offset, locator)

    # Create label
    annotation = create_annotation(locator, name, coord=label_coord)

    # Parent annotation to locator
    cmds.parent(annotation, locator)

    # Create and connect attributes
    attr_offset = 'offset'
    cmds.addAttr(light, ln=attr_offset, at='bool', dv=False, k=True)
    cmds.connectAttr('.'.join([light, attr_offset]), offset_shape + '.visibility', f=True)

    attr_enable = name + 'Enable'
    cmds.addAttr(locator, ln=attr_enable, at='bool', dv=True, k=True)
    cmds.connectAttr('.'.join([locator, attr_enable]), light_shape + '.on', f=True)

    attr_visible = name + 'Visible'
    cmds.addAttr(locator, ln=attr_visible, at='bool', dv=False, k=True)
    cmds.connectAttr('.'.join([locator, attr_visible]), light_shape + '.areaVisibleInRender', f=True)

    attr_intensity = name + 'Intensity'
    cmds.addAttr(locator, ln=attr_intensity, at='double', dv=100, k=True)
    cmds.connectAttr('.'.join([locator, attr_intensity]), light_shape + '.intensity', f=True)

    attr_exposure = name + 'Exposure'
    cmds.addAttr(locator, ln=attr_exposure, at='double', k=True)
    cmds.connectAttr('.'.join([locator, attr_exposure]), light_shape + '.exposure', f=True)

    attr_distance = name + 'Distance'
    cmds.addAttr(locator, ln=attr_distance, at='double', dv=10, k=True)
    cmds.connectAttr('.'.join([locator, attr_distance]), offset + '.translateZ', f=True)

    attr_size = name + 'Size'
    cmds.addAttr(locator, ln=attr_size, at='double', dv=1, k=True)
    cmds.connectAttr('.'.join([locator, attr_size]), offset + '.scaleX', f=True)
    cmds.connectAttr('.'.join([locator, attr_size]), offset + '.scaleY', f=True)
    cmds.connectAttr('.'.join([locator, attr_size]), offset + '.scaleZ', f=True)

    return locator


def main():
    """docstring for main"""
    # Create light
    # Add parent controller

    key_light = create_single_light_rig('keyLight', color=22, label_coord=(0, 1.25, 0))
    cmds.rotate(-30, -45, 0,key_light)
    fill_light = create_single_light_rig('fillLight', color=23, label_coord=(0, 1, 0))

    cmds.rotate(-30, 45, 0, fill_light)
    cmds.setAttr(fill_light+'.fillLightExposure', -1)

    rim_light = create_single_light_rig('rimLight', color=24, label_coord=(0, .75, 0))
    cmds.rotate(-30, -135, 0, rim_light)


if __name__ == '__main__':
    main()
