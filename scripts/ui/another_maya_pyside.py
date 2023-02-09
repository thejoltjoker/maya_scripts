from maya import cmds
from PySide2 import QtWidgets, QtCore, QtGui
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance


def getMayaMainWindow():  # Set to Maya Interface file
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    return mayaMainWindow


class App(QtWidgets.QMainWindow):
    def __init__(self, parent=getMayaMainWindow()):
        super(App, self).__init__(parent)
        self.setWindowTitle('App')

        self.tree = QtWidgets.QTreeWidget()
        self.tree.setHeaderLabels(['Substance', 'Shader', 'Action'])
        self.tree.header().resizeSection(0, 200)
        self.tree.header().resizeSection(1, 200)

        frame = QtWidgets.QWidget()
        self.setCentralWidget(frame)
        hl = QtWidgets.QHBoxLayout(frame)

        self.library = QtWidgets.QLineEdit()
        self.item = QtWidgets.QLineEdit()
        self.component = QtWidgets.QLineEdit()
        self.file_filter = QtWidgets.QLineEdit()
        self.execute_button = QtWidgets.QPushButton()

        self.library.setPlaceholderText('Library')
        self.item.setPlaceholderText('Item')
        self.component.setPlaceholderText('Component')
        self.file_filter.setPlaceholderText('File filter')
        self.execute_button.setText('Execute')
        self.execute_button.clicked.connect(self.execute)

        hl.addWidget(self.library)
        hl.addWidget(self.item)
        hl.addWidget(self.component)
        hl.addWidget(self.file_filter)
        hl.addWidget(self.execute_button)

    def execute(self, *args):
        # do stuff
        return


if __name__ == '__main__':
    app = App()
    app.show()
