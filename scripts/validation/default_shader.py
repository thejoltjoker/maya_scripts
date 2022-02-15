from maya import cmds

TITLE = 'Default Shader'
CATEGORY = 'Node'
DESCRIPTION = 'Objects that are connected to initialShadingGroup (lambert1), should have a redshift material.'


def create_material(name):
    """Create a material and return the material and shading group

    Args:
        name: The name of the new material

    Returns:
        tuple: (material, shading group)
    """
    material = cmds.shadingNode('RedshiftMaterial', name='{}_shd'.format(name), asShader=True)
    sg = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='{}_sg'.format(name))
    cmds.connectAttr('{}.outColor'.format(material), '{}.surfaceShader'.format(sg), f=True)

    return material, sg


def connect_to_sg(nodes: list, sg):
    """Connect nodes to a shading group

    Args:
        nodes: list of nodes
        sg: shading group node
    """
    for node in nodes:
        cmds.sets(node, e=True, forceElement=sg)


def connected_to_initial_shading_group():
    """Get all nodes connected to initialShadingGroup

    Returns:
        list: list of nodes connected to initialShadingGroup
    """
    connected = cmds.listConnections('initialShadingGroup')
    transforms = [x for x in connected if cmds.nodeType(x) == 'transform']
    return transforms


def check(*args):
    print('# Filebrary: Attempting to check %s' % (TITLE))

    default_shader = connected_to_initial_shading_group()

    return default_shader, len(default_shader), len(cmds.ls(tr=True))


def fix(*args):
    print('# Filebrary: Attempting to fix %s' % (TITLE))

    # Find all objects attached to default shader
    nodes = connected_to_initial_shading_group()

    # Create new material
    material, sg = create_material('default')

    # Apply material to objects
    connect_to_sg(nodes, sg)


def main():
    """docstring for main"""
    window = cmds.window(title=TITLE)
    cmds.columnLayout()
    cmds.text('Check for redshift aovs.\nFix: Remove aovs')
    cmds.button(label='Check', command=check)
    cmds.button(label='Fix', command=fix)
    cmds.setParent('..')
    cmds.showWindow(window)


if __name__ == '__main__':
    main()
