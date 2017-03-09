"""load qt ui file

just testing to load a ui.
"""

from __future__ import division
import sys, os
from PyQt4 import QtCore, QtGui
from PyQt4.uic import loadUi
from PyQt4.QtGui import QMessageBox



class ShotCreator(QtGui.QDialog):
    def __init__(self, *args):
        ui = 'ShotCreator_UI.ui'
        QtGui.QWidget.__init__(self, *args)
        loadUi(ui, self)
        self.show()

        #Slots

        self.connect(self.browseLocation_btn, QtCore.SIGNAL("clicked()"), self.openBrowse)
        self.connect(self.create_btn, QtCore.SIGNAL("clicked()"), self.makeDir)
        self.progressBar.setValue(0)

    def openBrowse(self):
        dirLocation = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.browseLocation.setText(dirLocation)


    def fullShotAmount(self):
        amount = self.shotAmount
        amount = amount.text()
        #Making sure it's an integer
        try:
            amount = int(amount)
            if amount <= 250:
                return range(amount)

            if amount >= 251:
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setWindowTitle("Are you sure?")
                msgBox.setText("Creating this many folders may take a long time. Are you sure?")
                msgBox.addButton(QtGui.QMessageBox.Yes)
                msgBox.addButton(QtGui.QMessageBox.No)
                msgBox.setDefaultButton(QtGui.QMessageBox.No)
                ret = msgBox.exec_()

                if ret == QtGui.QMessageBox.Yes:
                    return range(amount)

                if ret == QtGui.QMessageBox.No:
                    return


        except ValueError:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Oops - Shot Amount")
            msgBox.setText("Please enter a whole number. (No letters, expressions, or float values)")
            msgBox.exec_()

    def projName(self):
        proj = self.projectName
        proj = proj.text()
        proj = str(proj)
        #Making sure there is a project name
        if len(proj) == 0:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Oops - Project Name")
            msgBox.setText("Please enter your project name")
            msgBox.exec_()

        else:
            return proj

    def queryValues(self):
        #Checking what folders to create and assigning name.
        self.checkBoxes = []
        if self.animation_btn.isChecked():
            self.checkBoxes.append("Animation")
        if self.compositing_btn.isChecked():
            self.checkBoxes.append("Compositing")
        if self.FX_btn.isChecked():
            self.checkBoxes.append("FX")
        if self.layout_btn.isChecked():
            self.checkBoxes.append("Layout")
        if self.lighting_btn.isChecked():
            self.checkBoxes.append("Lighting")
        if self.surfacing_btn.isChecked():
            self.checkBoxes.append("Surfacing")
        if self.productionCheck_btn.isChecked():
            self.checkBoxes.append("Production")
        if self.sourcePlates_btn.isChecked():
            self.checkBoxes.append("Source Plates")

        #Checking if department checkboxes are checked
        if self.checkBoxes == []:

            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Oops - Checkboxes")
            msgBox.setText("Please check your department folders")
            msgBox.exec_()
        return self.checkBoxes


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = ShotCreator()
    sys.exit(app.exec_())