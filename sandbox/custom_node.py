import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

kPluginNodeName = "customNode"
kPluginNodeId = OpenMaya.MTypeId(0x00333)


class customNode(OpenMayaMPx.MPxNode):

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)

    def nodeCreator():
        return OpenMayaMPx.asMPxPtr(customNode())

    def nodeInitializer():
        pass

    def initializePlugin(mobject):
        mplugin = OpenMayaMPx.MFnPlugin(mobject, "", "", "Any")
        try:
            mplugin.registerNode(
                kPluginNodeName, kPluginNodeId, nodeCreator, nodeInitializer)
        except:
            sys.stderr.write("Failed to register command: % s
                             " % kPluginNodeName)
            raise

    def uninitializePlugin(mobject):
        mplugin = OpenMayaMPx.MFnPlugin(mobject)
        try:
            mplugin.deregisterNode(kPluginNodeId)
        except:
            sys.stderr.write("Failed to unregister node: % s
                             " % kPluginNodeName)
            raise
