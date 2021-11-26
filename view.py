import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QGridLayout
from PyQt5.QtCore import pyqtSlot, QSize
import PyQt5.QtWidgets as qtw

class AddStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle('Student Database')
        self.resize(200, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()

    def initUI(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Enter Student Name")
        textbox.move(20, 20)
        textbox.resize(150, 30)
        textbox.setStyleSheet("border: 1px solid black;")
        textbox2 = QLineEdit(self)
        textbox2.setPlaceholderText("Enter Student ID")
        textbox2.move(20, 60)
        textbox2.resize(150,30)
        button = QPushButton("Add Student", self)
        button.resize(150, 40)
        button.move(20, 100)
        button2 = QPushButton("Remove Student", self)
        button2.resize(150, 40)
        button2.move(20, 140)
        button3 = QPushButton("Edit Student Info", self)
        button3.clicked.connect(self.showStudentInfo)
        button3.resize(150, 40)
        button3.move(20, 180)

    def showStudentInfo(self):
        if self.w is None:
            self.w = studentInfo()
            self.w.show()
        else:
            self.w.close()
            self.w = None

class studentInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Database')
        self.resize(200, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()

    def initUI(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Enter Student Name")
        textbox.move(20, 20)
        textbox.resize(150, 30)

class AddInstructor(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle('Instructor Database')
        self.resize(200, 300)
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
        button.resize(150, 40)
        button.move(20, 100)
        button2 = QPushButton("Remove Instructor", self)
        button2.resize(150, 40)
        button2.move(20, 140)
        button3 = QPushButton("Edit Instructor Info", self)
        button3.clicked.connect(self.showInstructorInfo)
        button3.resize(150, 40)
        button3.move(20, 180)
    def showInstructorInfo(self):
        if self.w is None:
            self.w = instructorInfo()
            self.w.show()
        else:
            self.w.close()
            self.w = None
class instructorInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle('Instructor Database')
        self.resize(200, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUi()
    def initUi(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Enter Instructor Name")
class RegisterStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Register Student')
        self.resize(200, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUi()

    def initUi(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Enter Course ID")
        textbox.move(20, 20)
        textbox.resize(150, 30)
        textbox2 = QLineEdit(self)
        textbox2.setPlaceholderText("Enter Student ID")
        textbox2.move(20, 60)
        textbox2.resize(150, 30)
        textbox3 = QLineEdit(self)
        textbox3.setPlaceholderText("Enter Course Section ID")
        textbox3.move(20, 100)
        textbox3.resize(150, 30)
        button = QPushButton("Register Student", self)
        button.move(20, 150)
        button.resize(150, 40)

class RemoveFlag(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle('Remove Flag')
        self.resize(200, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUi()
    def initUi(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Enter Student ID")
        textbox.move(20, 20)
        textbox.resize(150, 30)
        button = QPushButton("Search", self)
        button.move(20, 100)
        button.clicked.connect(self.showFlags)
        button2 = QPushButton("Exit", self)
        button2.move(20, 140)
        button2.clicked.connect(lambda:self.close())

    def showFlags(self):
        if self.w is None:
            self.w = flagMenu()
            self.w.show()
        else:
            self.w.close()
            self.w = None

class flagMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Database')
        self.resize(200, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()

    def initUI(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Enter Student Name")
        textbox.move(20, 20)
        textbox.resize(150, 30)

class PrintStudentDetails(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle('Student Details')
        self.resize(200, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUi()

    def initUi(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Enter Student ID")
        textbox.move(20, 20)
        textbox.resize(150, 30)
        button = QPushButton("Search", self)
        button.move(20, 100)
        button.clicked.connect(self.showStudentInfo)
        button2 = QPushButton("Exit", self)
        button2.move(20, 140)
        button2.clicked.connect(lambda: self.close())

    def showStudentInfo(self):
        if self.w is None:
            self.w = studentDetails()
            self.w.show()
        else:
            self.w.close()
            self.w = None

class studentDetails(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Details')
        self.resize(200, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()

    def initUI(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Student Details here WIP")
        textbox.move(20, 20)
        textbox.resize(150, 30)

class editSection(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Section")
        self.resize(200,200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()
    def initUI(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Enter Course ID")
        textbox.move(20, 20)
        textbox.resize(150, 30)
        textbox2 = QLineEdit(self)
        textbox2.setPlaceholderText("Enter New Section ID")
        textbox2.move(20, 60)
        textbox2.resize(150, 30)
        textbox3 = QLineEdit(self)
        textbox3.setPlaceholderText("Enter Instructor ID")
        textbox3.move(20, 100)
        textbox3.resize(150, 30)
        button = QPushButton("Add Section to Course", self)
        button.move(20, 140)
        button.resize(150, 30)

class editCourse(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Course")
        self.resize(200,200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()
    def initUI(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Enter Course ID")
        textbox.move(20, 20)
        textbox.resize(150, 30)
        textbox2 = QLineEdit(self)
        textbox2.setPlaceholderText("Enter New Section ID")
        textbox2.move(20, 60)
        textbox2.resize(150, 30)
        button = QPushButton("Add Section to Course", self)
        button.move(20, 100)
        button.resize(150, 30)

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
        pybutton.move(20, 30)

        pybutton2 = QPushButton('Instructor', self)
        pybutton2.clicked.connect(self.showAddInstructor)
        pybutton2.resize(120, 40)
        pybutton2.move(20, 70)

        pybutton3 = QPushButton('Section', self)
        pybutton3.clicked.connect(self.showSection)
        pybutton3.resize(120, 40)
        pybutton3.move(20, 110)

        pybutton4 = QPushButton('Course', self)
        pybutton4.clicked.connect(self.showCourse)
        pybutton4.resize(120, 40)
        pybutton4.move(20, 150)

        pybutton5 = QPushButton("Register Students", self)
        pybutton5.clicked.connect(self.showRegisterStudent)
        pybutton5.resize(150, 40)
        pybutton5.move(160, 30)

        pybutton6 = QPushButton("Remove Flags", self)
        pybutton6.clicked.connect(self.showRemoveFlag)
        pybutton6.resize(150, 40)
        pybutton6.move(160, 70)

        pybutton7 = QPushButton("Print Student Details", self)
        pybutton7.clicked.connect(self.showPrintStudentDetail)
        pybutton7.resize(150, 40)
        pybutton7.move(160, 110)

        pybutton8 = QPushButton("Exit", self)
        pybutton8.clicked.connect(lambda: self.close())
        pybutton8.resize(150, 40)
        pybutton8.move(100, 250)

    def clickMethod(self):
        print('Clicked Pyqt button.')

    def showAddStudent(self):
        if self.w is None:
            self.w = AddStudent()
            self.w.show()
        else:
            self.w.close()
            self.w = None

    def showAddInstructor(self):
        if self.w is None:
            self.w = AddInstructor()
            self.w.show()
        else:
            self.w.close()
            self.w = None

    def showSection(self):
        if self.w is None:
            self.w = editSection()
            self.w.show()
        else:
            self.w.close()
            self.w = None

    def showRegisterStudent(self):
        if self.w is None:
            self.w = RegisterStudent()
            self.w.show()
        else:
            self.w.close()
            self.w = None

    def showRemoveFlag(self):
        if self.w is None:
            self.w = RemoveFlag()
            self.w.show()
        else:
            self.w.close()
            self.w = None

    def showPrintStudentDetail(self):
        if self.w is None:
            self.w = PrintStudentDetails()
            self.w.show()
        else:
            self.w.close()
            self.w = None

    def showCourse(self):
        if self.w is None:
            self.w = editCourse()
            self.w.show()
        else:
            self.w.close()
            self.w = None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
