#!/usr/bin/env python3
"""list_references_scenes.py
Description of list_references_scenes.py.
"""
from maya import cmds


def get_referenced_scenes():
    scenes = []
    reference_nodes = cmds.ls(references=True)
    for node in reference_nodes:
        path = cmds.referenceQuery(node, filename=True)
        scenes.append(path)
    return scenes


if __name__ == '__main__':
    print(get_referenced_scenes())
