import maya.OpenMayaUI as omui
from rafiki.core.Qt import QtCore
from rafiki.core.Qt import QtWidgets
try:
    from shiboken import wrapInstance
except:
    from shiboken import wrapInstance


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class TestDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(TestDialog, self).__init__(parent)

        self.setWindowTitle("Test Dialog")
        self.setMinimumWidth(200)

        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)


if __name__ == "__main__":
    d = TestDialog()
    d.show()
