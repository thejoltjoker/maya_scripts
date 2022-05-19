def initializePlugin(plugin):
    from maya_scripts import scripts_to_menu
    scripts_to_menu.create_menu()


def uninitializePlugin(plugin):
    from maya_scripts import scripts_to_menu
    scripts_to_menu.delete_menu()
