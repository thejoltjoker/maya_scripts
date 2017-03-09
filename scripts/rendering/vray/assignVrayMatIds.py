import maya.cmds as cmds


def addVrayMaterialIds(materials=None):
    """ Add a vray_material_id attribute to selected materials (and related materials from objects)
    :param materials: Materials to apply the attribute to. If materials is None it will get
                      the materials related to the current selection.
    """
    if materials is None:

        materials = cmds.ls(sl=True, mat=True)

        # Get materials related to selection (material from object)
        # And add those materials to the material list we already have
        sel = cmds.ls(sl=True)
        if sel:
            sel_history = cmds.listHistory(sel,f=1)
            if sel_history:
                sel_connections = cmds.listConnections(sel_history)
                if sel_connections:
                    connected_materials = cmds.ls(sel_connections, mat=True)
                    if connected_materials:
                        materials = set(materials)
                        materials.update(connected_materials)
                        materials = list(materials)
    else:
        # filter input to materials only
        materials = cmds.ls(materials, mat=1)

    if not materials:
        raise RuntimeError("No materials found")

    if materials:
        result = cmds.promptDialog(title='Material ID value',
                                    message='Material ID:',
                                    button=['OK', 'Cancel'],
                                    defaultButton='OK',
                                    cancelButton='Cancel',
                                    dismissString='Cancel')

        if result == 'OK':
            value = int(cmds.promptDialog(query=True, text=True))
            for mat in materials:
                cmds.vray("addAttributesFromGroup", mat, "vray_material_id", 1)
                cmds.setAttr("{0}.{1}".format(mat, 'vrayMaterialId'), value)


if __name__ == "__main__":
    addVrayMaterialIds()