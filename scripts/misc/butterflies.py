# Used in the butterfly project to set attributes on multiple butterflies
import re
import maya.cmds as cmds

# step by step
# select proxytransform
for transform in cmds.ls(sl=1):
    print("transform = {}".format(transform))

    proxy_id = int(re.findall(r"\d+", transform)[0])
    print("proxy_id = {}".format(proxy_id*4))

    if not cmds.attributeQuery('proxyID', node=transform, exists=True):
        cmds.addAttr(longName="proxyID", attributeType='long', k=True)

    id_multiplier = 3
    cmds.setAttr('{}.proxyID'.format(transform), proxy_id*id_multiplier)

    shape = cmds.listRelatives(transform)[0]
    print("shape = {}".format(shape))

    b_name = shape.split('_')[0]
    print("b_name = {}".format(b_name))

    proxy_node = [x for x in cmds.listConnections(
        shape, scn=0) if 'Proxy' or 'PROXY' in x][0]
    print("proxy_node = {}".format(proxy_node))

    # create multDivide node
    mult_node = cmds.shadingNode(
        'multiplyDivide', asUtility=1, n='{}_MULT'.format(b_name))
    print mult_node

    # create sum node
    sum_node = cmds.shadingNode(
        'plusMinusAverage', asUtility=1, n='{}_SUM'.format(b_name))
    print sum_node

    # connect nodes
    # Transform to multdiv
    cmds.connectAttr('{}.proxyID'.format(
        transform), '{}.input1.input1X'.format(mult_node), f=1)
    # ramp to mult
    cmds.connectAttr('butterfly_mult_RAMP.outColor',
                     '{}.input2'.format(mult_node), f=1)

    # multdiv to sum
    cmds.connectAttr('{}.output.outputX'.format(
        mult_node), '{}.input1D[0]'.format(sum_node), f=1)
    # time to sum
    cmds.connectAttr('butterflies_CTRL.time',
                     '{}.input1D[1]'.format(sum_node), f=1)

    # sum to proxy frame
    cmds.connectAttr('{}.output1D'.format(sum_node),
                     '{}.frameExtension'.format(proxy_node), f=1)

    # connect proxy display mode
    cmds.connectAttr('{}.proxyDisplayMode'.format('butterflies_CTRL'), '{}.displayMode'.format(
        proxy_node), f=1)

    # connect proxy animation toggle
    cmds.connectAttr('{}.proxyAnimation'.format('butterflies_CTRL'), '{}.useFrameExtension'.format(
        proxy_node), f=1)

    # rename proxy
    cmds.rename(proxy_node, '{}_PROXY'.format(b_name))


# //////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////


# cmds.addAttr(longName="proxyID", attributeType='long', k=True)

# for i in cmds.ls(sl=1):
#     cmds.deleteAttr('{}.proxyID'.format(i))


# for n, i in enumerate(cmds.ls(sl=1)):
#     cmds.setAttr('{}.proxyID'.format(i), n+1)


# set proxy id
for transform in cmds.ls(sl=1):
    multiplier = 3
    print("transform = {}".format(transform))

    proxy_id = int(re.findall(r"\d+", transform)[0])
    print("proxy_id = {}".format(proxy_id*multiplier))

    cmds.setAttr('{}.proxyID'.format(transform), proxy_id*multiplier)


# # connect attributes
# sel = cmds.ls(sl=1)
# print sel
# cmds.connectAttr('{}.proxyID'.format(
#     sel[0]), '{}.input1D[1]'.format(sel[1]), f=1)
# cmds.connectAttr('{}.output1D'.format(
#     sel[1]), '{}.frameExtension'.format(sel[2]), f=1)


# # set proxy display mode
# sel = cmds.ls(sl=1)
# for node in sel:
#     print cmds.nodeType(node)
#     if cmds.nodeType(node) == 'RedshiftProxyMesh':
#         cmds.setAttr("{}.displayMode".format(node), 1)

# test_string = 'jensne012_proxu'
# proxy_id = int(re.findall(r"\d+", test_string)[0])
# print proxy_id
