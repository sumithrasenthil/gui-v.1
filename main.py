import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtGui import QMovie, QPainter, QPixmap
from PyQt5.QtCore import QRect, pyqtSlot, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLineEdit, QMessageBox, QSizePolicy, QStyle, QLabel, QDialog


from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)
from   PyQt5.QtWidgets import *
from   PyQt5.QtGui     import *
from   PyQt5.QtCore    import *

GIF = 'charging1.gif'

from pprogress import External

StyleSheet = '''
QPushButton:hover#BlueButton
{
   background-color:green;
}

'''


TIME_LIMIT = 100


class VideoWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(VideoWindow, self).__init__(parent)

        self.title = "CAAS"
        self.top = 0
        self.left = 0
        self.width = 1400
        self.height = 1000
        self.Iconimage = "icon.png"

        self.InitWindow()
        self.show()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.Iconimage))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.Uicomponent()

    def Uicomponent(self):

        #Heading of the window .
        self.label = QtWidgets.QLabel(self)
        self.label.setText("<h1>ChargePay Welcomes You</h1>")
        self.label.setFont(QtGui.QFont("Bitter",20))
        self.label.setGeometry(QRect(150, 40, 925, 145))
        self.label.setStyleSheet('color:#1B9CFC')

        # welcome user heading
        
        self.label = QtWidgets.QLabel(self)
        self.label.setText("<h1>Welcome User</h1>")
        self.label.setFont(QtGui.QFont("Bitter",15))

        self.label.setGeometry(QRect(900, 170, 625, 145))
        self.label.setStyleSheet('color:#1B9CFC')
#         self.label.setFont(QtGui.QFont("Bitter"))
#         self.label2 = QLabel(self)
#         self.label2.setPixmap(QtGui.QPixmap('user2.png'))
#         self.label2.setGeometry(900,209, 30, 30)
#         self.label3 = QLabel(self)



        # state of charge
        self.button1 = QtWidgets.QLabel(self)
        self.button1.setText("<h1>Soc</3>")
        self.button1.setFont(QtGui.QFont("Bitter",13))

        #self.button1.setGeometry(QRect(900, 170, 625, 145))
        #self.button1.setStyleSheet('color:darkred')
        #button1 = QPushButton(" SOC ", self)
        #button1.setStyleSheet('QPushButton {background-color: black ,color: darkred;}')
        #button1.setStyleSheet('color:darkblack')

        self.button1.setGeometry(QRect(940, 300, 100, 45))
