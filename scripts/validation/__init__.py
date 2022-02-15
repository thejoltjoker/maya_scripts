from maya import cmds


def validator_window(title, check_cmd, fix_cmd):
    """docstring for main"""
    window = cmds.window(title=title)
    cmds.columnLayout()
    cmds.text('Check for redshift aovs.\nFix: Remove aovs')
    cmds.button(label='Check', command=check_cmd)
    cmds.button(label='Fix', command=fix_cmd)
    cmds.setParent('..')
    cmds.showWindow(window)
