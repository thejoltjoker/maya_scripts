#!/usr/bin/env python3
""".py
Description of .py.
"""
import maya.cmds as mc


def node_exists(keywords, case_sensitive=True):
    """Checks if a node contains a list of keywords

    Args:
        keywords (list): list of keywords
        case_sensitive (object): whether the check should be case sensitive

    Returns:
        bool: True if node exists, else False
    """
    existing_keywords = []
    for node in mc.ls(r=True):
        existing_keywords = []
        for kw in keywords:
            if case_sensitive:
                if kw in node:
                    existing_keywords.append(kw)
            else:
                if kw.lower() in node.lower():
                    existing_keywords.append(kw)
    return len(existing_keywords) == len(keywords)


def camera_exists(shot):
    """Check if a camera exists with the given shot name"""
    for node in mc.ls(tr=True, r=True):
        children = mc.listRelatives(node, ad=True, typ='camera')
        if children:
            for cam in children:
                if shot in cam:
                    return True
    return False


def light_exists(shot):
    """Check if a light exists with the given shot name"""
    for node in mc.ls(tr=True, r=True):
        children = mc.listRelatives(node, ad=True)
        if children:
            for child in children:
                if 'light' in mc.nodeType(child).lower():
                    if shot in child:
                        return True
    return False


def set_exists(shot):
    """Check if a set exists with the given shot name"""
    for node in mc.ls(set=True, r=True):
        if shot in node:
            return True
    return False


def sequence_exists(shot):
    """Check if a sequence exists with the given shot name"""
    for node in mc.ls(type='shot', r=True):
        if shot in node:
            return True
    return False


def main():
    """docstring for main"""
    shot = 's010'
    print(camera_exists(shot))
    print(set_exists(shot))
    print(sequence_exists(shot))
    print(light_exists(shot))
    print(node_exists([shot, 'group']))


if __name__ == '__main__':
    main()
