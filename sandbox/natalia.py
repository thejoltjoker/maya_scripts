import maya.cmds as mc


def process_group_structure(structure, parent=None):
    groups = []
    group = None
    nodes = mc.ls()
    name = structure.get('name')
    color = structure.get('color')

    # Check if group exists already
    for node in nodes:
        if node == name:
            group = node

    # Create new if it doesn't
    if not group:
        if parent:
            group = mc.group(p=parent, n=name, em=True)
        else:
            group = mc.group(n=name, em=True)

        # Set color in outliner
        if color:
            mc.setAttr(f'{group}.useOutlinerColor', True)
            mc.setAttr(f'{group}.outlinerColor', *color)

    # Add to list of groups
    groups.append(group)

    # Create children groups
    for child in structure.get("children", []):
        groups.extend(process_group_structure(child, parent=group))

    return groups


def turbo_create_default_groups():
    """Checks the scene for default groups and creates them if they don't exist"""
    group_nodes = []
    groups = [
        {
            'name': 'cameras',
            'color': (0.545, 0.737, 1)
        },
        {
            'name': 'generic',
            'children': [{
                'name': 'scene_lights',
                'color': (1, 0.629, 0)
            }]
        }
    ]

    # Create or get groups
    for g in groups:
        group_nodes.extend(process_group_structure(g))

    return group_nodes


def main():
    print(turbo_create_default_groups())


if __name__ == '__main__':
    main()
