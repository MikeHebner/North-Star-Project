from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys

def clicked():
    print("clicked")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Header")

    label = QtWidgets.QLabel(win)
    label.setText("Label One")
    label.move(75,10)

    label = QtWidgets.QLabel(win)
    label.setText("Label Two")
    label.move(75, 50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click to add")
    b1.move(170, 225)
    b1.clicked.connect(clicked)

    combo = QComboBox(win)
    combo.addItem("Option One")
    combo.addItem("Option Two")

    combo.move(50, 225)

    combo = QComboBox(win)
    combo.addItem("Option Three")
    combo.addItem("Option Four")

    combo.move(50, 175)

    win.show()
    sys.exit(app.exec_())

window()