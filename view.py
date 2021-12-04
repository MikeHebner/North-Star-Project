import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, \
    QGridLayout, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import pyqtSlot, QSize, Qt
import PyQt5.QtWidgets as qtw
import sqlite3 as sql
import model


class AddStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.textbox2 = QLineEdit(self)
        self.textbox = QLineEdit(self)
        self.msg = QMessageBox(self)
        self.prompt = QLabel(self)
        self.w = None
        self.setWindowTitle('Student Database')
        self.resize(200, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()

    def initUI(self):
        self.textbox.setPlaceholderText("Enter Student Name")
        self.textbox.move(20, 20)
        self.textbox.resize(150, 30)
        self.textbox.setStyleSheet("border: 1px solid black;")
        self.textbox2.setPlaceholderText("Enter Student ID")
        self.textbox2.move(20, 60)
        self.textbox2.resize(150, 30)
        self.prompt.setText("ADD - name & ID\n"
                            "REMOVE - ID\n"
                            "EDIT - new name & ID\n")
        self.prompt.move(20, 95)
        self.prompt.resize(150, 45)
        button = QPushButton("Add Student", self)
        button.resize(150, 40)
        button.move(20, 140)
        button.clicked.connect(self.addClick)
        button2 = QPushButton("Remove Student", self)
        button2.resize(150, 40)
        button2.move(20, 180)
        button2.clicked.connect(self.remClick)
        button3 = QPushButton("Edit Student Info", self)
        button3.clicked.connect(self.editClick)
        button3.resize(150, 40)
        button3.move(20, 220)

    def addClick(self):
        try:
            studentID = self.textbox2.text()
            studentName = self.textbox.text()
            print("Name:" + studentName + " ID:" + studentID)
            model.Student.add(studentID, studentName)
        except Exception as e:
            print("Oops!", e, "occurred.")
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Error")
            self.msg.setInformativeText('That name or ID already exists in this table')
            self.msg.setWindowTitle("Error")
            self.msg.exec_()


    def remClick(self):
        studentID = self.textbox2.text()
        model.Student.remove(studentID)

    def editClick(self):
        studentID = self.textbox2.text()
        newName = self.textbox.text()
        model.Student.editStudentInfo(newName, studentID)


class AddInstructor(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.prompt = QLabel(self)
        self.msg = QMessageBox(self)
        self.textbox2 = QLineEdit(self)
        self.textbox = QLineEdit(self)
        self.setWindowTitle('Instructor Database')
        self.resize(200, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUi()

    def initUi(self):
        self.textbox.setPlaceholderText("Enter Instructor Name")
        self.textbox.move(20, 20)
        self.textbox.resize(150, 30)
        self.textbox2.setPlaceholderText("Enter Instructor ID")
        self.textbox2.move(20, 60)
        self.textbox2.resize(150, 30)
        self.prompt.setText("ADD - name & ID\n"
                            "REMOVE - ID\n"
                            "EDIT - new name & ID\n")
        self.prompt.move(20, 95)
        self.prompt.resize(150, 45)
        button = QPushButton("Add Instructor", self)
        button.resize(150, 40)
        button.move(20, 140)
        button.clicked.connect(self.addClick)
        button2 = QPushButton("Remove Instructor", self)
        button2.resize(150, 40)
        button2.move(20, 180)
        button2.clicked.connect(self.remClick)
        button3 = QPushButton("Edit Instructor Info", self)
        button3.clicked.connect(self.editClick)
        button3.resize(150, 40)
        button3.move(20, 220)

    def editClick(self):
        instructorID = self.textbox2.text()
        newName = self.textbox.text()
        model.Instructor.editInstructorInfo(newName, instructorID)

    def addClick(self):
        try:
            instructorID = self.textbox2.text()
            instructorName = self.textbox.text()
            print("Name:" + instructorName + " ID:" + instructorID)
            model.Instructor.add(instructorID, instructorName)
        except Exception as e:
            print("Oops!", e, "occurred.")
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Error")
            self.msg.setInformativeText('That name or ID already exists in this table')
            self.msg.setWindowTitle("Error")
            self.msg.exec_()

    def remClick(self):
        instructorID = self.textbox2.text()
        model.Instructor.remove(instructorID)


class RegisterStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Student Course')
        self.resize(200, 200)
        self.label = QLabel(self)

        self.textbox = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox3 = QLineEdit(self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUi()

    def initUi(self):
        self.label.move(20, 5)
        self.label.resize(150, 30)
        self.textbox.setPlaceholderText("Enter Course ID")
        self.textbox.move(20, 20)
        self.textbox.resize(160, 30)
        self.textbox2.setPlaceholderText("Enter Course Description")
        self.textbox2.move(20, 60)
        self.textbox2.resize(160, 30)
        self.textbox3.setPlaceholderText("Enter Credits")
        self.textbox3.move(20, 100)
        self.textbox3.resize(160, 30)
        button = QPushButton("Register Student", self)
        button.move(20, 160)
        button.resize(150, 40)
        button.clicked.connect(self.addClick)

    def addClick(self):
        courseID = self.textbox.text().upper()
        sectionID = self.textbox3.text()
        studentID = self.textbox2.text()
        flag = 'None'
        course_link = model.Enrollment.getCourseLink(sectionID, courseID)
        course_link = str(course_link)
        duplicateCheck = model.Enrollment.checkDuplicate(studentID, course_link)
        if duplicateCheck > 0:
            self.label.setText("Student already enrolled")
        else:
            course_link = course_link[1]
            sa = model.Enrollment.checkCap(int(course_link))[0][0]
            print(sa)
            if sa == 0:
                print("OVER CAPACITY FLAG")
                flag = "Over Capacity"
                model.Enrollment.add(flag, studentID, course_link)
            elif model.Enrollment.getEnrolledCreds(studentID) > 12:
                print("EXCESS CRED")
                flag = "Excess Cred"
                model.Enrollment.add(flag, studentID, course_link)
            else:
                model.Enrollment.add(flag, studentID, course_link)


class RemoveFlag(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle('Remove Flag')
        self.resize(200, 200)
        self.textbox = QLineEdit(self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUi()

    def initUi(self):
        self.textbox.setPlaceholderText("Enter Student ID")
        self.textbox.move(20, 20)
        self.textbox.resize(150, 30)
        button = QPushButton("Search", self)
        button.move(20, 100)
        button.clicked.connect(self.showFlags)
        button2 = QPushButton("Exit", self)
        button2.move(20, 140)
        button2.clicked.connect(lambda: self.close())

    # def initUi(self):
    # self.textbox.setPlaceholderText("Enter Student ID")
    # self.textbox.move(20, 20)
    # self.textbox.resize(150, 30)
    # button = QPushButton("Search", self)
    # button.move(20, 100)
    # button.clicked.connect(self.showFlags)
    # button2 = QPushButton("Exit", self)
    # button2.move(20, 140)
    # button2.clicked.connect(lambda: self.close())

    def showFlags(self):
        if self.w is None:
            self.w = rFlag(self.textbox.text())
            self.w.show()
        else:
            self.w.close()
            self.w = None


class rFlag(QWidget):
    def __init__(self, student_id):
        super().__init__()
        self.student_id = student_id
        self.setWindowTitle('Flag Removal')
        self.resize(500, 500)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.textbox = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.initUI()
        self.createTable()

    def initUI(self):
        self.createTable()
        semID = QLabel(self)
        semID.setText("Fall 2021")
        semID.move(150, 20)
        semID.resize(150, 40)
        semID.adjustSize()
        studentDetails = QLabel(self)
        studentName = model.Student.getName(self.student_id)[0]
        studentDetails.setText(str(studentName) + "  ID:" + self.student_id)
        studentDetails.move(150, 40)
        studentDetails.resize(150, 40)
        studentDetails.adjustSize()
        label = QLabel(self)
        label.setText("ENTER COURSE_ID AND SECTION_ID\nOF FLAGGED COURSE\nTO BE REMOVE FLAG")
        label.move(220, 100)
        label.resize(200,50)
        self.textbox.setPlaceholderText("Enter Course ID")
        self.textbox.move(275, 150)
        self.textbox.resize(200, 50)
        self.textbox2.setPlaceholderText("Enter Section ID")
        self.textbox2.move(275, 200)
        self.textbox2.resize(200, 50)
        submit = QPushButton("Submit", self)
        submit.clicked.connect(self.submitClick)
        submit.move(300, 250)


    def createTable(self):
        data = model.Enrollment.getIt(self.student_id)
        totalCredits = model.Enrollment.getEnrolledCreds(self.student_id)
        rowCount = model.Enrollment.enrolledCount(self.student_id)

        table = QTableWidget(self)
        table.setColumnCount(3)
        table.setRowCount(rowCount)
        table.move(0, 100)
        table.setMinimumSize(220, 150)

        table.setHorizontalHeaderLabels(("Course ID;Section;Course Flags").split(";"))
        for i in range(rowCount):
            for j in range(3):
                table.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        table.resizeColumnsToContents()
        table.resizeRowsToContents()


    def submitClick(self):
        courseID = self.textbox.text().upper()
        sectionID = self.textbox2.text()
        course_link = model.Enrollment.getCourseLink(sectionID,courseID)
        model.Enrollment.removeFlag(self.student_id,course_link[0])




class PrintStudentDetails(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.textbox = QLineEdit(self)
        self.setWindowTitle('Student Details')
        self.resize(200, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUi()

    def initUi(self):
        self.textbox.setPlaceholderText("Enter Student ID")
        self.textbox.move(20, 20)
        self.textbox.resize(150, 30)
        button = QPushButton("Search", self)
        button.move(20, 100)
        button.clicked.connect(self.showStudentInfo)
        button2 = QPushButton("Exit", self)
        button2.move(20, 140)
        button2.clicked.connect(lambda: self.close())

    def showStudentInfo(self):
        if self.w is None:
            self.w = studentDetails(self.textbox.text())
            self.w.show()
        else:
            self.w.close()
            self.w = None


class studentDetails(QWidget):
    def __init__(self, student_id):
        super().__init__()
        self.student_id = student_id
        self.setWindowTitle('Student Details')
        self.resize(600, 400)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()

    def initUI(self):
        self.createTable()
        semID = QLabel(self)
        semID.setText("Fall 2021")
        semID.move(150, 20)
        semID.resize(150, 40)
        semID.adjustSize()
        studentDetails = QLabel(self)
        studentName = model.Student.getName(self.student_id)[0]
        studentDetails.setText(str(studentName) + "  ID:" + self.student_id)
        studentDetails.move(150, 40)
        studentDetails.resize(150, 40)
        studentDetails.adjustSize()

    def createTable(self):
        data = model.Enrollment.getEnrollmentDetails(self.student_id)
        totalCredits = model.Enrollment.getEnrolledCreds(self.student_id)
        rowCount = model.Enrollment.enrolledCount(self.student_id)
        table = QTableWidget(self)
        table.setColumnCount(5)
        table.setRowCount(rowCount + 2)
        table.move(0, 100)
        table.setMinimumSize(700, 500)

        table.setHorizontalHeaderLabels(("Course Description;Course ID;Instructor;Credits;Course Flags").split(";"))
        for i in range(rowCount):
            for j in range(5):
                table.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        for i in range(5):
            table.setItem(rowCount, i, QTableWidgetItem(""))
            table.item(rowCount, i).setBackground(QtGui.QColor(0, 0, 0))
        table.setItem(rowCount + 1, 0, QTableWidgetItem("Total Credits"))
        table.setItem(rowCount + 1, 1, QTableWidgetItem(str(totalCredits)))
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        exit = QPushButton("OK", self)
        exit.clicked.connect(lambda: self.close())
        exit.move(300, 250)


class editSection(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Section")
        self.resize(250, 300)
        self.textbox = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox3 = QLineEdit(self)
        self.textbox4 = QLineEdit(self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()

    def initUI(self):
        self.textbox.setPlaceholderText("Enter Course ID")
        self.textbox.move(20, 20)
        self.textbox.resize(150, 30)
        self.textbox2.setPlaceholderText("Enter New Section ID")
        self.textbox2.move(20, 60)
        self.textbox2.resize(150, 30)
        self.textbox3.setPlaceholderText("Enter Instructor ID")
        self.textbox3.move(20, 100)
        self.textbox3.resize(150, 30)
        self.textbox4.setPlaceholderText("Enter Capacity")
        self.textbox4.move(20, 140)
        self.textbox4.resize(150, 30)
        button = QPushButton("Add Section to Course", self)
        button.clicked.connect(self.addClick)
        button.move(20, 180)
        button.resize(150, 30)
        button.clicked.connect(self.addClick)

    def addClick(self):
        course_ID = self.textbox.text().upper()
        section_ID = self.textbox2.text()
        instructor_ID = self.textbox3.text()
        capacity = self.textbox4.text()
        print(model.Section.add(section_ID, capacity, course_ID, instructor_ID))


class addCourse(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Course")
        self.resize(200, 300)
        self.textbox = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox3 = QLineEdit(self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()

    def initUI(self):
        self.textbox.setPlaceholderText("Enter Course Description")
        self.textbox.move(20, 20)
        self.textbox.resize(150, 30)
        self.textbox2.setPlaceholderText("Enter Course ID")
        self.textbox2.move(20, 60)
        self.textbox2.resize(150, 30)
        self.textbox3.setPlaceholderText("Enter Course Credits")
        self.textbox3.move(20, 100)
        self.textbox3.resize(150, 30)
        button = QPushButton("Add Course", self)
        button.move(20, 140)
        button.resize(150, 30)
        button.clicked.connect(self.addClick)

    def addClick(self):
        course_desc = self.textbox.text()
        course_ID = self.textbox2.text()
        course_creds = self.textbox3.text()
        print(model.Course.add(course_desc, course_ID, course_creds))


class modifyDescription(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle('Modify Description')
        self.resize(200, 300)
        self.textbox = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()

    def initUI(self):
        self.textbox.setPlaceholderText("Enter Course ID")
        self.textbox.move(20, 20)
        self.textbox.resize(150, 30)
        self.textbox2.setPlaceholderText("Enter modified Description")
        self.textbox2.move(20, 40)
        self.textbox2.resize(150, 30)
        search = QPushButton("Submit", self)
        search.move(20, 200)
        search.clicked.connect(self.modDescription)

    def showDescription(self):
        if self.w is None:
            self.w = description()
            self.w.show()
        else:
            self.w.close()
            self.w = None

    def modDescription(self):
        course_id = self.textbox.text().upper()
        course_desc = self.textbox2.text()
        model.Course.editDescription(course_desc, course_id)
        print(course_id, course_desc)


class description(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Modify Description')
        self.resize(200, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUI()

    def initUI(self):
        textbox = QLineEdit(self)
        textbox.setPlaceholderText("Description")
        textbox.move(20, 20)
        textbox.resize(150, 30)
        textbox.setStyleSheet("border: 1px solid black;")
        textbox2 = QLineEdit(self)
        textbox2.setPlaceholderText("Course ID")
        textbox2.move(20, 60)
        textbox2.resize(150, 30)
        textbox3 = QLineEdit(self)
        textbox3.setPlaceholderText("Credits")
        textbox3.move(20, 100)
        textbox3.resize(150, 30)
        button2 = QPushButton("ADD", self)
        button2.resize(150, 40)
        button2.move(20, 140)


class unenrollStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle('Unenroll Student')
        self.resize(200, 200)
        self.textbox = QLineEdit(self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.initUi()

    def initUi(self):
        self.textbox.setPlaceholderText("Enter Student ID")
        self.textbox.move(20, 20)
        self.textbox.resize(150, 30)
        button = QPushButton("Search", self)
        button.move(20, 100)
        button.clicked.connect(self.showCourses)
        button2 = QPushButton("Exit", self)
        button2.move(20, 140)
        button2.clicked.connect(lambda: self.close())

    def showCourses(self):
        if self.w is None:
            self.w = courses(self.textbox.text())
            self.w.show()
        else:
            self.w.close()
            self.w = None


class courses(QWidget):
    def __init__(self, student_id):
        super().__init__()
        self.student_id = student_id
        self.setWindowTitle('Student Unenrollment')
        self.resize(500, 500)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.initUI()
        self.createTable()

    def initUI(self):
        self.createTable()
        semID = QLabel(self)
        semID.setText("Fall 2021")
        semID.move(150, 20)
        semID.resize(150, 40)
        semID.adjustSize()
        studentDetails = QLabel(self)
        studentName = model.Student.getName(self.student_id)[0]
        studentDetails.setText(str(studentName) + "  ID:" + self.student_id)
        studentDetails.move(150, 40)
        studentDetails.resize(150, 40)
        studentDetails.adjustSize()

    def createTable(self):
        data = model.Enrollment.getEnrollmentDetails(self.student_id)
        totalCredits = model.Enrollment.getEnrolledCreds(self.student_id)
        rowCount = model.Enrollment.enrolledCount(self.student_id)
        table = QTableWidget(self)
        table.setColumnCount(5)
        table.setRowCount(rowCount + 2)
        table.move(0, 100)
        table.setMinimumSize(700, 500)

        table.setHorizontalHeaderLabels(("Course Description;Course ID;Instructor;Credits;Course Flags").split(";"))
        for i in range(rowCount):
            for j in range(5):
                table.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        for i in range(5):
            table.setItem(rowCount, i, QTableWidgetItem(""))
            table.item(rowCount, i).setBackground(QtGui.QColor(0, 0, 0))
        table.setItem(rowCount + 1, 0, QTableWidgetItem("Total Credits"))
        table.setItem(rowCount + 1, 1, QTableWidgetItem(str(totalCredits)))
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        exit = QPushButton("OK", self)
        exit.clicked.connect(lambda: self.close())
        exit.move(300, 250)


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

        pybutton5 = QPushButton("Enroll in Course", self)
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

        pybutton9 = QPushButton("Modify Description", self)
        pybutton9.clicked.connect(self.showModifyDescription)
        pybutton9.resize(120, 40)
        pybutton9.move(20, 190)

        pybutton10 = QPushButton("Unenroll in Course", self)
        pybutton10.clicked.connect(self.showUnenrollStudent)
        pybutton10.resize(150, 40)
        pybutton10.move(160, 150)

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
            self.w = addCourse()
            self.w.show()
        else:
            self.w.close()
            self.w = None

    def showModifyDescription(self):
        if self.w is None:
            self.w = modifyDescription()
            self.w.show()
        else:
            self.w.close()
            self.w = None

    def showUnenrollStudent(self):
        if self.w is None:
            self.w = unenrollStudent()
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
