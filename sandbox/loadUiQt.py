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




    def makeDir(self):
        #Get data
        departments = self.queryValues()
        shots = self.fullShotAmount()
        proj = self.projName()

        #Converting proj to string
        proj = str(proj)

        #Converting dirLoc to string
        dirLoc = self.browseLocation.text()
        dirLoc = str(dirLoc)

        if dirLoc == "":
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Oops - Directory Location")
            msgBox.setText("Please give a directory location")
            msgBox.exec_()


        #Make dirs
        if not os.path.exists(dirLoc):
            os.mkdir(dirLoc)
        os.chdir(dirLoc)

        if not os.path.exists(proj):
            os.mkdir(proj)

        os.chdir(proj)


        #Creating folders
        if not os.path.exists("Images"):
            os.mkdir("Images")

        if not os.path.exists("Work"):
            os.mkdir("Work")

        if not os.path.exists("Repository"):
            os.mkdir("Repository")

        if not os.path.exists("Production"):
            if "Production" in departments:
                os.mkdir("Production")

        if not os.path.exists("Source Plates"):
            if "Source Plates" in departments:
                os.mkdir("Source Plates")

        os.chdir("Images")

        #Creating shot numbers
        shot = 0
        for s in shots:
            shot = shot + 5
            sShot = ("00" + str(shot))

            if not os.path.exists(sShot):

                #Create shot and it's folders for "Images"
                #Create shot folder
                os.mkdir(sShot)
                os.chdir(sShot)
                #Create Compositing
                if "Compositing" in departments:
                    os.makedirs(os.path.join("Compositing", "Nuke"))
                #Back to shot
                os.chdir(dirLoc)
                os.chdir(proj)
                os.chdir("Images")
                os.chdir(sShot)
                #Create FX
                if "FX" in departments:
                    os.makedirs(os.path.join("FX", "Houdini"))
                    os.chdir("FX")
                    os.mkdir("Maya")
                #Back to shot
                os.chdir(dirLoc)
                os.chdir(proj)
                os.chdir("Images")
                os.chdir(sShot)
                #Create Lighting
                if "Lighting" in departments:
                    os.makedirs(os.path.join("Lighting", "Maya"))


                #Create shot and it's folders for "Work"
                os.chdir(dirLoc)
                os.chdir(proj)
                os.chdir("Work")
                #Create shot folder
                os.mkdir(sShot)
                os.chdir(sShot)
                if "Animation" in departments:
                    os.makedirs(os.path.join("Animation", "Maya"))
                    #Back to shot
                    os.chdir(dirLoc)
                    os.chdir(proj)
                    os.chdir("Work")
                    os.chdir(sShot)

                if "Compositing" in departments:
                    os.makedirs(os.path.join("Compositing", "Nuke"))
                    #Back to shot
                    os.chdir(dirLoc)
                    os.chdir(proj)
                    os.chdir("Work")
                    os.chdir(sShot)

                if "FX" in departments:
                    os.makedirs(os.path.join("FX", "Houdini"))
                    os.chdir("FX")
                    os.mkdir("Maya")
                    #Back to shot
                    os.chdir(dirLoc)
                    os.chdir(proj)
                    os.chdir("Work")
                    os.chdir(sShot)

                if "Layout" in departments:
                    os.mkdir("Layout")
                    #Back to shot
                    os.chdir(dirLoc)
                    os.chdir(proj)
                    os.chdir("Work")
                    os.chdir(sShot)

                if "Lighting" in departments:
                    os.makedirs(os.path.join("Lighting", "Maya"))
                    #Back to shot
                    os.chdir(dirLoc)
                    os.chdir(proj)
                    os.chdir("Work")
                    os.chdir(sShot)

                if "Surfacing" in departments:
                    os.makedirs(os.path.join("Surfacing", "Mari"))
                    os.chdir("Surfacing")
                    os.mkdir("Maya")


                #Create shot and it's folders for "Source Plates"
                os.chdir(dirLoc)
                os.chdir(proj)
                if os.path.exists("Source Plates"):
                    os.chdir("Source Plates")
                    #Create shot folder
                    os.mkdir(sShot)
                    os.chdir(sShot)
                    os.makedirs(os.path.join("Image Sequence", "DeNoise" ))
                    os.chdir("Image Sequence")
                    os.mkdir("Source")
                    os.chdir(dirLoc)
                    os.chdir(proj)
                    os.chdir("Source Plates")
                    os.chdir(sShot)
                    os.mkdir("MOVs")


                #End of loop
                os.chdir(dirLoc)
                os.chdir(proj)
                os.chdir("Images")
                #Progress Bar update
                self.progressBar.setValue((int(s) / int(len(shots))* 100))

        self.progressBar.setValue(100)





    def openBrowse(self):
        dirLocation = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.browseLocation.setText(dirLocation)


    #Getting the amount of shots
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



