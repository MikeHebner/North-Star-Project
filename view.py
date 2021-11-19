import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QGridLayout
from PyQt5.QtCore import pyqtSlot, QSize
import PyQt5.QtWidgets as qtw

class AddStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Menu')
        self.resize(200, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()

    def initUI(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Enter Student Name")
        textbox.move(20, 20)
        textbox.resize(150, 30)
        textbox2 = QLineEdit(self)
        textbox2.setPlaceholderText("Enter Student ID")
        textbox2.move(20, 60)
        textbox2.resize(150,30)
        button = QPushButton("Add Student", self)
        button.resize(120, 40)
        button.move(20, 100)
        button = QPushButton("Remove Student", self)
        button.resize(130, 40)
        button.move(20, 140)

class AddInstructor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Instructor')
        self.resize(200, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUi()
    def initUi(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Enter Instructor Name")
        textbox.move(20, 20)
        textbox.resize(150, 30)
        textbox2 = QLineEdit(self)
        textbox2.setPlaceholderText("Enter Instructor ID")
        textbox2.move(20, 60)
        textbox2.resize(150, 30)
        button = QPushButton("Add Instructor", self)
        button.resize(140, 40)
        button.move(20, 100)
        button = QPushButton("Remove Instructor", self)
        button.resize(140, 40)
        button.move(20, 140)

class editDatabase(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose Database")
        self.resize(200,200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()
    def initUI(self):
        button = QPushButton("Student Database", self)
        button.move(20, 50)
        button2 = QPushButton("Faculty Database", self)
        button2.move(20, 100)
        button2 = QPushButton("Faculty Database", self)
        button2.move(20, 100)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setMinimumSize(QSize(350, 300))
        self.setWindowTitle("Main Menu")
        self.label = QLabel("Database", self)
        self.label.move(40, 0)
        self.label1 = QLabel("Registration", self)
        self.label1.move(180, 0)
        self.initUI()

    def initUI(self):
        pybutton = QPushButton('Student', self)
        pybutton.clicked.connect(self.showAddStudent)
        pybutton.resize(120, 40)
        pybutton.move(20, 20)

        pybutton2 = QPushButton('Instructor', self)
        pybutton2.clicked.connect(self.showAddInstructor)
        pybutton2.resize(120, 40)
        pybutton2.move(20, 60)

        pybutton3 = QPushButton('Section', self)
        pybutton3.clicked.connect(self.showEditDatabase)
        pybutton3.resize(120, 40)
        pybutton3.move(20, 100)

        pybutton4 = QPushButton('Course', self)
        pybutton4.clicked.connect(self.clickMethod)
        pybutton4.resize(120, 40)
        pybutton4.move(20, 140)

        pybutton5 = QPushButton("Register Students", self)
        pybutton5.clicked.connect(self.clickMethod)
        pybutton5.resize(150, 40)
        pybutton5.move(160, 20)

        pybutton6 = QPushButton("Remove Flags", self)
        pybutton6.clicked.connect(self.clickMethod)
        pybutton6.resize(150, 40)
        pybutton6.move(160, 60)

        pybutton6 = QPushButton("Print Student Details", self)
        pybutton6.clicked.connect(self.clickMethod)
        pybutton6.resize(150, 40)
        pybutton6.move(160, 100)

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
