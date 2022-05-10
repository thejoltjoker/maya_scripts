# list all materials and their subdivisions, file nodes(dropdown), select button
# list all subdivision settings.
# enable/disable lights. Solo light switch.
# group by lights and materials
# utility layer setup, remove lights and gi etc.
# ppos, uv and other custom aovs.
# texture input gamma.
# assign material ids and add multimattes accordingly.
# proxy manager

import maya.cmds as cmds


widgets = {}


# FIND ALL THE SUBDIVS

# list all material nodes
allMaterials = cmds.ls(mat=True)

for mat in allMaterials:
	if cmds.attributeQuery('reflectionColor', node=mat, exists=True):
		reflClr = cmds.getAttr(mat+'.reflectionColor')

	if cmds.attributeQuery('reflectionSubdivs', node=mat, exists=True) and reflClr[0] > 0:
		print(mat)
		print(cmds.getAttr(mat+'.reflectionSubdivs'))


# LIGHTS
# list all lights
# allLights = cmds.ls(lt=True)
# for light in allLights:
# 	if cmds.attributeQuery('enabled', node=light, exists=True):
# 		print cmds.getAttr(light+'.enabled')
# 		print "yes"


# OPEN VFB
def openVFB():
	cmds.vray("showVFB")

def ppAov():

	if cmds.objExists('vrayRE_PP'):
		print( "YES")
		cmds.confirmDialog( title='Confirm', message='There\'s already a Point Position pass added. Do you want to add another one?', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )

    #Add Render Element Extra_Tex
	mel.eval("vrayAddRenderElement ExtraTexElement")

	#Rename Extra_Tex
	cmds.rename("vrayRE_Extra_Tex", "vrayRE_PP")

	#Set Consider for Anti-Aliasing to 0
	cmds.getAttr("vrayRE_PP.vray_considerforaa_extratex")
	cmds.setAttr("vrayRE_PP.vray_considerforaa_extratex", 0)

	#Set Filtering to 0
	cmds.getAttr("vrayRE_PP.vray_filtering_extratex")
	cmds.setAttr("vrayRE_PP.vray_filtering_extratex", 0)

	#Set Filename suffix to "PointPosition"
	cmds.getAttr("vrayRE_PP.vray_name_extratex")
	cmds.setAttr("vrayRE_PP.vray_name_extratex", "PPos", type="string")

	#Create a Sampler Info Node
	cmds.createNode("samplerInfo", n="samplerInfo_PP")

	#Connect Sampler Info to PP
	cmds.connectAttr("samplerInfo_PP.pointWorldX", "vrayRE_PP.vray_texture_extratexR")
	cmds.connectAttr("samplerInfo_PP.pointWorldY", "vrayRE_PP.vray_texture_extratexG")
	cmds.connectAttr("samplerInfo_PP.pointWorldZ", "vrayRE_PP.vray_texture_extratexB")

	#Deselect SamplerInfo
	cmds.select("samplerInfo_PP", d=True)

	#Display Render Element PointPosition created
	om.MGlobal.displayInfo("Render Element PointPosition created")

def uvAov ():
	#Add Render Element Extra_Tex
	mel.eval("vrayAddRenderElement ExtraTexElement")

	#Rename Extra_Tex
	cmds.rename("vrayRE_Extra_Tex", "vrayRE_UV")

	#Set Consider for Anti-Aliasing to 0
	cmds.getAttr("vrayRE_UV.vray_considerforaa_extratex")
	cmds.setAttr("vrayRE_UV.vray_considerforaa_extratex", 0)

	#Set Filtering to 0
	cmds.getAttr("vrayRE_UV.vray_filtering_extratex")
	cmds.setAttr("vrayRE_UV.vray_filtering_extratex", 0)

	#Set Filename suffix to "UV"
	cmds.getAttr("vrayRE_UV.vray_name_extratex")
	cmds.setAttr("vrayRE_UV.vray_name_extratex", "UV", type="string")

	#Create a Sampler Info Node
	cmds.createNode("samplerInfo", n="samplerInfo_UV")

	#Connect Sampler Info to UV
	cmds.connectAttr("samplerInfo_UV.pointWorldX", "vrayRE_UV.vray_texture_extratexR")
	cmds.connectAttr("samplerInfo_UV.pointWorldY", "vrayRE_UV.vray_texture_extratexG")

	#Deselect SamplerInfo
	cmds.select("samplerInfo_UV", d=True)

	#Display Render Element UV created
	om.MGlobal.displayInfo("Render Element UV created")