#         self.button1.resize(70, 55)
        self.button1.setToolTip("STATE OF CHARGE")

        # soc output
        button1 = QPushButton("  ", self)
        button1.setGeometry(QRect(1070, 300, 80, 55))
        button1.resize(100, 45)
        button1.setToolTip("STATE OF CHARGE")

        # required units
        self.button1 = QtWidgets.QLabel(self)
        self.button1.setText("<h1>Units</3>")
        self.button1.setFont(QtGui.QFont("Bitter",13))

        self.button1.setGeometry(QRect(940, 370, 100, 45))
        #button1.resize(50, 35)
        #button1.setToolTip("Units needed for the user ")

        # input fields for charging
        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(QRect(1070, 370, 700, 145))
        self.textbox.resize(100, 45)

        # Create a button in the window
        self.button2 = QPushButton("Charge", self)
        self.button2.setGeometry(QRect(980, 500, 180, 60))
        self.button2.setStyleSheet('color:darkred')
        #self.button2.setStyleSheet('QPushButton{background-color:black;color:red;}')
        self.button2.setFont(QtGui.QFont("Bitter",23))

        self.button2.setIcon(QtGui.QIcon("icon.png"))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.setToolTip("Proceed to Charge")
        self.lineEdit1 = QLineEdit("Type here what you want to transfer for [Window1].", self)

        # connect button to function on_click
        self.button2.clicked.connect(self.on_click)

        self.button2.clicked.connect(self.button2_onClick)

        #contact
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<h1>Contact</h1>")
        self.label1.setGeometry(QRect(940, 640, 400, 45))
        self.label1.setStyleSheet('color:#1B9CFC')
        self.label1.setFont(QtGui.QFont("Bitter",15))

        #self.label2 = QLabel(self)
        #self.label2.setPixmap(QtGui.QPixmap('contact1.png'))
        #self.label2.setGeometry(910, 640, 40, 40)
        # self.label3 = QLabel(self)
        # self.label3.setPixmap(QtGui.QPixmap('line.png'))
        # self.label3.setGeometry(540, 375, 200, 10)
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<h2>xyz@gmail.com</h2>")
        self.label1.setGeometry(QRect(985, 710, 400, 45))
        self.label2 = QLabel(self) # self.setGeometry(self.left, self.top, self.width, self.height)

        #self.label2.setPixmap(QtGui.QPixmap('gmail.png'))
        #self.label2.setGeometry(955, 705, 35, 35)
        #self.label3 = QLabel(self)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<h2>1223-3542-2334</h2>")
        self.label1.setGeometry(QRect(985, 765, 400, 45))
        self.label2 = QLabel(self)
        #self.label2.setPixmap(QtGui.QPixmap('phone2.png'))
        #self.label2.setGeometry(960,740, 40, 40)
        #self.label3 = QLabel(self)




        # visit again..
        
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<h1>Reduce Your Footprint</h1>")
        self.label1.setFont(QtGui.QFont("Bitter",17))
        self.label1.setGeometry(QRect(100, 735, 925, 145))
        self.label1.setStyleSheet('color:#4caf50')
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("<h1>And</h1>")
        self.label2.setFont(QtGui.QFont("Bitter",17))
        self.label2.setGeometry(QRect(390, 800, 925, 145))
        self.label2.setStyleSheet('color:#4caf50')
        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("<h1>Go  Green !!!</h1>")
        self.label3.setFont(QtGui.QFont("Bitter",17))
        self.label3.setGeometry(QRect(280, 865, 925, 145))
        self.label3.setStyleSheet('color:#4caf50')

        
        
        
        
        #self.label1 = QtWidgets.QLabel(self)
        #self.label1.setText("<h1> VISIT AGAIN !!!</h1>")
        #self.label1.setGeometry(QRect(470, 880, 400, 45))
        #self.label1.setStyleSheet('color:darkred')
        #self.label2 = QLabel(self)
        #self.label2.setPixmap(QtGui.QPixmap('redheart2.png'))
        #self.label2.setGeometry(560, 900, 64, 64)
        #self.label2.setFont(QtGui.QFont("Bitter",20))


        # self.label = QLabel(self)
        # self.label.setPixmap(QPixmap('payment5.jpg'))
        # self.label.setGeometry(40, 50, 400, 400)


        self.show()

        # buttonWindow1 = QPushButton('Window1', self)
        # buttonWindow1.move(100, 100)
        # buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
        # self.lineEdit1 = QLineEdit("Type here what you want to transfer for [Window1].", self)
        # self.lineEdit1.setGeometry(250, 100, 400, 30)

        #video player code
        self.mediaPlayer = QtMultimedia.QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)

        videoWidget = QtMultimediaWidgets.QVideoWidget()

        container = QtWidgets.QWidget()
        lay = QtWidgets.QVBoxLayout(container)
        lay.setContentsMargins(50, 130, 550, 10)

        lay.addWidget(videoWidget)



        self.playButton = QtWidgets.QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)


        self.errorLabel = QtWidgets.QLabel()
        self.errorLabel.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                      QtWidgets.QSizePolicy.Maximum)

        # Create new action
        openAction = QtWidgets.QAction(QtGui.QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('CAAS')
        openAction.triggered.connect(self.openFile)

        # Create exit action
        exitAction = QtWidgets.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        # # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        # fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

        # # Create a widget for window contents
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)

        # Create layouts to place inside widget
        controlLayout = QtWidgets.QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 550, 200)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(container)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)

        # Set widget to contain window contents
        wid.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

     # Onclick function for units to charge
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        print(textboxValue)

        self.textbox.setText("")
        
    @pyqtSlot()
    def button2_onClick(self):
        self.statusBar().showMessage("Switched to window 1")
        self.cams = Window1(self.lineEdit1.text())
        self.cams.show()
        self.close()
    

    # video player code
    def openFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Movie",
                                                            QtCore.QDir.homePath())

        if fileName:
            self.mediaPlayer.setMedia(
                QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def play(self):
        if self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

class Window1(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)

        self.top = 0
        self.left = 100
        self.width = 1400
        self.height = 1000
        self.InitUI()
        # player.resize(2100, 3470)

    def InitUI(self):
        
       
        #self.movie = QMovie("charging1.gif")
        #self.movie.frameChanged.connect(self.repaint)
        #self.movie.setGeometry(100, 100, 800, 800)
        
        #self.movie.start()

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('testing3.jpeg'))
        self.label.setGeometry(100, 150, 600, 600)
        #self.show()

        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle('Amount')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
         
        
         

        # second window Header
        self.label = QtWidgets.QLabel(self)
        self.label.setText("<h1>ChargePay Welcomes you</h1>")
        self.label.setGeometry(QRect(150, 20, 925, 145))
        self.label.setFont(QtGui.QFont("Bitter",20))
        self.label.setStyleSheet('color:darkblue')
        

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<h1>Hello User</h1>")
        #self.label.setGeometry(QRect(900, 170, 625, 145))
        self.label1.setGeometry(QRect(930, 150, 525, 145))
        self.label1.setStyleSheet('color:darkblue')
        self.label1.setFont(QtGui.QFont("Bitter",18))
        
        
        
        button1 = QtWidgets.QLabel(self)
        button1.setText("<h1>Amount</h1>")
        button1.setFont(QtGui.QFont("Bitter",13))
        button1.setStyleSheet('color:darkblack')

        button1.setGeometry(QRect(910, 320, 150, 45))
        
        

        #  Amount output
        button1 = QPushButton("  ", self)
        button1.setGeometry(QRect(1100, 320, 100, 45))
        button1.resize(100, 45)
        button1.setToolTip("Amount for the respective units")

        # Progress bar header
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<h1>Charging</h1>")
        self.label1.setFont(QtGui.QFont("Bitter",13))
        self.label1.setGeometry(QRect(955,415,190,45))
        self.label1.setStyleSheet('color:darkblue')

        #Progress bar for charging
        self.progress = QProgressBar(self)
        self.progress.setGeometry(995, 525, 200, 25)
        self.progress.setMaximum(100)
        self.button = QPushButton('start', self)
        self.button.setGeometry(1000, 575, 100, 30)
        self.button.clicked.connect(self.onButtonClick)
        
     
        
        
        
