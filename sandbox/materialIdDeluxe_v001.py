import maya.cmds as cmds
import os
import os.path

new_list = []
texturePathList = []
widgets = {}

allTexturesList = cmds.ls(materials=True)
allTextures = sorted(allTexturesList)
print allTextures


def closeWin():
    if cmds.window('materialDeluxeWindow', exists=True):
        cmds.deleteUI('materialDeluxeWindow')


def selectBtn(selText):
    cmds.select(selText)

# UI


def materialDeluxeUI():
    if cmds.window('materialDeluxeWindow', exists=True):
        cmds.deleteUI('materialDeluxeWindow')

    widgets['window'] = cmds.window(
        'materialDeluxeWindow', title='Material ID Deluxe', w=600, h=600, mxb=False, mnb=False)
    mainLayout = cmds.frameLayout(w=600, h=300)

    # Materials
    widgets['gradlayout'] = cmds.gridLayout(
        numberOfColumns=2, cellWidthHeight=(300, 30), cr=True)
    for each in texturePathList:
        file_name = os.path.basename(each)
        new_list.append(file_name)

    for texture in allTextures:

        if cmds.attributeQuery('vrayMaterialId', node=texture):

            file_name = os.path.basename(texturePath)
            widgets[(texture+'_nodeTextType')] = cmds.text(label=texture +
                                                           "("+file_name+")", parent=widgets['gradlayout'])
            widgets[(texture+'_filterType')
                    ] = cmds.attrControlGrp(attribute=(texture+'.vrayMaterialId'))
            widgets[(texture+'_selectButton')] = cmds.button(label='Select node',
                                                             command='cmds.select("'+texture+'")', parent=widgets['gradlayout'])

    cmds.setParent('..')
    cmds.frameLayout(w=600, h=100, borderStyle='etchedIn')
    cmds.button(label='Close', command='closeWin()')
    cmds.showWindow(widgets['window'])


materialDeluxeUI()


# CRAP
# setAttr "wrinkles_txt.filterType" 0;
# setAttr "wrinkles_txt.filterType" 1;
