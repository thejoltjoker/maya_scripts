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

        self.create_widgets()
        self.create_layouts()

    def create_widgets(self):
        self.lineedit = QtWidgets.QLineEdit()
        self.checkbox1 = QtWidgets.QCheckBox('cb1')
        self.checkbox2 = QtWidgets.QCheckBox('cb2')
        self.button1 = QtWidgets.QPushButton('btn1')
        self.button2 = QtWidgets.QPushButton('btn2')

    def create_layouts(self):
        main_layout = QtWidgets.QGridLayout(self)
        main_layout.addWidget(self.lineedit)
        main_layout.addWidget(self.checkbox1)
        main_layout.addWidget(self.checkbox2)
        main_layout.addWidget(self.button1)
        main_layout.addWidget(self.button2)


if __name__ == "__main__":
    d = TestDialog()
    d.show()
