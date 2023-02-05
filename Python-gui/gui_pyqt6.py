from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import os
import command
import subprocess
from subprocess import call,Popen
import sys
 
 
class Window(QWidget):
    def clicked():
        os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
    def __init__(self):
        super().__init__()

        def button3_clicked():
            #os.system("start cmd /K wsl.exe --distribution Ubuntu-20.04 |rosversion -d")
            #call(["gnome-terminal", "-x", "sh", "-c", "python3; bash"])
            os.system("powershell.exe -x python gui_pyqt6.py")

        def button4_clicked():
            os.system("rosverion -d")
            
            
            
            
            

        
        self.resize(500, 300)
        self.setWindowTitle("ROS setup gui")
        self.setWindowIcon(QtGui.QIcon('ROS.jpg'))
 
        button = QPushButton("set ROS1 Noetic", self)
        button.setIcon(QIcon('ros-noetic-ninjemys.svg'))
        button.move(100, 100)

        button2 = QPushButton("set ROS2 Foxy", self)
        button2.setIcon(QIcon('foxy.png'))
        button2.move(300, 100)

        button3 = QPushButton("Open new terminal", self)
        button3.clicked.connect(button3_clicked)
        button3.move(100, 200)

        button4 = QPushButton("Install packages using github link", self)
        button4.move(300, 200)

        button4 = QPushButton("Check ROS version", self)
        button4.clicked.connect(button4_clicked)
        button4.move(200, 250)
        
    
 
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
