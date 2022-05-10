#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
incremental_save.py
Description of incremental_save.py.
"""
import maya.standalone
import maya.cmds as cmds
import os
import re


def incremental_save():
    """docstring for incremental_save"""
    cur_scene_path = cmds.file(sn=True, q=True)
    cur_scene_name = os.path.basename(cur_scene_path)
    print(cur_scene_name)
    cur_scene_folder = os.path.dirname(cur_scene_path)
    print(cur_scene_folder)

    # Find version in filename
    regex = r"_v\d+"

    cur_scene_version = re.findall(regex, cur_scene_name)[0]
    print(cur_scene_version)
    cur_scene_version_int = int(cur_scene_version[2:])
    print(cur_scene_version_int)

    scene_versions = os.listdir(cur_scene_folder)
    print(scene_versions)

    new_scene_version_int = cur_scene_version_int + 1
    print(new_scene_version_int)
    new_scene_version = "_v{:03d}".format(new_scene_version_int)
    new_scene_name = cur_scene_name.replace(
        cur_scene_version, new_scene_version)
    print(new_scene_name)

    while new_scene_name in scene_versions:
        print("{} already exists in folder. Versioning up.".format(new_scene_name))
        new_scene_version_int = new_scene_version_int + 1
        new_scene_version = "_v{:03d}".format(new_scene_version_int)
        new_scene_name = cur_scene_name.replace(
            cur_scene_version, new_scene_version)
        print(new_scene_name)

    # Save new file
    cmds.file(rename=os.path.join(cur_scene_folder,
                                  new_scene_name))
    cmds.file(save=True)
    print("File saved as {}".format(
        os.path.join(cur_scene_folder, new_scene_name)))


def main():
    incremental_save()


if __name__ == '__main__':
    maya.standalone.initialize()
    cmds.file(r'C:\Users\thejoltjoker\Desktop\scene_v002.ma', open=True)
    incremental_save()
    maya.standalone.uninitialize()

# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# """
# incremental_save.py
# Description of incremental_save.py.
# """
# import os

# import maya.cmds as cmds


# def incremental_save():
#     """docstring for incremental_save"""
#     scene_name = cmds.file(q=True, sn=True)

#     # Find version in filename
#     regex = r"_[v]\d\d\d"
#     current_version_match = re.findall(regex, scene_name)[0]

#     current_version =
#     new_version = current_version + 1
#     new_scene_name = scene_name.replace(
#         matches[0], '_v{:03d}'.format(new_version))

#     new_file = os.path.isfile(new_scene_name)

#     while new_file:
#         new_version = current_version + 1

#         new_scene_name = scene_name.replace(
#             matches[0], '_v{:03d}'.format(new_version))

#         new_file = os.path.isfile(new_scene_name)

#     print(new_scene_name)


# incremental_save()


# # if __name__ == '__main__':
# #     incremental_save()
