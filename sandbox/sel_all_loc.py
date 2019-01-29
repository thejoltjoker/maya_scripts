import maya.cmds as cmds

# select all locators


def selectLocators():
    selNodes = "_LOC"
    allObjs = cmds.ls()

    for obj in allObjs:
        if selNodes in obj:
            cmds.select(obj, add=True)


def selectBaked():
    selNodes = "_baked"
    allObjs = cmds.ls()

    for obj in allObjs:
        if selNodes in obj:
            cmds.select(obj)


selectLocators()

selectBaked()
