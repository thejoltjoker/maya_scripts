# GI + Lighting + Specular + Reflection + Refraction + SelfIllum + SSS = Beauty

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om


def ppAov (*args):
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

def uvAov (*args):
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

def aoAov (*args):
	#Add Render Element Extra_Tex
	mel.eval("vrayAddRenderElement ExtraTexElement")

	#Rename Extra_Tex
	cmds.rename("vrayRE_Extra_Tex", "vrayRE_AO")

	#Create VRayDirt node for AO
	cmds.createNode("VRayDirt", n="VRayDirt_AO")

	#Connect VRayDirt to extratex
	cmds.connectAttr('VRayDirt_AO'+'.outColor','vrayRE_AO'+'.vray_texture_extratex')

	setAttr -type "string" vrayRE_AO.vray_name_extratex `textField -q -tx MayaWindow|MainAttributeEditorLayout|formLayout2|AEmenuBarLayout|AErootLayout|AEStackLayout|AErootLayoutPane|AEbaseFormLayout|AEcontrolFormLayout|AttrEdVRayRenderElementFormLayout|scrollLayout2|columnLayout18|frameLayout40|vrayAEMasterColumnLayout|vrayExtraTexChannel_VRayRenderElement|vray_name_extratex_VRayRenderElement_row|vray_name_extratex_VRayRenderElement`;

	# createRenderNode -textures "defaultNavigation -force true -connectToExisting -source %node -destination vrayRE_Extra_Tex.vray_texture_extratex" "";
	# defaultNavigation -defaultTraversal -destination "vrayRE_Extra_Tex.vray_texture_extratex";
	# shadingNode -asTexture VRayDirt;
	# // Result: VRayDirt1 // 
	# shadingNode -asUtility place2dTexture;
	# // Result: place2dTexture1 // 
	# connectAttr place2dTexture1.outUV VRayDirt1.uv;
	# // Result: Connected place2dTexture1.outUV to VRayDirt1.uvCoord. // 
	# connectAttr place2dTexture1.outUvFilterSize VRayDirt1.uvFilterSize;
	# // Result: Connected place2dTexture1.outUvFilterSize to VRayDirt1.uvFilterSize. // 
	# defaultNavigation -force true -connectToExisting -source VRayDirt1 -destination vrayRE_Extra_Tex.vray_texture_extratex; window -e -vis false createRenderNodeWindow;
	# connectAttr -force VRayDirt1.outColor vrayRE_Extra_Tex.vray_texture_extratex;
	# // Result: Connected VRayDirt1.outColor to vrayRE_Extra_Tex.vray_texture_extratex. // 
	# // Result: createRenderNodeWindow // 
	# rename VRayDirt1 "ao" ;
	# // Result: ao // 

	om.MGlobal.displayInfo("Render Element Ambient Occlusion created")

def normalAov (*args):
	mel.eval("vrayAddRenderElement normalChannel")

def beautyPass (*args):
	#Add Render Element Extra_Tex
	mel.eval("vrayAddRenderElement giChannel")
	mel.eval("vrayAddRenderElement lightingChannel")
	mel.eval("vrayAddRenderElement specularChannel")
	mel.eval("vrayAddRenderElement reflectChannel")
	mel.eval("vrayAddRenderElement refractChannel")
	mel.eval("vrayAddRenderElement selfIllumChannel")
	mel.eval("vrayAddRenderElement FastSSS2Channel")

# Define an id string for the window first
winID = 'aovUI'

# Test to make sure that the UI isn't already active
if cmds.window(winID, exists=True):
    cmds.deleteUI(winID)
    
# Now create a fresh UI window
cmds.window(winID)

# Add a Layout - a columnLayout stacks controls vertically
cmds.columnLayout()

# Add controls into this Layout
#whatUSay = cmds.textField()
cmds.button(label='Point Position', command='ppAov()')
cmds.button(label='UV', command='uvAov()')
cmds.button(label='Ambient Occlusion', command='aoAov()')
cmds.button(label='Ambient Occlusion', command='normalAov()')
cmds.button(label='All beauty passes', command='beautyPass()')

# Display the window
cmds.showWindow()









import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om

#Add Render Element Extra_Tex
mel.eval("vrayAddRenderElement ExtraTexElement")

#Rename Extra_Tex
cmds.rename("vrayRE_Extra_Tex", "vrayRE_Extra_Tex_UV")

#Set Consider for Anti-Aliasing to 0
cmds.getAttr("vrayRE_Extra_Tex_UV.vray_considerforaa_extratex")
cmds.setAttr("vrayRE_Extra_Tex_UV.vray_considerforaa_extratex", 0)

#Set Filtering to 0
cmds.getAttr("vrayRE_Extra_Tex_UV.vray_filtering_extratex")
cmds.setAttr("vrayRE_Extra_Tex_UV.vray_filtering_extratex", 0)

#Set Filename suffix to "UV"
cmds.getAttr("vrayRE_Extra_Tex_UV.vray_name_extratex")
cmds.setAttr("vrayRE_Extra_Tex_UV.vray_name_extratex", "UV", type="string")

#Create a Sampler Info Node
cmds.createNode("samplerInfo", n="samplerInfo_UV")

#Connect Sampler Info to UV
cmds.connectAttr("samplerInfo_UV.uCoord", "vrayRE_Extra_Tex_UV.vray_texture_extratexR")
cmds.connectAttr("samplerInfo_UV.vCoord", "vrayRE_Extra_Tex_UV.vray_texture_extratexG")

#Deselect SamplerInfo
cmds.select("samplerInfo_UV", d=True)

#Display Render Element UV created
om.MGlobal.displayInfo("Render Element UV created")