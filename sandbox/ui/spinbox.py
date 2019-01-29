from PySide import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)

        # Create a slider
        self.floatSlider = QtGui.QSlider()
        self.floatSlider.setObjectName('floatSlider')
        self.floatSlider.valueChanged.connect(self.myFunction)

        # Create a spinbox
        self.colorSpinBox = QtGui.QSpinBox()
        self.colorSpinBox.setObjectName('colorSlider')
        self.colorSpinBox.valueChanged.connect(self.myFunction)

        # Create widget's layout
        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addWidget(self.floatSlider)
        mainLayout.addWidget(self.colorSpinBox)
        self.setLayout(mainLayout)

        # Resize widget and show it
        self.resize(300, 300)
        self.show()

    def myFunction(self):
        # Getting current control calling this function with self.sender()
        # Print out the control's internal name, its type, and its value
        print "{0}: type {1}, value {2}".format( self.sender().objectName(), type( self.sender() ), self.sender().value() )

win = Window()