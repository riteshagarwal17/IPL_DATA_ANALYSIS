from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
data=pd.read_csv('matches.csv')
data1=pd.read_csv("deliveries.csv")
data1.dismissal_kind.fillna('notout',inplace=True)
data1.player_dismissed.fillna('notout',inplace=True)

class Demo1(QWidget):
    def __init__(self):
        super(Demo1, self).__init__()
        self.setWindowTitle(" GET STAT OF ANY YEAR ")
        self.setWindowIcon(QIcon("ipl2.png"))
        self.setGeometry(10,40,1930, 950)
        grid = QGridLayout()
        newfont = QFont("cambria",18,QFont.Bold)
        label3 = QLabel("SEE YEAR WISE STATS")
        btn1 = QPushButton("TOP  20 PLAYERS OF SELECTED SEASON")
        btn2 = QPushButton("TOP  20 RUN SCORER OF SELECTED SEASON")
        btn3 = QPushButton("TOP  20 WICKET TAKER OF SELECTED SEASON")
        btn4 = QPushButton("TOP  TEAMS OF SELECTED SEASON")
        btn5 = QPushButton("TOP  20 SIX HITTER OF SELECTED SEASON")
        btn6 = QPushButton("TOP  20 FOUR HITTER OF SELECTED SEASON")
        btn7 = QPushButton("TOP  20 PLAYERS WITH HIGHEST STRIKE RATE OF SELECTED SEASON")


        self.combo1 = QComboBox()
        values = ['Select Any YEAR', "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"]
        self.combo1.addItems(values)

        label3.setFont(newfont)
        btn1.setFont(newfont)
        btn2.setFont(newfont)
        btn3.setFont(newfont)
        btn4.setFont(newfont)
        btn5.setFont(newfont)
        btn6.setFont(newfont)
        btn7.setFont(newfont)
        self.combo1.setFont(newfont)


        grid.addWidget(btn1, 6, 1, 1, 1)
        grid.addWidget(btn2, 7,1, 1, 1)
        grid.addWidget(btn3, 8, 1, 1, 1)
        grid.addWidget(btn4, 9, 1, 1, 1)
        grid.addWidget(btn5, 11, 1, 1, 1)
        grid.addWidget(btn6, 12, 1, 1,1)
        grid.addWidget(btn7, 13, 1, 1,1)
        grid.addWidget(self.combo1, 3, 1, 4, 1)
        grid.addWidget(label3, 2, 1, 1, 1)

        btn1.clicked.connect(self.man)
        btn2.clicked.connect(self.scorer)
        btn3.clicked.connect(self.getter)
        btn4.clicked.connect(self.teamwin)
        btn5.clicked.connect(self.maximum6)
        btn6.clicked.connect(self.maximum4)
        btn7.clicked.connect(self.maximumSR)

        image = QImage(os.path.abspath("ipl15.jpg"))
        sImage = image.scaled(QSize(1900, 1000))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        #btn1.setIcon(QIcon(QPixmap("ipl7.jpg")))

        self.combo1.currentTextChanged.connect(self.perform)
        self.setLayout(grid)
        self.show()

    def man(self,values):
        try:
            value = self.combo1.currentText()
            if value=='Select Any YEAR':
                QMessageBox.about(self, "Error", "No Year Selected")
                QMessageBox.setBaseSize(self,QSize(800, 120))
            else:
                pass
            values = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                      "2017"]
            for i in range(0, 10):
                if value == values[i]:
                    details = (data['season'] == int(values[i]))
                    details1 = data.loc[details]
                    break
                    # print(details1)
                else:
                    pass
            details1.to_csv('seasonwise.csv')
            data2 = pd.read_csv("seasonwise.csv")
            details2 = (data2["player_of_match"].value_counts()[:20])
            #print(details)
            details2.plot(kind="bar",legend=False,figsize=(14,8),fontsize=12)
            plt.subplots_adjust(bottom=0.25)
            #plt.figure(figsize=(5,5))
            plt.xlabel('Player Names',fontsize=20)
            plt.ylabel('No Of Man Of Match Awards',fontsize=20)
            plt.title("No Of Man Of Match Awards By Players In"+ str(values[i]),fontsize=22)
            plt.show()
            os.remove("seasonwise.csv")
        except BaseException as ex:
            print(ex)

    def perform(self):
        try:
            value = self.combo1.currentText()
            values = [ "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                      "2017"]
            for i in range(0,10):
                if value == values[i]:
                    details = (data['season'] == int(values[i]) )
                    details1 = data.loc[details]
                    #print(details1)
                else:
                    pass
            details1.to_csv('seasonwise.csv')
        except BaseException as ex:
            print(ex)

    def scorer(self):
        try:
            value = self.combo1.currentText()
            if value=='Select Any YEAR':
                QMessageBox.about(self, "Error", "No Year Selected")
                QMessageBox.setBaseSize(self,QSize(800, 120))
            else:
                pass
            values = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                      "2017"]
            for i in range(0, 10):
                if value == values[i]:
                    combined = data1.set_index('match_id').join(data.set_index('id'), how='inner')
                    runs_series = combined.groupby([combined.season, combined.batsman]).total_runs.sum()
                    runs_df = pd.DataFrame(runs_series)
                    runs_df.reset_index(inplace=True)
                    condition=runs_df.season == (int(values[i]))
                    details = runs_df.loc[condition, :].sort_values('total_runs', ascending=False).head(20)
                    #print(details)
                    details.plot(kind="bar", x='batsman', y='total_runs',legend=False,figsize=(14,8),fontsize=12)
                    plt.subplots_adjust(bottom=0.25)
                    plt.xlabel('Player Names',fontsize=20)
                    plt.ylabel('No Of Runs Scored',fontsize=20)
                    plt.title("Top 20 Run Scorers In " + str(values[i]),fontsize=22)
                    plt.show()
                else:
                    pass
        except BaseException as ex:
            print(ex)

    def getter(self):
        try:
            value = self.combo1.currentText()
            if value=='Select Any YEAR':
                QMessageBox.about(self, "Error", "No Year Selected")
                QMessageBox.setBaseSize(self,QSize(800, 120))
            else:
                pass
            values = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                      "2017"]
            for i in range(0, 10):
                if value == values[i]:
                    combined = data1.set_index('match_id').join(data.set_index('id'), how='inner')
                    condition = (combined.dismissal_kind != 'run out') & (combined.dismissal_kind != 'retired hurt') & (
                                combined.dismissal_kind != 'notout')
                    df = combined.loc[condition, :]
                    wicket_series = df.groupby([df.season, df.bowler]).non_striker.count()
                    wicket_df = pd.DataFrame(wicket_series)
                    wicket_df.reset_index(inplace=True)
                    condition = wicket_df.season == (int(values[i]))
                    details=wicket_df.loc[condition, :].sort_values('non_striker', ascending=False).head(20)
                    #print(details)
                    details.plot(kind="bar", x='bowler', y='non_striker',legend=False,figsize=(14,8),fontsize=12)
                    plt.subplots_adjust(bottom=0.25)
                    plt.xlabel('Player Names',fontsize=20)
                    plt.ylabel('No Of Wickets Taken',fontsize=20)
                    plt.title("Top 20 Wicket Takers In " + str(values[i]),fontsize=22)
                    plt.show()
                else:
                    pass
        except BaseException as ex:
            print(ex)

    def teamwin(self):
        try:
            value = self.combo1.currentText()
            if value=='Select Any YEAR':
                QMessageBox.about(self, "Error", "No Year Selected")
                QMessageBox.setBaseSize(self,QSize(800, 120))
            else:
                pass
            values = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                      "2017"]
            for i in range(0, 10):
                if value == values[i]:
                    details = (data['season'] == int(values[i]))
                    details1 = data.loc[details]
                    # print(details1)
                    details1.to_csv('seasonwise.csv')
                    data2 = pd.read_csv("seasonwise.csv")
                    details3 = data2["winner"].value_counts()
                    # print(details)
                    details3.plot(kind="bar",figsize=(14,8),fontsize=12)
                    plt.subplots_adjust(bottom=0.25)
                    plt.xlabel('Team Names',fontsize=20)
                    plt.ylabel('No Of Matches Won',fontsize=20)
                    plt.title("No Of Matches Won By Different Teams In"+ str(values[i]),fontsize=22)
                    plt.show()
                    os.remove("seasonwise.csv")
                else:
                    pass

        except BaseException as ex:
            print(ex)

    def maximum6(self):
        try:
            value = self.combo1.currentText()
            if value=='Select Any YEAR':
                QMessageBox.about(self, "Error", "No Year Selected")
                QMessageBox.setBaseSize(self,QSize(800, 120))
            else:
                pass
            values = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                      "2017"]
            for i in range(0, 10):
                if value == values[i]:
                    batsman_grp = data1.groupby(["match_id", "inning", "batting_team", "batsman"])
                    batsmen = batsman_grp["batsman_runs"].sum().reset_index()
                    balls_faced = data1[data1["wide_runs"] == 0]
                    balls_faced = balls_faced.groupby(["match_id", "inning", "batsman"])["batsman_runs"].count().reset_index()
                    balls_faced.columns = ["match_id", "inning", "batsman", "balls_faced"]
                    batsmen = batsmen.merge(balls_faced, left_on=["match_id", "inning", "batsman"],right_on=["match_id", "inning", "batsman"], how="left")
                    fours = data1[data1["batsman_runs"] == 4]
                    sixes = data1[data1["batsman_runs"] == 6]
                    fours_per_batsman = fours.groupby(["match_id", "inning", "batsman"])["batsman_runs"].count().reset_index()
                    sixes_per_batsman = sixes.groupby(["match_id", "inning", "batsman"])["batsman_runs"].count().reset_index()
                    fours_per_batsman.columns = ["match_id", "inning", "batsman", "4s"]
                    sixes_per_batsman.columns = ["match_id", "inning", "batsman", "6s"]
                    batsmen = batsmen.merge(fours_per_batsman, left_on=["match_id", "inning", "batsman"],right_on=["match_id", "inning", "batsman"], how="left")
                    batsmen = batsmen.merge(sixes_per_batsman, left_on=["match_id", "inning", "batsman"],right_on=["match_id", "inning", "batsman"], how="left")
                    batsmen['SR'] = np.round(batsmen['batsman_runs'] / batsmen['balls_faced'] * 100, 2)
                    for col in ["batsman_runs", "4s", "6s", "balls_faced", "SR"]:
                        batsmen[col] = batsmen[col].fillna(0)
                    dismissals = data1[pd.notnull(data1["player_dismissed"])]
                    dismissals = dismissals[["match_id", "inning", "player_dismissed", "dismissal_kind", "fielder"]]
                    dismissals.rename(columns={"player_dismissed": "batsman"}, inplace=True)
                    batsmen = batsmen.merge(dismissals, left_on=["match_id", "inning", "batsman"],right_on=["match_id", "inning", "batsman"], how="left")
                    batsmen = data[['id', 'season' ]].merge(batsmen, left_on='id', right_on='match_id',how='left').drop('id', axis=1)
                    #details=batsmen["batsman"]["4s"].value_counts()
                    details=batsmen[batsmen["season"]==int(values[i])].sort_values('6s',ascending=False).head(20)
                    #print(details)
                    details.plot(kind="bar", x='batsman', y='6s',legend=False,figsize=(14,8),fontsize=12)
                    plt.subplots_adjust(bottom=0.25)
                    plt.xlabel('Player Names',fontsize=20)
                    plt.ylabel('No Of 6s',fontsize=20)
                    plt.title("Top 20 6s Hitters In " + str(values[i]),fontsize=22)
                    plt.show()
                else:
                    pass
        except BaseException as ex:
            print(ex)

    def maximum4(self):
        try:
            value = self.combo1.currentText()
            if value=='Select Any YEAR':
                QMessageBox.about(self, "Error", "No Year Selected")
                QMessageBox.setBaseSize(self,QSize(800, 120))
            else:
                pass
            values = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                      "2017"]
            for i in range(0, 10):
                if value == values[i]:
                    batsman_grp = data1.groupby(["match_id", "inning", "batting_team", "batsman"])
                    batsmen = batsman_grp["batsman_runs"].sum().reset_index()
                    balls_faced = data1[data1["wide_runs"] == 0]
                    balls_faced = balls_faced.groupby(["match_id", "inning", "batsman"])["batsman_runs"].count().reset_index()
                    balls_faced.columns = ["match_id", "inning", "batsman", "balls_faced"]
                    batsmen = batsmen.merge(balls_faced, left_on=["match_id", "inning", "batsman"],right_on=["match_id", "inning", "batsman"], how="left")
                    fours = data1[data1["batsman_runs"] == 4]
                    sixes = data1[data1["batsman_runs"] == 6]
                    fours_per_batsman = fours.groupby(["match_id", "inning", "batsman"])["batsman_runs"].count().reset_index()
                    sixes_per_batsman = sixes.groupby(["match_id", "inning", "batsman"])["batsman_runs"].count().reset_index()
                    fours_per_batsman.columns = ["match_id", "inning", "batsman", "4s"]
                    sixes_per_batsman.columns = ["match_id", "inning", "batsman", "6s"]
                    batsmen = batsmen.merge(fours_per_batsman, left_on=["match_id", "inning", "batsman"],right_on=["match_id", "inning", "batsman"], how="left")
                    batsmen = batsmen.merge(sixes_per_batsman, left_on=["match_id", "inning", "batsman"],right_on=["match_id", "inning", "batsman"], how="left")
                    batsmen['SR'] = np.round(batsmen['batsman_runs'] / batsmen['balls_faced'] * 100, 2)
                    for col in ["batsman_runs", "4s", "6s", "balls_faced", "SR"]:
                        batsmen[col] = batsmen[col].fillna(0)
                    dismissals = data1[pd.notnull(data1["player_dismissed"])]
                    dismissals = dismissals[["match_id", "inning", "player_dismissed", "dismissal_kind", "fielder"]]
                    dismissals.rename(columns={"player_dismissed": "batsman"}, inplace=True)
                    batsmen = batsmen.merge(dismissals, left_on=["match_id", "inning", "batsman"],right_on=["match_id", "inning", "batsman"], how="left")
                    batsmen = data[['id', 'season' ]].merge(batsmen, left_on='id', right_on='match_id',how='left').drop('id', axis=1)
                    details=batsmen[batsmen["season"]==int(values[i])].sort_values('4s',ascending=False).head(20)
                    #print(details)
                    details.plot(kind="bar", x='batsman', y='4s',legend=False,figsize=(14,8),fontsize=12)
                    plt.subplots_adjust(bottom=0.25)
                    plt.xlabel('Player Names',fontsize=20)
                    plt.ylabel('No Of 4s',fontsize=20)
                    plt.title("Top 20 4s Hitters In " + str(values[i]),fontsize=22)
                    plt.show()
                else:
                    pass
        except BaseException as ex:
            print(ex)

    def maximumSR(self):
        try:
            value = self.combo1.currentText()
            if value=='Select Any YEAR':
                QMessageBox.about(self, "Error", "No Year Selected")
                QMessageBox.setBaseSize(self,QSize(800, 120))
            else:
                pass
            values = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                      "2017"]
            for i in range(0, 10):
                if value == values[i]:
                    batsman_grp = data1.groupby(["match_id", "inning", "batting_team", "batsman"])
                    batsmen = batsman_grp["batsman_runs"].sum().reset_index()
                    balls_faced = data1[data1["wide_runs"] == 0]
                    balls_faced = balls_faced.groupby(["match_id", "inning", "batsman"])["batsman_runs"].count().reset_index()
                    balls_faced.columns = ["match_id", "inning", "batsman", "balls_faced"]
                    batsmen = batsmen.merge(balls_faced, left_on=["match_id", "inning", "batsman"],right_on=["match_id", "inning", "batsman"], how="left")
                    fours = data1[data1["batsman_runs"] == 4]
                    sixes = data1[data1["batsman_runs"] == 6]
                    fours_per_batsman = fours.groupby(["match_id", "inning", "batsman"])["batsman_runs"].count().reset_index()
                    sixes_per_batsman = sixes.groupby(["match_id", "inning", "batsman"])["batsman_runs"].count().reset_index()
                    fours_per_batsman.columns = ["match_id", "inning", "batsman", "4s"]
                    sixes_per_batsman.columns = ["match_id", "inning", "batsman", "6s"]
                    batsmen = batsmen.merge(fours_per_batsman, left_on=["match_id", "inning", "batsman"],right_on=["match_id", "inning", "batsman"], how="left")
                    batsmen = batsmen.merge(sixes_per_batsman, left_on=["match_id", "inning", "batsman"],right_on=["match_id", "inning", "batsman"], how="left")
                    batsmen['SR'] = np.round(batsmen['batsman_runs'] / batsmen['balls_faced'] * 100, 2)
                    for col in ["batsman_runs", "4s", "6s", "balls_faced", "SR"]:
                        batsmen[col] = batsmen[col].fillna(0)
                    dismissals = data1[pd.notnull(data1["player_dismissed"])]
                    dismissals = dismissals[["match_id", "inning", "player_dismissed", "dismissal_kind", "fielder"]]
                    dismissals.rename(columns={"player_dismissed": "batsman"}, inplace=True)
                    batsmen = batsmen.merge(dismissals, left_on=["match_id", "inning", "batsman"],right_on=["match_id", "inning", "batsman"], how="left")
                    batsmen = data[['id', 'season' ]].merge(batsmen, left_on='id', right_on='match_id',how='left').drop('id', axis=1)
                    details=batsmen[batsmen["season"]==int(values[i])].sort_values('SR',ascending=False).head(20)
                    #print(details)
                    details.plot(kind="bar", x='batsman', y='SR',legend=False,figsize=(14,8),fontsize=12)
                    plt.subplots_adjust(bottom=0.25)
                    plt.xlabel('Player Names',fontsize=20)
                    plt.ylabel('Strike Rate',fontsize=20)
                    plt.title("Top 20 High Strike Rates In " + str(values[i]),fontsize=22)
                    plt.subplots_adjust()
                    plt.show()
                else:
                    pass
        except BaseException as ex:
            print(ex)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Demo1()
    sys.exit(app.exec_())

