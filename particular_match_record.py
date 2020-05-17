from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
import table_view
import pandas as pd
data = pd.read_csv('matches.csv')
data1 = pd.read_csv("deliveries.csv")
data1.dismissal_kind.fillna('notout',inplace=True)
data1.player_dismissed.fillna('notout',inplace=True)
data.city.fillna('notavailable',inplace=True)

class Demo3(QWidget):
    def __init__(self):
        super(Demo3, self).__init__()
        self.setWindowTitle("SEARCH ANY MATCH DETAILS ")
        self.setWindowIcon(QIcon("ipl20.jpg"))
        self.setGeometry(10,40,1930, 950)
        grid = QGridLayout()
        newfont = QFont("Times",18,QFont.Bold)


        self.combo1 = QComboBox()
        self.combo2 = QComboBox()
        self.combo3 = QComboBox()
        btn1 = QPushButton("CLICK HERE TO SEE DETAILS")

        image = QImage("ipl20.jpg")
        sImage = image.scaled(QSize(1900, 1000))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        values = ['Select Any YEAR', "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"]
        self.combo1.addItems(values)
        self.combo2.addItem("Select Any Date")
        self.combo3.addItem("Select Host City")
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)
        self.combo3.setFont(newfont)
        btn1.setFont(newfont)

        grid.addWidget(self.combo1, 3, 1, 3, 2)
        grid.addWidget(self.combo2, 5, 1, 3, 2)
        grid.addWidget(self.combo3, 7, 1, 3, 2)
        grid.addWidget(btn1, 10, 1, 1, 2)

        self.combo1.currentTextChanged.connect(self.perform)
        self.combo2.currentTextChanged.connect(self.city)
        btn1.clicked.connect(self.seedetails)


        self.setLayout(grid)
        self.show()

    def perform(self):
        try:
            value = self.combo1.currentText()
            values = [ "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                      "2017"]
            for i in range(0,10):
                if value == values[i]:
                    details = (data['season'] == int(values[i]) )
                    details1 = data.loc[details]
                else:
                    pass
            details1.to_csv('seasonwise.csv')
            data2 = pd.read_csv("seasonwise.csv")
            #print(details)
            self.combo2.clear()
            self.combo2.addItem("Select Any Date")
            details3 = data2["date"].unique()
            for x in details3:
                self.combo2.addItem(x)
                #print(x)
            os.remove("seasonwise.csv")

        except BaseException as ex:
            print(ex)

    def city(self):
            try:
                value1 = self.combo1.currentText()
                values = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016","2017"]
                for i in range(0, 10):
                    if value1 == values[i]:
                        details = (data['season'] == int(values[i]))
                        details1 = data.loc[details]
                    else:
                        pass
                details1.to_csv('seasonwise.csv')
                data2 = pd.read_csv("seasonwise.csv")
                value2 = self.combo2.currentText()
                details3 = data2["date"].unique()
                #print(len(details3))
                for i in range(0, len(details3)):
                    if value2 == details3[i]:
                        details4 = (data2['date'] == details3[i])
                        details5 = data2.loc[details4]
                    else:
                        pass
                details5.to_csv("citywise.csv")
                data3 = pd.read_csv("citywise.csv")
                # print(details)
                self.combo3.clear()
                self.combo3.addItem("Select Any City")
                details5 = data3["city"].unique()
                for x in details5:
                    self.combo3.addItem(x)
                    #print(x)
                os.remove("citywise.csv")
                os.remove("seasonwise.csv")
                return value1
                return value2

            except BaseException as ex:
                print(ex)

    def seedetails(self):
        try:
            value1 = self.combo1.currentText()
            value2 = self.combo2.currentText()
            value3 = self.combo3.currentText()
            if value1 == 'Select Any Year' or value2=='Select Any Date' or value3=='Select Any City':
                QMessageBox.about(self, "Error", "Please Chose Required Fields!!!")
                QMessageBox.setBaseSize(self, QSize(800, 120))
                exit()
            else:
                pass

            self.obj = table_view.CountriesScreen(value1, value2, value3)
            self.obj.show()
        except BaseException as ex:
            print(ex)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = Demo3()
    sys.exit(app.exec_())