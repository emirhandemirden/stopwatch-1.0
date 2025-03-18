import sys
from PyQt5.QtWidgets import (QApplication,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QPushButton)
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QIcon

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StopWatch 1.0")
        self.setWindowIcon(QIcon("stopwatch.ico"))
        self.setGeometry(1000,500,500,250)
        self.time = QTime(0,0,0,0)
        self.timeLabel = QLabel("00:00:00.00",self)
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.startButton = QPushButton("Start",self)
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.start)
        self.stopButton = QPushButton("Stop",self)
        self.stopButton.setObjectName("stopButton")
        self.stopButton.clicked.connect(self.stop)
        self.resetButton = QPushButton("Reset",self)
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(self.reset)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateDisplay)
        self.setStyleSheet("""
            QWidget {
                background-color: #141414;
                color: #cccccc;
            }
            QPushButton, Qlabel {
                font-family: montserrat;
                padding: 10px;
            }
            QLabel {
                font-weight: bold;
                font-size: 75px;    
            }
            QPushButton {
                font-size: 25px; 
                border: 1px solid;
                border-radius: 20px;
                margin: 15px 5px;
            }
            QPushButton#startButton { background-color: #42a5f5; }
            QPushButton#startButton:Hover { background-color: #90caf9; }
            QPushButton#stopButton { background-color: #f44336; }
            QPushButton#stopButton:Hover { background-color: #e57373; }
            QPushButton#resetButton { background-color: #f57c00; }
            QPushButton#resetButton:Hover { background-color: #ffa726; }
        """)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.timeLabel)
        hbox = QHBoxLayout()
        hbox.addWidget(self.startButton)
        hbox.addWidget(self.stopButton)
        hbox.addWidget(self.resetButton)
        self.setLayout(vbox)
        vbox.addLayout(hbox)

    def start(self):
        self.timer.start(10)
        self.startButton.setText("Continue")

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.timeLabel.setText(self.formatTime(self.time))
        self.startButton.setText("Start")

    def formatTime(self, time): 
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def updateDisplay(self):
        self.time = self.time.addMSecs(10)
        self.timeLabel.setText(self.formatTime(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())