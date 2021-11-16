from PyQt5 import QtWidgets, QtCore, QTGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import PyQt5.QtWidgets as qtw
import sys

#used for main menu
def clicked():
    print("clicked")

def otherWindow():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Main Menu")
    win.show()


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
    label.move(75,10)

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
    b1.clicked.connect(clicked)

    combo = QComboBox(win)
    combo.addItem("Faculty")
    combo.addItem("Student")
    combo.addItem("Course")
    combo.addItem("Section")

    combo.move(50, 225)

    win.show()
    sys.exit(app.exec_())
window()
class SampleDatabaseWin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 492)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.firstbutton = QtWidgets.QPushButton(self.centralwidget)
        self.firstbutton.setObjectName("firstbutton")
        self.horizontalLayout.addWidget(self.firstbutton)
        self.secondbutton = QtWidgets.QPushButton(self.centralwidget)
        self.secondbutton.setObjectName("secondbutton")
        self.horizontalLayout.addWidget(self.secondbutton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "First column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Second column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Third"))
        self.firstbutton.setText(_translate("MainWindow", "Add"))
        self.secondbutton.setText(_translate("MainWindow", "Delete"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())