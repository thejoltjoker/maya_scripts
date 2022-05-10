import maya.cmds as cmds
import os
import os.path
import maya.mel as mel
import time
import math

new_list = []
texturePathList = []
widgets = {}

allTexturesList = cmds.ls(tex=True)
allTextures = sorted(allTexturesList)
print allTextures


# UI
def textureToolsOldUI():
	if cmds.window('textureToolsWindow', exists=True):
		cmds.deleteUI('textureToolsWindow')

	widgets['window'] = cmds.window('textureToolsWindow', title='Texture Tools', w=600, h=600, mxb=False, mnb=False)
	mainLayout = cmds.frameLayout(w=600, h=300)

	# Materials
	cmds.gridLayout( numberOfColumns=2, cellWidthHeight=(300, 30), cr=True )
	for each in texturePathList:
	    file_name = os.path.basename(each)
	    new_list.append(file_name)

	for texture in allTextures:

		if cmds.nodeType(texture) == 'file':
			texturePath = cmds.getAttr(texture+".fileTextureName")
			file_name = os.path.basename(texturePath)
			widgets[(texture+'_nodeTextType')] =cmds.text(label=texture+"("+file_name+")")
			widgets[(texture+'_filterType')] = cmds.attrControlGrp(attribute = (texture+'.filterType'))
			widgets[(texture+'_selectButton')] = cmds.button(label='Select node', command='selectBtn()')
	cmds.setParent( '..' )
	cmds.frameLayout(w=600, h=100, borderStyle='etchedIn')
	cmds.button(label='Open Vray Frame Buffer', command='openVFB()')
	cmds.button(label='Reload all textures', command='reloadTextures()')
	cmds.button(label='Delete unused nodes', command='deleteNodes()')
	cmds.button(label = 'Close', command ='closeWin()')
	cmds.showWindow(widgets['window'])




def textureToolsUI():

	if cmds.dockControl('ttoolsDock',exists=1):
		cmds.deleteUI('ttoolsDock')

	# window and mainLayout
	widgets['window'] = cmds.window()


	# MAIN LAYOUT
	cmds.scrollLayout(cr=1)
	widgets['mainLayout'] = cmds.columnLayout(adj=1)



	# GENERAL FRAMELAYOUT
	widgets['frameLayout_01'] = cmds.frameLayout(label='General', collapsable=1, w=300, bs='etchedIn',mh=0,parent=widgets['mainLayout'])
	widgets['formLayout_01'] = cmds.formLayout(parent=widgets['frameLayout_01'])
	
	widgets['descriptionSubdivs'] = cmds.text( label='General goodness',w=315,h=20,fn='boldLabelFont',bgc=(0.15,0.15,0.15))
	widgets['sepBottom'] = cmds.separator( w=315,height=2, style='out' )

	# Button with function call
	widgets['subBtn'] = cmds.button(l='Set',w=60,h=21,command='openVFB()')

	##############################
	# SHOW UI
	##############################
	# Refresh bug?
	cmds.dockControl('dockControl1', e=1, r=1)
	

	# Show Dock Window
	widgets['dockPanel'] = cmds.dockControl('ttoolsDock',label='Texture Tools',area='right',w=326,content=widgets['window'],aa='right',sizeable=0)
	cmds.dockControl('ttoolsDock',e=1,r=1)


##############################
# FUNCTIONS
##############################

def openVFB():
	cmds.vray("showVFB")

def reloadTextures():
	# Reload file nodes

	for texture in allTextures:

		if cmds.nodeType(texture) == 'file':

			texturePath = cmds.getAttr(texture+".fileTextureName")
			texturePathList.append(texturePath)
			cmds.setAttr(texture+".fileTextureName", texturePath, type='string')
		
			print "Reloaded "+texture+" with "+texturePath

def deleteNodes():
	# Delete unused nodes
	mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')

def closeWin():
	if cmds.window('textureToolsWindow', exists=True):
		cmds.deleteUI('textureToolsWindow')

def selectBtn():
	cmds.select(texture)



# OPEN UI
textureToolsUI()

