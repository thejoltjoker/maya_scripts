class hello(object):
    """docstring for hello"""
    def __init__(self):
        super(hello, self).__init__()

        ## Define path to ui file
        pathToFile = 'C:/johannes/gdrive/scripts/sequence/maya/tools/exportNulls/ui'

        ## Load our window and put it into a variable.
        qtWin = cmds.loadUI(uiFile=pathToFile)

        # Test to make sure that the UI isn't already active
        if cmds.window(qtWin, exists=True):
            cmds.deleteUI(qtWin)

        ## Open our window
        cmds.showWindow(qtWin)
