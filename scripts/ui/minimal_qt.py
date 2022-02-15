from PySide import QtCore, QtGui
from PySide import QtUiTools
import os, sys


def load_ui(file_name, where=None):
    loader = QtUiTools.QUiLoader()
    ui_file = QtCore.QFile(file_name)
    ui_file.open(QtCore.QFile.ReadOnly)
    myWidget = loader.load(ui_file, where)
    ui_file.close()
    return myWidget


if __name__ == '__main__':
    # Create Qt app
    app = QtGui.QApplication(sys.argv)

    # Load ui and show the widget
    ui_file_path = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'PCBOutlineCreator.ui')
    gui = load_ui(ui_file_path)
    gui.show()

    # Run the app
    sys.exit(app.exec_())
