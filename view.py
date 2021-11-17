import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, \
    QGridLayout
from PyQt5.QtCore import pyqtSlot, QSize


class AddStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Student')
        self.resize(200, 200)
        layout = QGridLayout()
        id1 = QLabel('<font size="4"> Username </font>')
        layout.addWidget(self.label)

        self.lineEditID = QLineEdit()
        self.lineEditID.setPlaceholderText("Student ID")
        layout.addWidget(id1, 0, 0)
        layout.addWidget(self.lineEditID, 0, 1)
        self.setLayout(layout)


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


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Main Menu")

    label = QtWidgets.QLabel(win)
    label.setText("Options: ")
    label.move(20, 10)

    label = QtWidgets.QLabel(win)
    label.setText("Choose an option: ")
    label.move(50, 180)

    label = QtWidgets.QLabel(win)
    label.setText("Faculty")
    label.move(75, 10)

    label = QtWidgets.QLabel(win)
    label.setText("Student")
    label.move(75, 30)

    label = QtWidgets.QLabel(win)
    label.setText("Course")
    label.move(75, 50)

    label = QtWidgets.QLabel(win)
    label.setText("Section")
    label.move(75, 70)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Choose")
    b1.move(170, 225)
    b1.clicked.connect()

    combo = QComboBox(win)
    combo.addItem("Faculty")
    combo.addItem("Student")
    combo.addItem("Course")
    combo.addItem("Section")

    combo.move(50, 225)

    win.show()
    sys.exit(app.exec_())
