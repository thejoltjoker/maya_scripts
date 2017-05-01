import os
import maya.cmds as cmds

def testSubmit():
    mayapy_location = 'C:/Program Files/Autodesk/Maya2016/bin/mayapy.exe'
    script = 'D:/people/johannes/scripts/repos/sequence/maya/tools/clayblast/test03.py'
    testVariable = 'test'
    command = '"%s" "%s" "%s"' %(mayapy_location, script, testVariable)
    os.system('"' + command + '"')
testSubmit()