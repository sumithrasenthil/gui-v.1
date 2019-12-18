import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtCore import QRect, pyqtSlot, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLineEdit, QMessageBox, QSizePolicy, QStyle, QLabel, QDialog


from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)

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
        self.left = 100
        self.width = 2100
        self.height = 3470
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
        self.label.setText("<h1>CHARGEPAY WELCOMES YOU</h2>")
        self.label.setGeometry(QRect(750, -15, 525, 145))
        self.label.setStyleSheet('color:darkblack')

        # welcome user heading
        self.label = QtWidgets.QLabel(self)
        self.label.setText("<h2>Welcome User</h3>")
        self.label.setGeometry(QRect(1550, 110, 525, 145))
        self.label.setStyleSheet('color:darkred')
        self.label2 = QLabel(self)
        self.label2.setPixmap(QtGui.QPixmap('user2.png'))
        self.label2.setGeometry(1500,159, 40, 40)
        self.label3 = QLabel(self)



        # state of charge
        button1 = QPushButton(" SOC ", self)
        button1.setStyleSheet('QPushButton {background-color: black ,color: darkred;}')

        button1.setGeometry(QRect(1540, 270, 100, 45))
        button1.resize(50, 35)
        button1.setToolTip("STATE OF CHARGE")

        # soc output
        button1 = QPushButton("  ", self)
        button1.setGeometry(QRect(1670, 270, 100, 45))
        button1.resize(60, 35)
        button1.setToolTip("STATE OF CHARGE")

        # required units
        button1 = QPushButton(" UNITS ", self)

        button1.setGeometry(QRect(1540, 370, 100, 45))
        button1.resize(50, 35)
        button1.setToolTip("Units needed for the user ")

        # input fields for charging
        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(QRect(1670, 370, 100, 45))
        self.textbox.resize(60, 35)

        # Create a button in the window
        self.button2 = QPushButton("Charge  ", self)
        self.button2.setGeometry(QRect(1580, 470, 100, 45))
        self.button2.setStyleSheet('color:darkred')
        self.button2.setIcon(QtGui.QIcon("icon.png"))
        self.button2.setIconSize(QtCore.QSize(30, 30))
        self.button2.setToolTip("Proceed to Charge")
        self.lineEdit1 = QLineEdit("Type here what you want to transfer for [Window1].", self)

        # connect button to function on_click
        self.button2.clicked.connect(self.on_click)

        self.button2.clicked.connect(self.button2_onClick)

        #contact
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<h3>Contact</h2>")
        self.label1.setGeometry(QRect(1540, 640, 400, 45))
        self.label1.setStyleSheet('color:darkred')
        self.label2 = QLabel(self)
        self.label2.setPixmap(QtGui.QPixmap('contact1.png'))
        self.label2.setGeometry(1510, 640, 40, 40)
        # self.label3 = QLabel(self)
        # self.label3.setPixmap(QtGui.QPixmap('line.png'))
        # self.label3.setGeometry(540, 375, 200, 10)
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<h4>xyz@gmail.com</h4>")
        self.label1.setGeometry(QRect(1585, 700, 400, 45))
        self.label2 = QLabel(self) # self.setGeometry(self.left, self.top, self.width, self.height)

        self.label2.setPixmap(QtGui.QPixmap('gmail.png'))
        self.label2.setGeometry(1555, 705, 35, 35)
        self.label3 = QLabel(self)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<h4>1223-3542-2334</h4>")
        self.label1.setGeometry(QRect(1585, 735, 400, 45))
        self.label2 = QLabel(self)
        self.label2.setPixmap(QtGui.QPixmap('phone2.png'))
        self.label2.setGeometry(1560,740, 40, 40)
        self.label3 = QLabel(self)




        # visit again..
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<h3> VISIT AGAIN !!!</h2>")
        self.label1.setGeometry(QRect(1570, 810, 400, 45))
        self.label1.setStyleSheet('color:darkred')
        self.label2 = QLabel(self)
        self.label2.setPixmap(QtGui.QPixmap('heart5.png'))
        self.label2.setGeometry(1530, 810, 40, 40)

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
        lay.setContentsMargins(50, 100, 550, 10)

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
        controlLayout.setContentsMargins(0, 0, 550, 0)
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
        self.width = 2100
        self.height = 3470
        self.InitUI()
        # player.resize(2100, 3470)

    def InitUI(self):

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('payment5.jpg'))
        self.label.setGeometry(0, 0, 3800, 400)
        # self.show()

        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle('Amount')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))


        # second window Header
        self.label = QtWidgets.QLabel(self)
        self.label.setText("<h2>ChargePay Welcomes you</h2>")
        self.label.setGeometry(QRect(275, -30, 525, 145))
        self.label.setStyleSheet('color:darkred')

        # amount Input
        button1 = QPushButton(" Amount ", self)
        button1.setGeometry(QRect(1510, 100, 100, 45))
        button1.resize(60, 35)
        button1.setToolTip("Amount")

        #  Amount output
        button1 = QPushButton("  ", self)
        button1.setGeometry(QRect(1650, 100, 100, 45))
        button1.resize(60, 35)
        button1.setToolTip("Amount for the respective units")

        # Progress bar header
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<h3>Charging</h2>")
        self.label1.setGeometry(QRect(1555,165,100,45))
        self.label1.setStyleSheet('color:darkred')

        #Progress bar for charging
        self.progress = QProgressBar(self)
        self.progress.setGeometry(1510, 225, 200, 25)
        self.progress.setMaximum(100)
        self.button = QPushButton('start', self)
        self.button.move(1555, 270)

        self.button.clicked.connect(self.onButtonClick)


        #Bach button for first window
        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Back')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)


        # thanksGiving for user
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<h3>THANKS FOR COMING !!!</h2>")
        self.label1.setGeometry(QRect(1500, 350, 400, 45))
        self.label1.setStyleSheet('color:darkred')

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<h3>HAPPY JOURNEY</h2>")
        self.label1.setGeometry(QRect(1530, 380, 300, 45))
        self.label1.setStyleSheet('color:darkred')
        self.label2 = QLabel(self)
        self.label2.setPixmap(QtGui.QPixmap('heart5.png'))
        self.label2.setGeometry(1690, 380, 40, 40)

        # icon
        # self.label3= QtWidgets.QLabel(self)
        # self.label3.setText("<h3>HAPPY JOURNEY</h2>")
        # self.label3.setGeometry(QRect(600, 250, 100, 45))
        # self.label3.setIcon(QtGui.QIcon("heart1.png"))
        # self.label3.setIconSize(QtCore.QSize(30, 30))
        # self.label3.setToolTip("Proceed to Charge")
        # # self.lineEdit1 = QLineEdit("Type here what you want to transfer for [Window1].", self)

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
    player.resize(2100, 3470)
    player.show()
    # amount.show()
    sys.exit(app.exec_())
