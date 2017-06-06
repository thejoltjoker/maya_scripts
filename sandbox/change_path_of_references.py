import maya.cmds as cmds

reference_nodes = cmds.ls(references=True)
search_for = '/Volumes/macpath'
replace_with = 'P:'

for node in reference_nodes:
    id_exists = cmds.attributeQuery('fileNames', node=node, exists=True)
    if id_exists:
        print cmds.getAttr(node+'.fileNames')