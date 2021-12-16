#!/usr/bin/env python
"""
rename_duplicates.py
Rename duplicate nodes in Maya.
Based on the script found here http://erwanleroy.com/maya-python-renaming-duplicate-objects/
"""

import re
import maya.cmds as cmds


def main():
    """docstring for main"""
    #Find all objects that have the same shortname as another
    #We can indentify them because they have | in the name
    duplicates = [f for f in cmds.ls(dag=True, ro=False) if '|' in f]
    #Sort them by hierarchy so that we don't rename a parent before a child.
    duplicates.sort(key=lambda obj: obj.count('|'), reverse=True)

    #if we have duplicates, rename them
    if duplicates:
        for name in duplicates:
            # extract the base name
            m = re.compile("[^|]*$").search(name)
            shortname = m.group(0)

            # extract the numeric suffix
            m2 = re.compile(".*[^0-9]").match(shortname)
            if m2:
                stripSuffix = m2.group(0)
            else:
                stripSuffix = shortname

            #rename, adding '#' as the suffix, which tells maya to find the next available number
            print "renaming {}".format(name)
            newname = cmds.rename(name, (stripSuffix + "#"))
            print "renamed {} to {}".format(name, newname)

        return "Renamed {} objects with duplicated name.".format(
            len(duplicates))
    else:
        return "No Duplicates"


if __name__ == '__main__':
    main()