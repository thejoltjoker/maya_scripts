import maya.cmds as cmds

def main(layer_name):
    layer_adjustments = cmds.editRenderLayerAdjustment(layer_name, query=True, layer=True)
    for adj in layer_adjustments:
        val = cmds.getAttr(adj)
        print adj+" = "+val

if __name__ == '__main__':
    RENDERLAYER = 'layerName'
    main(RENDERLAYER)
