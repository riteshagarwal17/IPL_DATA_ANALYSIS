from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys
import particular_match_record
data=pd.read_csv('matches.csv')
data1=pd.read_csv("deliveries.csv")


class CountriesScreen(QDialog):
    def __init__(self,value1,value2,value3):
        try:
            super(CountriesScreen, self).__init__()
            self.setWindowTitle(" HERE'S REQUIRED DETAILS!!! ")
            self.setGeometry(50, 100, 1800, 700)
            image = QImage("ipl17.jpg")
            sImage = image.scaled(QSize(1050, 750))
            palette = QPalette()
            palette.setBrush(10, QBrush(sImage))
            self.setPalette(palette)

            #data = pd.read_csv("country_population.csv")
            details = (data.season == int(value1)) & (data.city == (value3)) & (data.date == (value2) )
            details1 = data.loc[details,:]
            listss=details1.apply(lambda x:x.tolist(),axis=1)

            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(18)

            self.tableWidget.move(0, 0)
            #y=str(list[0])
            column_headers = ("id","season","city","date","team1","team2","toss_winner","toss_decision"	,"result","dl_applied","winner","win_by_runs","win_by_wickets","player_of_match","venue","umpire1","umpire2","umpire3")
            self.tableWidget.setHorizontalHeaderLabels(column_headers)
            for record in listss:
                self.tableWidget.setItem(0, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget.setItem(0, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget.setItem(0, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget.setItem(0, 3, QTableWidgetItem(str(record[3])))
                self.tableWidget.setItem(0, 4, QTableWidgetItem(str(record[4])))
                self.tableWidget.setItem(0, 5, QTableWidgetItem(str(record[5])))
                self.tableWidget.setItem(0, 6, QTableWidgetItem(str(record[6])))
                self.tableWidget.setItem(0, 7, QTableWidgetItem(str(record[7])))
                self.tableWidget.setItem(0, 8, QTableWidgetItem(str(record[8])))
                self.tableWidget.setItem(0, 9, QTableWidgetItem(str(record[9])))
                self.tableWidget.setItem(0, 10, QTableWidgetItem(str(record[10])))
                self.tableWidget.setItem(0, 11, QTableWidgetItem(str(record[11])))
                self.tableWidget.setItem(0, 12, QTableWidgetItem(str(record[12])))
                self.tableWidget.setItem(0, 13, QTableWidgetItem(str(record[13])))
                self.tableWidget.setItem(0, 14, QTableWidgetItem(str(record[14])))
                self.tableWidget.setItem(0, 15, QTableWidgetItem(str(record[15])))
                self.tableWidget.setItem(0, 16, QTableWidgetItem(str(record[16])))
                self.tableWidget.setItem(0, 17, QTableWidgetItem(str(record[17])))

            self.tableWidget.move(0, 0)

            self.layout = QVBoxLayout()
            self.layout.addWidget(self.tableWidget)
            self.setLayout(self.layout)
            self.show()
        except BaseException as ex:
            print(ex)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = CountriesScreen(value1,value2,value3)
    sys.exit(app.exec_())