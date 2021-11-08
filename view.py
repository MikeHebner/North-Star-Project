from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
#used for main menu
def clicked():
    print("clicked")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Main Menu")

    label = QtWidgets.QLabel(win)
    label.setText("Options: ")
    label.move(20, 10)

    label = QtWidgets.QLabel(win)
    label.setText("Add Student")
    label.move(75,10)

    label = QtWidgets.QLabel(win)
    label.setText("Add Instructor")
    label.move(75, 30)

    label = QtWidgets.QLabel(win)
    label.setText("Edit Database")
    label.move(75, 50)

    label = QtWidgets.QLabel(win)
    label.setText("Remove Student")
    label.move(75, 70)
    label = QtWidgets.QLabel(win)
    label.setText("Remove Instructor")
    label.move(75, 90)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click to add")
    b1.move(170, 225)
    b1.clicked.connect(clicked)

    combo = QComboBox(win)
    combo.addItem("Add Student")
    combo.addItem("Add Instructor")
    combo.addItem("Remove Instructor")
    combo.addItem("Remove Student")
    combo.addItem("Edit Database")

    combo.move(50, 225)

    win.show()
    sys.exit(app.exec_())

window()