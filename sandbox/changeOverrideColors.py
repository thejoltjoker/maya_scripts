import maya.cmds as cmds

# selObj = cmds.ls(sl=True)

# for node in selObj:
for node in cmds.ls():
	if node.endswith('_ctrl'):
		cmds.setAttr(node+".overrideEnabled",1)
		
		# Red color if it's the right side
		if node.startswith('r_'):
			cmds.setAttr(node+".overrideColor",13)
		# Other blue color for offset
			if node.endswith('Offset_ctrl'):
				cmds.setAttr(node+".overrideColor",20)

		# Blue color if it's the left side
		elif node.startswith('l_'):
			cmds.setAttr(node+".overrideColor",6)
		# Other blue color for offset
			if node.endswith('Offset_ctrl'):
				cmds.setAttr(node+".overrideColor",18)
		
		else:
			cmds.setAttr(node+".overrideColor",17)

			# Other yellow color for offset
			if node.endswith('Offset_ctrl'):
				cmds.setAttr(node+".overrideColor",21)