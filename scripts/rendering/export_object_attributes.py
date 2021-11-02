#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
export_object_attributes.py
Description of export_object_attributes.py.
"""
import maya.cmds as cmds
import json

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
export_object_attributes.py
Description of export_object_attributes.py.
"""

# def list_textures():
#     """docstring for main"""
#     materials = cmds.ls(mat=True)
#     dict = {}
#     for mat in materials:
#         dict[mat] = {}
#         dict[mat]['type'] = cmds.nodeType(mat)
#         dict[mat]['maps'] = {}
#         in_conn = cmds.listConnections(
#             mat, s=True, d=False, c=True, scn=True, t='file')
#         if in_conn is not None:
#             for n, node in enumerate(in_conn):
#                 if n % 2 == 0:
#                     dict[mat]['maps'][node] = cmds.getAttr(
#                         '{}.fileTextureName'.format(in_conn[n + 1]))
#                 else:
#                     pass  # Odd
#     # return json.dumps(dict)
#     return dict


def save_to_file(data):
    scene_path = cmds.file(sn=True, q=True)
    directory = os.path.abspath(os.path.join(
        os.path.dirname(scene_path), 'exports'))

    if not os.path.exists(directory):
        os.makedirs(directory)

    attributes_file = os.path.join(directory,
                                   '{}_attributes.json'.format(os.path.splitext(os.path.basename(scene_path))[0]))

    with open(attributes_file, 'w') as outfile:
        json.dump(data, outfile)


def main():
    """docstring for main"""
    attributes = {}
    sel = cmds.ls(sl=1)
    for obj in sel:

        attributes[obj] = {}
        for a in cmds.listAttr(obj, hd=1):

            try:
                attributes[obj][a] = cmds.getAttr(obj+'.'+a)
            except:
                pass

    save_to_file(attributes)


if __name__ == '__main__':
    main()
