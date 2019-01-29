import maya.cmds as cmds

m=0
for i in cmds.ls(shapes=False):
    node=slips[]
        if m<myList[i]:
            m=myList[i]

set([x for x in l if l.count(x) > 1])

# import maya.cmds as cmds
# for node in cmds.ls():
#     if not cmds.ls(shapes=False)
#         print node


import maya.cmds as cmds

objs = [x for x in cmds.ls(shortNames=True, shapes=False) if '|' in x]
objs.sort(key=lambda x : x.count('|'))
objs.reverse()
for i in range(len(objs)):
    print ', '.join(objs)
    #cmds.rename(objs[i], objs[i].replace('|', ''))

    # proof
    if not len([x for x in cmds.ls(shortNames=True, shapes=False) if '|' in x]):
        print 'no non-unique names :)'