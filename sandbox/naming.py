import maya.cmds as cmds
print '// Renaming joints'
#joint
for node in cmds.ls(type='joint'):
    if not node.endswith('_jnt'):

        #print node+'_jnt'
        cmds.rename(node, node+'_jnt')

        print node+' was renamed to '+node+'_jnt'


print ''
print ''
print ''

print '// Renaming ik'
#ikHandle
for node in cmds.ls(type='ikHandle'):
    if not node.endswith('_ik'):

        #print node+'_ik'
        cmds.rename(node, node+'_ik')

        print node+' was renamed to '+node+'_ik'


print ''
print ''
print ''

print '// Renaming blend color'
#blendColor
for node in cmds.ls(type='blendColors'):
    if not node.endswith('_color'):

        #print node+'_color'
        cmds.rename(node, node+'_color')

        print node+' was renamed to '+node+'_color'


print ''
print ''
print ''

print '// Renaming skin cluster'
#skinCluster
for node in cmds.ls(type='skinCluster'):
    if not node.endswith('_skin'):

        #print node+'_skin'
        cmds.rename(node, node+'_skin')

        print node+' was renamed to '+node+'_skin'


print ''
print ''
print ''

print '// Renaming ikEffector'
#ikEffector
for node in cmds.ls(type='ikEffector'):
    if not node.endswith('_eff'):

        #print node+'_eff'
        cmds.rename(node, node+'_eff')

        print node+' was renamed to '+node+'_eff'


print ''
print ''
print ''

print '// Renaming constraints'
#pointConstraint
for node in cmds.ls(type='pointConstraint'):
    if not cmds.nodeType(node) == 'poleVectorConstraint':
        if node.endswith('_pointConstraint1'):

            #print node[:-17]+'_pointCnst'
            cmds.rename(node, node[:-17]+'_pointCnst')

            print node+' was renamed to '+node[:-17]+'_pointCnst'

        elif node.endswith('_pointConstraint'):

            #print node[:-16]+'_pointCnst'
            cmds.rename(node, node[:-16]+'_pointCnst')

            print node+' was renamed to '+node[:-16]+'_pointCnst'

        elif node.endswith('_pointCnst_pointCnst'):

            #print node+'_pointCnst'
            cmds.rename(node, node[:-20]+'_pointCnst')

            print node+' was renamed to '+node[:-20]+'_pointCnst'

        elif not node.endswith('_pointCnst'):

            #print node+'_pointCnst'
            cmds.rename(node, node+'_pointCnst')

            print node+' was renamed to '+node+'_pointCnst'

#poleVectorConstraint
for node in cmds.ls(type='pointConstraint'):
    if cmds.nodeType(node) == 'poleVectorConstraint':
        if node.endswith('_poleVectorConstraint1'):

            #print node[:-22]+'_poleCnst'
            cmds.rename(node, node[:-22]+'_poleCnst')

            print node+' was renamed to '+node[:-22]+'_poleCnst'

        elif node.endswith('_poleVectorConstraint'):

            #print node[:-21]+'_poleCnst'
            cmds.rename(node, node[:-21]+'_poleCnst')

            print node+' was renamed to '+node[:-21]+'_poleCnst'

        elif node.endswith('_poleCnst_poleCnst'):

            #print node[:-18]+'_poleCnst'
            cmds.rename(node, node[:-18]+'_poleCnst')

            print node+' was renamed to '+node[:-18]+'_poleCnst'

        elif not node.endswith('_poleCnst'):

            cmds.rename(node, node+'_poleCnst')

            print node+' was renamed to '+node+'_poleCnst'

#orientConstraint
for node in cmds.ls(type='orientConstraint'):
    if node.endswith('_orientConstraint1'):

        #print node[:-18]+'_orientCnst'
        cmds.rename(node, node[:-18]+'_orientCnst')

        print node+' was renamed to '+node[:-18]+'_orientCnst'

    elif node.endswith('_orientConstraint'):

        #print node[:-17]+'_orientCnst'
        cmds.rename(node, node[:-17]+'_orientCnst')

        print node+' was renamed to '+node[:-17]+'_orientCnst'

    elif node.endswith('_orientCnst_orientCnst'):

        #print node[:-22]+'_orientCnst'
        cmds.rename(node, node[:-22]+'_orientCnst')

        print node+' was renamed to '+node[:-22]+'_orientCnst'

    elif not node.endswith('_orientCnst'):
        #print node+'_orientCnst'
        cmds.rename(node, node+'_orientCnst')

        print node+' was renamed to '+node+'_orientCnst'


#parentConstraint
for node in cmds.ls(type='parentConstraint'):
    if node.endswith('_parentConstraint1'):

        #print node[:-18]+'_parentCnst'
        cmds.rename(node, node[:-18]+'_parentCnst')

        print node+' was renamed to '+node[:-18]+'_parentCnst'

    elif node.endswith('_parentConstraint'):

        #print node[:-17]+'_parentCnst'
        cmds.rename(node, node[:-17]+'_parentCnst')

        print node+' was renamed to '+node[:-17]+'_parentCnst'

    elif node.endswith('_parentCnst_parentCnst'):

        #print node[:-22]+'_parentCnst'
        cmds.rename(node, node[:-22]+'_parentCnst')

        print node+' was renamed to '+node[:-22]+'_parentCnst'

    elif not node.endswith('_parentCnst'):
        #print node+'_parentCnst'
        cmds.rename(node, node+'_parentCnst')

        print node+' was renamed to '+node+'_parentCnst'
