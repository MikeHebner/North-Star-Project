import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QGridLayout
from PyQt5.QtCore import pyqtSlot, QSize
import PyQt5.QtWidgets as qtw


class AddStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Student')
        self.resize(200, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()

    def initUI(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Enter Student Name")
        textbox.move(20, 20)
        textbox2 = QLineEdit(self)
        textbox2.setPlaceholderText("Enter Student ID")
        textbox2.move(20, 60)
        button = QPushButton("Add Student", self)
        button.move(20, 100)




class AddInstructor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Instructor')
        self.resize(200, 200)
        layout = QVBoxLayout()
        self.initUi()
        self.setLayout(layout)
    def initUi(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Enter Instructor Name")
        textbox.move(20, 20)
        textbox2 = QLineEdit(self)
        textbox2.setPlaceholderText("Enter Instructor ID")
        textbox2.move(20, 60)

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

        pybutton3 = QPushButton('Edit Database', self)
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