def aoAov ():
	#Add Render Element Extra_Tex
	mel.eval("vrayAddRenderElement ExtraTexElement")

	#Rename Extra_Tex
	cmds.rename("vrayRE_Extra_Tex", "vrayRE_AO")
	cmds.setAttr("vrayRE_AO.vray_name_extratex", "AO")

	#Create VRayDirt node for AO
	cmds.createNode("VRayDirt", n="VRayDirt_AO")

	#Connect VRayDirt to extratex
	cmds.connectAttr('VRayDirt_AO'+'.outColor','vrayRE_AO'+'.vray_texture_extratex')

	om.MGlobal.displayInfo("Render Element Ambient Occlusion created")

def normalAov ():
	mel.eval("vrayAddRenderElement normalsChannel")

def beautyPass ():
	#Add Render Element Extra_Tex
	mel.eval("vrayAddRenderElement giChannel")
	mel.eval("vrayAddRenderElement lightingChannel")
	mel.eval("vrayAddRenderElement specularChannel")
	mel.eval("vrayAddRenderElement reflectChannel")
	mel.eval("vrayAddRenderElement refractChannel")
	mel.eval("vrayAddRenderElement selfIllumChannel")
	mel.eval("vrayAddRenderElement FastSSS2Channel")


# UI
def vrayManagerUI():
	if cmds.window('vrayToolsWindow', exists=True):
		cmds.deleteUI('vrayToolsWindow')

	widgets['window'] = cmds.window('vrayToolsWindow', title='Vray Tools', w=450, h=600, mxb=False, mnb=False)
	mainLayout = cmds.columnLayout(w=450, h=600)
	widgets['tabLayout'] = cmds.tabLayout(imw=5, imh=5)


	# MAIN TAB
	widgets['mainTab'] = cmds.columnLayout(w=450, h=600, parent=widgets['tabLayout'])
	cmds.tabLayout(widgets['tabLayout'], edit=True, tabLabel=(widgets['mainTab'], 'Main'))

	cmds.button(label='Open Vray Frame Buffer', command='openVFB()')


	# SUBDIV TAB
	widgets['subdivTab'] = cmds.columnLayout(w=450, h=600, parent=widgets['tabLayout'])
	cmds.tabLayout(widgets['tabLayout'], edit=True, tabLabel=(widgets['subdivTab'], 'Subdivisions'))

	cmds.text(label='Adaptive Subdivision Controls')
	widgets['vrayMinSubdivs'] = cmds.attrControlGrp(attribute = 'vraySettings.dmcMinSubdivs')
	widgets['vrayMaxSubdivs'] = cmds.attrControlGrp(attribute = 'vraySettings.dmcMaxSubdivs')
	widgets['vraySamplerThreshold'] = cmds.attrControlGrp(attribute = 'vraySettings.dmcThreshold')

	# Materials
	cmds.text(label='Materials')
	cmds.scrollLayout(w=450, h=500)

	for mat in allMaterials:
		if cmds.attributeQuery('reflectionColor', node=mat, exists=True):
			reflClr = cmds.getAttr(mat+'.reflectionColor')

		if cmds.attributeQuery('reflectionSubdivs', node=mat, exists=True) and reflClr[0] > 0:
			cmds.text(label=mat)
			cmds.columnLayout(w=450, nch=3)
			cmds.swatchDisplayPort(mat, wh=(64, 64), sn=mat)
			widgets[(mat+'_reflSubdivs_slider')] = cmds.attrFieldSliderGrp(attribute = (mat+'.reflectionSubdivs'))
			widgets[(mat+'_refrSubdivs_slider')] = cmds.attrControlGrp(attribute = (mat+'.refractionSubdivs'))


	# AOV TAB
	widgets['aovTab'] = cmds.columnLayout(w=450, h=600, parent=widgets['tabLayout'])
	cmds.tabLayout(widgets['tabLayout'], edit=True, tabLabel=(widgets['aovTab'], 'Create AOV\'s'))

	cmds.button(label='Point Position', command='ppAov()')
	cmds.button(label='UV', command='uvAov()')
	cmds.button(label='Ambient Occlusion', command='aoAov()')
	cmds.button(label='Normal', command='normalAov()')
	cmds.button(label='All beauty passes', command='beautyPass()')

	cmds.showWindow(widgets['window'])

vrayManagerUI()




# CRAP