#         

        #Bach button for first window
        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Back')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)


        # thanksGiving for user
           
        self.label = QtWidgets.QLabel(self)
        self.label.setText("<h1>Thanks for Charging</h1>")
        self.label.setFont(QtGui.QFont("Bitter",20))
        self.label.setGeometry(QRect(300, 775, 925, 145))
        self.label.setStyleSheet('color:darkred')

        
        
        
        
        #self.label1 = QtWidgets.QLabel(self)
        #self.label1.setText("<h1> VISIT AGAIN !!!</h1>")
        #self.label1.setGeometry(QRect(470, 880, 400, 45))
        #self.label1.setStyleSheet('color:darkred')
        #self.label2 = QLabel(self)
        #self.label2.setPixmap(QtGui.QPixmap('redheart2.png'))
        #self.label2.setGeometry(560, 900, 64, 64)
        # icon
        # self.label3= QtWidgets.QLabel(self)
        # self.label3.setText("<h3>HAPPY JOURNEY</h2>")
        # self.label3.setGeometry(QRect(600, 250, 100, 45))
        # self.label3.setIcon(QtGui.QIcon("heart1.png"))
        # self.label3.setIconSize(QtCore.QSize(30, 30))
        # self.label3.setToolTip("Proceed to Charge")
        #self.lineEdit1 = QLineEdit("Type here what you want to transfer for [Window1].", selfdef onButtonClick(self):
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()
        
    def onButtonClick(self):
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()
    

    def onCountChanged(self, value):
        self.progress.setValue(value)

    def goMainWindow(self):
        self.cams = VideoWindow()
        self.cams.show()
        self.close()
class External(QThread):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)

    def run(self):
        count = 0
        while count < TIME_LIMIT:
            count += 10
            time.sleep(1)
            self.countChanged.emit(count)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    player = VideoWindow()
    # amount=Window1()
    # amount.resize(2100,3470)
#     player.resize(1500, 1020)
    player.show()
    # amount.show()
    sys.exit(app.exec_())

