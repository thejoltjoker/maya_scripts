"""
constrain_and_delete.py
"""


def constrain_and_delete():
    import maya.cmds as cmds
    cmds.pointConstraint(w=1, mo=False)
    cmds.orientConstraint(w=1, mo=False)
    cmds.delete(cn=True)


if __name__ == "__main__":
    constrain_and_delete()
