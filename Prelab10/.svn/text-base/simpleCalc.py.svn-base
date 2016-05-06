# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

class CalculatorConsumer(QMainWindow, Ui_Calculator):

    def __init__(self, parent=None):
        super(CalculatorConsumer, self).__init__(parent)
        self.setupUi(self)

        self.operator = None

        self.btn0.clicked.connect(self.displayNumber0)
        self.btn1.clicked.connect(self.displayNumber1)
        self.btn2.clicked.connect(self.displayNumber2)
        self.btn3.clicked.connect(self.displayNumber3)
        self.btn4.clicked.connect(self.displayNumber4)
        self.btn5.clicked.connect(self.displayNumber5)
        self.btn6.clicked.connect(self.displayNumber6)
        self.btn7.clicked.connect(self.displayNumber7)
        self.btn8.clicked.connect(self.displayNumber8)
        self.btn9.clicked.connect(self.displayNumber9)
        self.btnClear.clicked.connect(self.clear)
        self.btnEqual.clicked.connect(self.equal)
        self.btnDivide.clicked.connect(self.divide)
        self.btnDot.clicked.connect(self.dot)
        self.btnMinus.clicked.connect(self.minus)
        self.btnMultiply.clicked.connect(self.multiply)
        self.btnPlus.clicked.connect(self.plus)

    def displayNumber0(self):
        if self.txtDisplay.text() == "0":
            self.display("0")
        elif len(self.txtDisplay.text()) < 12:
            number = self.txtDisplay.text() + "0"
            self.txtDisplay.setText(number)

    def displayNumber1(self):
        if self.txtDisplay.text() == "0":
            self.txtDisplay.setText("1")
        elif len(self.txtDisplay.text()) < 12:
            number = self.txtDisplay.text() + "1"
            self.txtDisplay.setText(number)

    def displayNumber2(self):
        if self.txtDisplay.text() == "0":
            self.txtDisplay.setText("2")
        elif len(self.txtDisplay.text()) < 12:
            number = self.txtDisplay.text() + "2"
            self.txtDisplay.setText(number)

    def displayNumber3(self):
        if self.txtDisplay.text() == "0":
            self.txtDisplay.setText("3")
        elif len(self.txtDisplay.text()) < 12:
            number = self.txtDisplay.text() + "3"
            self.txtDisplay.setText(number)

    def displayNumber4(self):
        if self.txtDisplay.text() == "0":
            self.txtDisplay.setText("4")
        elif len(self.txtDisplay.text()) < 12:
            number = self.txtDisplay.text() + "4"
            self.txtDisplay.setText(number)

    def displayNumber5(self):
        if self.txtDisplay.text() == "0":
            self.txtDisplay.setText("5")
        elif len(self.txtDisplay.text()) < 12:
            number = self.txtDisplay.text() + "5"
            self.txtDisplay.setText(number)

    def displayNumber6(self):
        if self.txtDisplay.text() == "0":
            self.txtDisplay.setText("6")
        elif len(self.txtDisplay.text()) < 12:
            number = self.txtDisplay.text() + "6"
            self.txtDisplay.setText(number)

    def displayNumber7(self):
        if self.txtDisplay.text() == "0":
            self.txtDisplay.setText("7")
        elif len(self.txtDisplay.text()) < 12:
            number = self.txtDisplay.text() + "7"
            self.txtDisplay.setText(number)

    def displayNumber8(self):
        if self.txtDisplay.text() == "0":
            self.txtDisplay.setText("8")
        elif len(self.txtDisplay.text()) < 12:
            number = self.txtDisplay.text() + "8"
            self.txtDisplay.setText(number)

    def displayNumber9(self):
        if self.txtDisplay.text() == "0":
            self.txtDisplay.setText("9")
        elif len(self.txtDisplay.text()) < 12:
            number = self.txtDisplay.text() + "9"
            self.txtDisplay.setText(number)

    def clear(self):
        self.display("0")
        self.operator = None

    def divide(self):
        if self.operator is None:
            self.operator = "/"
            number = self.txtDisplay.text() + " / "
            self.txtDisplay.setText(number)
        else:
            if self.txtDisplay.text()[-1] == " ":
                number = self.txtDisplay.text()[:-2] + "/ "
                self.display(number)
                self.operator = "/"
            else:
                self.equal()
                self.operator = "/"
                number = self.txtDisplay.text() + " / "
                self.display(number)

    def dot(self):
        if "." in self.txtDisplay.text():
            return
        number = self.txtDisplay.text() + "."
        self.txtDisplay.setText(number)

    def equal(self):
        string = self.txtDisplay.text().split()
        if len(string) == 3 and self.operator is not None:
            num1 = float(string[0].replace(",", ""))
            num2 = float(string[2].replace(",", ""))
            if self.operator == "*":
                self.display(str(num1 * num2))
            elif self.operator == "+":
                self.display(str(num1 + num2))
            elif self.operator == "-":
                self.display(str(num1 - num2))
            elif self.operator == "/":
                self.display(str(num1 / num2))
            self.operator = None
        else:
            return

    def minus(self):
        if self.operator is None:
            self.operator = "-"
            number = self.txtDisplay.text() + " - "
            self.txtDisplay.setText(number)
        else:
            if self.txtDisplay.text()[-1] == " ":
                number = self.txtDisplay.text()[:-2] + "- "
                self.display(number)
                self.operator = "-"
            else:
                self.equal()
                self.operator = "-"
                number = self.txtDisplay.text() + " - "
                self.display(number)

    def multiply(self):
        if self.operator is None:
            self.operator = "*"
            number = self.txtDisplay.text() + " * "
            self.txtDisplay.setText(number)
        else:
            if self.txtDisplay.text()[-1] == " ":
                number = self.txtDisplay.text()[:-2] + "* "
                self.display(number)
                self.operator = "*"
            else:
                self.equal()
                self.operator = "*"
                number = self.txtDisplay.text() + " * "
                self.display(number)

    def plus(self):
        if self.operator is None:
            self.operator = "+"
            number = self.txtDisplay.text() + " + "
            self.txtDisplay.setText(number)
        else:
            if self.txtDisplay.text()[-1] == " ":
                number = self.txtDisplay.text()[:-2] + "+ "
                self.display(number)
                self.operator = "+"
            else:
                self.equal()
                self.operator = "+"
                number = self.txtDisplay.text() + " + "
                self.display(number)

    def display(self, text):
        decs = self.cboDecimal.currentIndex()
        tSplit = text.split()
        if len(tSplit) == 1:
            if self.chkSeparator.isChecked() is True:
                self.txtDisplay.setText("{:,.{precs}f}".format(float(tSplit[0].replace(",", "")), precs=decs))
            else:
                self.txtDisplay.setText("{:.{precs}f}".format(float(tSplit[0].replace(",", "")), precs=decs))
        elif len(tSplit) == 2:
            if self.chkSeparator.isChecked() is True:
                self.txtDisplay.setText("{:,.{precs}f} {} ".format(float(tSplit[0].replace(",", "")), tSplit[1], precs=decs))
            else:
                self.txtDisplay.setText("{:.{precs}f}".format(float(tSplit[0].replace(",", "")), precs=decs) + " " + "{}".format(tSplit[1]) + " ")
        elif len(tSplit) == 3:
            if self.chkSeparator.isChecked() is True:
                self.txtDisplay.setText("{:,.{precs}f} {} {:,.{precs}f}".format(float(tSplit[0].replace(",", "")), tSplit[1], float(tSplit[2].replace(",", "")), precs=decs))
            else:
                self.txtDisplay.setText("{:.{precs}f}".format(float(tSplit[0].replace(",", "")), precs=decs) + " " + "{}".format(tSplit[1]) + " " + "{:.{precs}f}".format(float(tSplit[2].replace(",", ""))), precs=decs)


currentApp = QApplication(sys.argv)
currentForm = CalculatorConsumer()

currentForm.show()
currentApp.exec_()
