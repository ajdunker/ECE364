import sys
import re

from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.errorInfoLabel.setText("")

        self.clearButton.clicked.connect(self.clear)
        self.loadButton.clicked.connect(self.loadData)
        self.saveToTargetButton.clicked.connect(self.validate)

        self.emailLineEdit.textChanged.connect(self.changeDetect)
        self.zipLineEdit.textChanged.connect(self.changeDetect)
        self.cityLineEdit.textChanged.connect(self.changeDetect)
        self.addressLineEdit.textChanged.connect(self.changeDetect)
        self.firstNameLineEdit.textChanged.connect(self.changeDetect)
        self.lastNameLineEdit.textChanged.connect(self.changeDetect)
        self.stateLineEdit.textChanged.connect(self.changeDetect)

        self.texts = [self.emailLineEdit, self.zipLineEdit, self.cityLineEdit, self.addressLineEdit,
                      self.firstNameLineEdit, self.lastNameLineEdit, self.stateLineEdit]



    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """
        self.clear()

        f = open(filePath, 'r')
        data = f.read()
        f.close()

        fname = re.search(r"<FirstName>([\w\s.]+)</FirstName>", data)
        if fname is not None:
            self.firstNameLineEdit.setText(fname.group(1))
        lname = re.search(r"<LastName>([\w\s.]+)</LastName>", data)
        if lname is not None:
            self.lastNameLineEdit.setText(lname.group(1))
        add = re.search(r"<Address>([\w\s.]+)</Address>", data)
        if add is not None:
            self.addressLineEdit.setText(add.group(1))
        city = re.search(r"<City>([\w\s.]+)</City>", data)
        if city is not None:
            self.cityLineEdit.setText(city.group(1))
        state = re.search(r"<State>([\w\s.]+)</State>", data)
        if state is not None:
            self.stateLineEdit.setText(state.group(1))
        zip = re.search(r"<ZIP>([\w\s]+)</ZIP>", data)
        if zip is not None:
            self.zipLineEdit.setText(zip.group(1))
        email = re.search(r"<Email>([\w\s.@]+)</Email>", data)
        if email is not None:
            self.emailLineEdit.setText(email.group(1))

        self.loadButton.setEnabled(False)
        self.saveToTargetButton.setEnabled(True)

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def clear(self):
        self.firstNameLineEdit.setText("")
        self.lastNameLineEdit.setText("")
        self.stateLineEdit.setText("")
        self.addressLineEdit.setText("")
        self.cityLineEdit.setText("")
        self.emailLineEdit.setText("")
        self.zipLineEdit.setText("")

        self.loadButton.setEnabled(True)
        self.saveToTargetButton.setEnabled(False)

    def changeDetect(self):
        self.loadButton.setEnabled(False)
        self.saveToTargetButton.setEnabled(True)
        emptycheck = True
        for item in self.texts:
            if item.text() != "":
                emptycheck = False
        if emptycheck is True:
            self.loadButton.setEnabled(True)
            self.saveToTargetButton.setEnabled(False)

    def validate(self):
        self.errorInfoLabel.setText("")
        if self.firstNameLineEdit.text() == "":
            self.errorInfoLabel.setText("No first name given.")
            return
        if self.lastNameLineEdit.text() == "":
            self.errorInfoLabel.setText("No last name given.")
            return
        if self.addressLineEdit.text() == "":
            self.errorInfoLabel.setText("No address given.")
            return
        if self.cityLineEdit.text() == "":
            self.errorInfoLabel.setText("No city given.")
            return
        if self.stateLineEdit.text() == "":
            self.errorInfoLabel.setText("No state given.")
            return
        elif self.stateLineEdit.text() not in self.states:
            self.errorInfoLabel.setText("Invalid state.")
            return
        if self.zipLineEdit.text() == "":
            self.errorInfoLabel.setText("No ZIP given.")
            return
        elif len(self.zipLineEdit.text()) != 5 or not str.isdigit(self.zipLineEdit.text()):
            self.errorInfoLabel.setText("Invalid ZIP.")
            return
        if self.emailLineEdit.text() == "":
            self.errorInfoLabel.setText("No email given.")
            return
        email = re.search(r"\w+@\w+\.\w+", self.emailLineEdit.text())
        if email is None:
            self.errorInfoLabel.setText("Invalid email.")
            return
        self.savexml()

    def savexml(self):
        wstring = '<?xml version="1.0" encoding="UTF-8"?>\n<user>\n'
        wstring += '\t<FirstName>' + self.firstNameLineEdit.text() + '</FirstName>\n'
        wstring += '\t<LastName>' + self.lastNameLineEdit.text() + '</LastName>\n'
        wstring += '\t<Address>' + self.addressLineEdit.text() + '</Address>\n'
        wstring += '\t<City>' + self.cityLineEdit.text() + '</City>\n'
        wstring += '\t<State>' + self.stateLineEdit.text() + '</State>\n'
        wstring += '\t<ZIP>' + self.zipLineEdit.text() + '</ZIP>\n'
        wstring += '\t<Email>' + self.emailLineEdit.text() + '</Email>\n'
        wstring += '</user>\n'
        f = open('target.xml', 'w')
        f.write(wstring)
        f.close()

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
