from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import year_wise
import main_analysis
import particular_match_record
import pandas as pd
import matplotlib.pyplot as plt
#from PyQt5.QtGui import QIcon, QPixmap
import os
data = pd.read_csv('matches.csv')
data1 = pd.read_csv("deliveries.csv")

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowTitle(" WELCOME TO IPL STATS ")
        self.setGeometry(10,40,1950, 950)
        grid = QGridLayout()
        newfont = QFont("cambria",20,QFont.Bold)
        newfont1 = QFont("cambria",30,QFont.Bold)

        image=QImage(os.path.abspath("ipl14.jpg"))
        sImage =image.scaled(QSize(1900, 1000))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        self.show()

        label1 = QLabel("IPL:FESTIVAL OF INDIA")
        label2 = QLabel("WELCOME!!!")
        label3 = QLabel("YEAR WISE RESULTS:-")
        label4 = QLabel("OVER ALL SEASONS:-")
        label5=QLabel("FOR MORE INFORMATION,CLICK ")
        btn1 = QPushButton("CLICK HERE TO SEE YEAR WISE RESULTS")
        btn2 = QPushButton("CLICK HERE TO SEE OVER ALL SEASONS RESULTS")
        btn3 = QPushButton("HERE")

        label1.setFont(newfont1)
        label2.setFont(newfont1)
        label3.setFont(newfont)
        label4.setFont(newfont)
        label5.setFont(newfont)
        btn1.setFont(newfont)
        btn2.setFont(newfont)
        btn3.setFont(newfont)

        grid.addWidget(label1, 0, 1, 1, 1)
        grid.addWidget(label2, 1, 1, 2, 1)
        grid.addWidget(label3, 4, 1, 1, 1)
        grid.addWidget(label4, 8, 1, 1, 1)
        grid.addWidget(label5, 11, 2, 2, 1)
        grid.addWidget(btn1, 5, 1, 1, 1)
        grid.addWidget(btn2, 9, 1, 1, 1)
        grid.addWidget(btn3, 11, 3, 2, 1)

        btn1.clicked.connect(self.new1)
        btn2.clicked.connect(self.new2)
        btn3.clicked.connect(self.new3)

        self.setLayout(grid)
        self.show()

    def new1(self):
        try:
            self.obj = year_wise.Demo1()
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def new2(self):
        try:
            self.obj = main_analysis.Demo2()
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def new3(self):
        try:
            self.obj = particular_match_record.Demo3()
            self.obj.show()
        except BaseException as ex:
            print(ex)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Demo()
    sys.exit(app.exec_())


