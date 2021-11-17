import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, \
    QGridLayout
from PyQt5.QtCore import pyqtSlot, QSize
import PyQt5.QtWidgets as qtw


class AddStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Student')
        self.resize(200, 200)
        layout = QVBoxLayout()
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Enter Student Name")
        self.textbox.move(20, 20)
        self.textbox2 = QLineEdit(self)
        self.textbox2.setPlaceholderText("Enter Student ID")
        self.textbox2.move(20, 60)
        self.b1 = QPushButton("Add Student", self)
        layout.addWidget(self.b1)
        self.b1.resize(30,100)#error button not resizing cant figure out
        self.b1.move(200, 50)
        self.setLayout(layout)
        self.show()


class AddInstructor(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window2")
        layout.addWidget(self.label)
        self.setLayout(layout)


class editDatabase(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window3")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None

        self.setMinimumSize(QSize(300, 200))
        self.setWindowTitle("Main Menu")
        self.initUI()

    def initUI(self):
        pybutton = QPushButton('Add Student', self)
        pybutton.clicked.connect(self.showAddStudent)
        pybutton.resize(100, 32)
        pybutton.move(50, 20)

        pybutton2 = QPushButton('Add Instructor', self)
        pybutton2.clicked.connect(self.showAddInstructor)
        pybutton2.resize(100, 32)
        pybutton2.move(50, 60)

        pybutton3 = QPushButton('Edit Course', self)
        pybutton3.clicked.connect(self.showEditDatabase)
        pybutton3.resize(100, 32)
        pybutton3.move(50, 100)

        pybutton4 = QPushButton('Edit Course', self)
        pybutton4.clicked.connect(self.clickMethod)
        pybutton4.resize(100, 32)
        pybutton4.move(50, 140)

    def clickMethod(self):
        print('Clicked Pyqt button.')

    def showAddStudent(self, checked):
        if self.w is None:
            self.w = AddStudent()
            self.w.show()
        else:
            self.w.close()
            self.w = None

    def showAddInstructor(self, checked):
        if self.w is None:
            self.w = AddInstructor()
            self.w.show()
        else:
            self.w.close()
            self.w = None

    def showEditDatabase(self, checked):
        if self.w is None:
            self.w = editDatabase()
            self.w.show()
        else:
            self.w.close()
            self.w = None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
