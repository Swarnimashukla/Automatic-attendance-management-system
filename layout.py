from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QHBoxLayout, QGroupBox, QVBoxLayout,QLabel,QMainWindow,QWidget,QMessageBox
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap,QImage,QPalette,QBrush
from PyQt5 import QtGui,QtWidgets
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "ROLLCALL"
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 300
        self.iconName = "home.png"

        self.setStyleSheet("QPushButton{font-size: 18pt;font-weight: bold;}")

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateLayout()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)



    def CreateLayout(self):
        self.groupBox = QGroupBox("")
        hboxLayout = QHBoxLayout()

        palette = QtGui.QPalette()
        myPixmap = QtGui.QPixmap('./icon/bg2.jpeg')
        myScaledPixmap = myPixmap.scaled(self.size(), QtCore.Qt.KeepAspectRatio, transformMode = QtCore.Qt.SmoothTransformation)
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(myScaledPixmap))
        self.setPalette(palette)

        hboxLayout.setSpacing(60)

        self.button2 = QPushButton("Edit the time table")
        self.button2.setIcon(QtGui.QIcon("./icon/timetable.png"))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.setMinimumHeight(60)
        self.button2.clicked.connect(self.timetable)
        hboxLayout.addWidget(self.button2)

        self.button1 = QPushButton("Enroll Student")
        self.button1.setIcon(QtGui.QIcon("./icon/enroll1.png"))
        self.button1.setIconSize(QtCore.QSize(40, 40))
        self.button1.setMinimumHeight(60)
        self.button1.clicked.connect(self.enroll)
        hboxLayout.addWidget(self.button1)

        self.button3 = QPushButton("Model Last Trained")
        self.button3.setIcon(QtGui.QIcon("./icon/status.png"))
        self.button3.setIconSize(QtCore.QSize(40, 40))
        self.button3.setMinimumHeight(60)
        self.button3.clicked.connect(self.status)
        hboxLayout.addWidget(self.button3)

        self.button4 = QPushButton("Spreadsheet")
        self.button4.setIcon(QtGui.QIcon("./icon/spread.png"))
        self.button4.setIconSize(QtCore.QSize(40, 40))
        self.button4.setMinimumHeight(60)
        self.button4.clicked.connect(self.spreadsheet)
        hboxLayout.addWidget(self.button4)

        self.button5 = QPushButton("Detect")
        self.button5.setIcon(QtGui.QIcon("./icon/detect.png"))
        self.button5.setIconSize(QtCore.QSize(40, 40))
        self.button5.setMinimumHeight(60)
        self.button5.clicked.connect(self.detect)
        hboxLayout.addWidget(self.button5)

        self.button6 = QPushButton("Identify")
        self.button6.setIcon(QtGui.QIcon("./icon/identify.png"))
        self.button6.setIconSize(QtCore.QSize(40, 40))
        self.button6.setMinimumHeight(60)
        self.button6.clicked.connect(self.identify)
        hboxLayout.addWidget(self.button6)

        self.groupBox.setLayout(hboxLayout)

    def enroll(self):
        name, done1 = QtWidgets.QInputDialog.getText(
            self, 'Input Dialog', 'Enter your name:')

        if(done1 == True):
            roll, done2 = QtWidgets.QInputDialog.getText(
                self, 'Input Dialog', 'Enter your) roll:')
            Id = roll[-3:]

            if(done1 == True and done2 == True):
                mobileno , done3 = QtWidgets.QInputDialog.getText(
                    self,'Input Dialog','Enter Father\'s Mobile No:'
                )


        #print("Hello whats up")

        if(done1 == True and done2 == True and done3 == True):
            os.system("python3 add_student.py "+name+" "+roll+" "+mobileno)

            os.system("python3 create_person.py user"+Id)

            os.system("python3 add_person_faces.py user"+Id)

            os.system("python3 train.py")


    def timetable(self):

        os.system("python3 "+"./timetable/"+"time.py")

        print("timetable")


    def status(self):
        import get_status
        res = get_status.status()
        date = res[:10].split('-')
        time = res[11:19].split(':')
        date.reverse()
        time.reverse()
        s='-'
        date = s.join(date)
        s=':'
        time = s.join(time)
        QMessageBox.about(self,"Status", "The model was trained on "+date+" at "+time)

    def detect(self):

        os.system("python3 detect.py")
        self.SW = SecondWindow()
        self.SW.show()
        #print("detect")

    def spreadsheet(self):

        os.system("python3 spreadsheet.py")
        #print("spreadsheet")


    def identify(self):

        os.system("python3 identify.py")
        #print("identify ")


class SecondWindow(QMainWindow):
     def __init__(self):
         super().__init__()

         labelImage = QLabel(self)
         pixmap = QPixmap("./pics/framee1.jpg")
         labelImage.resize(pixmap.width(),pixmap.height())
         self.setGeometry(0, 0, pixmap.width(), pixmap.height())
         labelImage.setPixmap(pixmap.scaled(labelImage.size(), QtCore.Qt.IgnoreAspectRatio))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MW = Window()
    MW.show()
    sys.exit(app.exec())