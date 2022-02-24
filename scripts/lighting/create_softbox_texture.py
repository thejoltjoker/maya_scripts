"""create_softbox_texture.py
Description of create_softbox_texture.py.
"""
from maya import cmds


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


def main():
    """docstring for main"""
    # redshiftCreateLight "RedshiftPhysicalLight";

    for node in cmds.ls(sl=True):
        if cmds.nodeType(node) == 'RedshiftPhysicalLight':
            shapes = [node]
        else:
            shapes = cmds.listRelatives(node)

        for shape in shapes:
            if cmds.nodeType(shape) == 'RedshiftPhysicalLight':
                softbox_texture = create_softbox_texture()
                cmds.connectAttr(softbox_texture + '.outColor', shape + '.color', force=True)
    pass


if __name__ == '__main__':
    main()
