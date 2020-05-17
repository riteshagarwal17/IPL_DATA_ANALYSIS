from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
#import ritesh1
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('matches.csv')
data1=pd.read_csv("deliveries.csv")
data1.dismissal_kind.fillna('notout',inplace=True)
data1.player_dismissed.fillna('notout',inplace=True)
#data1.fielder.fillna('notout',inplace=True)

class Demo2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GET STATS OF ALL SEASONS HERE ")
        self.setWindowIcon(QIcon("ipl17.jpg"))
        self.setGeometry(7,40,1930, 950)
        newfont = QFont("Times",18,QFont.Bold)
        self.count = 0

        mainMenu = self.menuBar()
        operationsMenu1 = mainMenu.addMenu("BATTING ANALYSIS")
        operationsMenu2 = mainMenu.addMenu("BOWLING ANALYSIS")
        operationsMenu3 = mainMenu.addMenu("FIELDING ANALYSIS")
        operationsMenu4 = mainMenu.addMenu("IMPACT OF TOSS")
        operationsMenu5 = mainMenu.addMenu("TOP SPORTSPERSON")
        operationsMenu6 = mainMenu.addMenu("UMPIRES")
        operationsMenu7 = mainMenu.addMenu("RESULTS")
        operationsMenu8 = mainMenu.addMenu("TEAMS WIN MARGIN")
        operationsMenu9 = mainMenu.addMenu("TEAM STATS")
        operationsMenu10 = mainMenu.addMenu("VENUE STATS")


        action1 = QAction("TEAM WIN BY 10 WICKETS",self)
        action1.setShortcut("Ctrl+N")
        action2 = QAction("TEAM WIN BY MORE THAN 100 RUNS",self)
        action2.setShortcut("Ctrl+O")
        action3 = QAction("TEAM WIN BY JUST 1 WICKET",self)
        action3.setShortcut("Ctrl+P")
        action4 = QAction("TEAM WIN BY JUST 1 RUN",self)
        action4.setShortcut("Ctrl+Q")
        action5 = QAction("IMPACT OF TOSS WINNING",self)
        action6 = QAction("IMPACT OF TOSS DECISION(FIELD)",self)
        action7 = QAction("IMPACT OF TOSS DECISION(BAT)",self)
        action8 = QAction("TOP  20 MAN OF THE MATCH",self)
        action9 = QAction("TOP 20 FIELDERS",self)
        action10 = QAction("TOP 20 WICKET TAKING BOWLERS",self)
        action11 = QAction("NO OF MATCHES IN EACH SEASON",self)
        action12 = QAction("NO OF WINS BY EACH TEAM",self)
        action13 = QAction("NO OF MATCHES AT EACH VENUE",self)
        action14 = QAction("VENUES NOT HAVING NORMAL RESULT",self)
        action15 = QAction("VENUES WHERE DL IS APPLIED MOST",self)
        action16 = QAction("UMPIRE1",self)
        action17 = QAction("UMPIRE2",self)
        action18 = QAction("TYPES OF  MATCH RESULTS",self)
        action19 = QAction("DL APPLIED",self)
        action20 = QAction("TYPES OF TOSS DECISION",self)
        action21 = QAction("TOTAL RUNS SCORED BY TEAMS",self)
        action22 = QAction("TOTAL RUNS SCORED IN DIFFERENT OVERS",self)
        action23 = QAction("TOTAL RUNS SCORED BY TOP 20 BATSMAN",self)
        action24 = QAction("TOTAL RUNS SCORED IN CHASING",self)
        action25 = QAction("TOTAL CENTURIES SCORED BY BATSMAN",self)
        action26 = QAction("DIFFERENT TYPES OF DISMISSALS",self)
        action27 = QAction("TOTAL WICKETS BETWEEN DIFF OVERS",self)
        action28 = QAction("TOTAL RUNS PER BALL(<1) CONCEDED BY BOWLERS  ",self)
        action29 = QAction("TOTAL WICKETS TAKEN BY DIFFERENT BOWLERS",self)
        action30 = QAction("MAX WICKETS TAKEN BY DIFFERENT BOWLERS IN DEATH OVERS",self)
        action31 = QAction("MIN RUNS PER BALL GIVEN BY DIFFERENT BOWLERS IN DEATH OVERS",self)
        action32 = QAction("BEST RUN OUTS BY DIFFERENT FIELDERS",self)
        action33 = QAction("BEST CATCHES BY DIFFERENT FIELDERS",self)
        action34 = QAction("BEST WICKET KEEPERS",self)
        action35 = QAction("TOP 20 HIGHEST RUN SCORERS",self)

        operationsMenu8.addAction(action1)
        operationsMenu8.addAction(action2)
        operationsMenu8.addAction(action3)
        operationsMenu8.addAction(action4)
        operationsMenu4.addAction(action5)
        operationsMenu4.addAction(action6)
        operationsMenu4.addAction(action7)
        operationsMenu5.addAction(action8)
        operationsMenu5.addAction(action9)
        operationsMenu5.addAction(action10)
        operationsMenu5.addAction(action35)
        operationsMenu9.addAction(action11)
        operationsMenu9.addAction(action12)
        operationsMenu10.addAction(action13)
        operationsMenu10.addAction(action14)
        operationsMenu10.addAction(action15)
        operationsMenu6.addAction(action16)
        operationsMenu6.addAction(action17)
        operationsMenu7.addAction(action18)
        operationsMenu7.addAction(action19)
        operationsMenu7.addAction(action20)
        operationsMenu1.addAction(action21)
        operationsMenu1.addAction(action22)
        operationsMenu1.addAction(action23)
        operationsMenu1.addAction(action24)
        operationsMenu1.addAction(action25)
        operationsMenu2.addAction(action26)
        operationsMenu2.addAction(action27)
        operationsMenu2.addAction(action28)
        operationsMenu2.addAction(action29)
        operationsMenu2.addAction(action30)
        operationsMenu2.addAction(action31)
        operationsMenu3.addAction(action32)
        operationsMenu3.addAction(action33)
        operationsMenu3.addAction(action34)

        action1.triggered.connect(self.MARGIN_WICKETS)
        action2.triggered.connect(self.MARGIN_RUNS)
        action3.triggered.connect(self.close_wickets)
        action4.triggered.connect(self.close_runs)
        action5.triggered.connect(self.tosswin)
        action6.triggered.connect(self.tossfield)
        action7.triggered.connect(self.tossbat)
        action8.triggered.connect(self.man)
        action9.triggered.connect(self.fielder)
        action10.triggered.connect(self.bowlers)
        action11.triggered.connect(self.number_matches)
        action12.triggered.connect(self.number_wins)
        action13.triggered.connect(self.venues)
        action14.triggered.connect(self.notnormal)
        action15.triggered.connect(self.dlvenues)
        action16.triggered.connect(self.umpire1)
        action17.triggered.connect(self.umpire2)
        action18.triggered.connect(self.resulttype)
        action19.triggered.connect(self.dlapplied)
        action20.triggered.connect(self.tossdecision)
        action21.triggered.connect(self.teamruns)
        action22.triggered.connect(self.overruns)
        action23.triggered.connect(self.batsmanruns)
        action24.triggered.connect(self.chasingruns)
        action25.triggered.connect(self.centbatsman)
        action26.triggered.connect(self.dismissals)
        action27.triggered.connect(self.overwickets)
        action28.triggered.connect(self.bowlerruns)
        action29.triggered.connect(self.bowlers)
        action30.triggered.connect(self.maxwickets)
        action31.triggered.connect(self.minruns)
        action32.triggered.connect(self.runouts)
        action33.triggered.connect(self.catches)
        action34.triggered.connect(self.keepers)
        action35.triggered.connect(self.batsmanruns)
        self.initUI()
        self.show()

    def initUI(self):
        newfont = QFont("Times",18,QFont.Bold)
        label1 = QLabel('CHOSE PLAYER NAME', self)
        label1.setGeometry(QRect(100, 200, 500, 81))
        label1.setFont(newfont)
        self.combo1 = QComboBox(self)
        values = data1.batsman.unique()
        values.sort()
        self.combo1.addItem("SELECT ANY PLAYER")
        self.combo1.addItems(values)
        self.combo1.setFont(newfont)
        self.combo1.setGeometry(QRect(100, 300, 500, 81))
        image = QImage("ipl19.jpg")
        sImage = image.scaled(QSize(1900, 1000))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        btn1 = QPushButton('RUNS SCORED BY CHOSEN BATSMAN AGAINST VARIOUS TEAMS', self)
        btn1.setGeometry(QRect(100, 500, 1050, 81))
        btn1.setFont(newfont)
        btn2 = QPushButton('RUNS SCORED BY CHOSEN BATSMAN AGAINST VARIOUS BOWLERS', self)
        btn2.setFont(newfont)
        btn2.setGeometry(QRect(100, 600, 1050, 81))
        btn1.clicked.connect(self.selectedbat1)
        btn2.clicked.connect(self.selectedbat2)
        self.show()
        '''centralWidget=QWidget(self)
        centralWidget2 = QWidget(self)
        self.combo1 = QComboBox(centralWidget)
        values = data1.batsman.unique()
        values.sort()
        self.combo1.addItem("SELECT ANY PLAYER")
        self.combo1.addItems(values)
        self.combo1.setFont(newfont)
        self.combo1.currentTextChanged.connect(self.MARGIN_WICKETS)
        self.combo1.setGeometry(QRect(100, 300, 500, 81))
        self.line = QLineEdit(centralWidget2)
        self.line.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.line.setFont(newfont)
        self.result = QLabel('Result                                                   ')
        self.result.setFont(newfont)
        self.setCentralWidget(centralWidget)
        self.show()'''

    def MARGIN_WICKETS(self):
        details = (data[data["win_by_wickets"] == 10]["winner"].value_counts())
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.35,top=0.94)
        plt.xlabel('Team Names',fontsize=20)
        plt.ylabel('No Of Matches',fontsize=20)
        plt.title("No Of Matches Won By 10 Wickets",fontsize=22)
        plt.show()

    def MARGIN_RUNS(self):
        details = (data[data["win_by_runs"] >= 100]["winner"].value_counts())
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.35,top=0.94)
        plt.xlabel('Team Names',fontsize=20)
        plt.ylabel('No Of Matches',fontsize=20)
        plt.title("No Of Matches Won By More Than 100 Runs",fontsize=22)
        plt.show()

    def close_runs(self):
        details = (data[data["win_by_runs"] == 1]["winner"].value_counts())
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.35,top=0.94)
        plt.xlabel('Team Names',fontsize=20)
        plt.ylabel('No Of Matches',fontsize=20)
        plt.title("No Of Matches Won By Only 1 Run Left",fontsize=22)
        plt.show()

    def close_wickets(self):
        details = (data[data["win_by_wickets"] == 1]["winner"].value_counts())
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.35,top=0.94)
        plt.xlabel('Team Names',fontsize=20)
        plt.ylabel('No Of Matches',fontsize=20)
        plt.title("No Of Matches Won By Only 1 Wicket Left",fontsize=22)
        plt.show()

    def tosswin(self):
        details = data[data["toss_winner"] == data["winner"]]["winner"].value_counts()
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel('Team Names',fontsize=20)
        plt.ylabel('No Of Matches Won',fontsize=20)
        plt.title("No Of Matches Won After Winning Toss",fontsize=22)
        plt.show()

    def tossfield(self):
        try:
            details=(data[(data["toss_decision"]=="field")&(data["toss_winner"]==data["winner"])]["winner"].value_counts())
            details.plot(kind="bar",figsize=(16,8),fontsize=12)
            plt.subplots_adjust(bottom=0.35)
            plt.xlabel('Team Names',fontsize=20)
            plt.ylabel('No Of Matches Won',fontsize=20)
            #plt.set_xticks(xlabel)
            plt.title("No Of Matches Won After Chosing Fielding",fontsize=22)
            plt.show()
        except BaseException as ex:
            print(ex)

    def tossbat(self):
        details=(data[(data["toss_decision"]=="bat")&(data["toss_winner"]==data["winner"])]["winner"].value_counts())
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel('Team Names',fontsize=20)
        plt.ylabel('No Of Matches Won',fontsize=20)
        plt.title("No Of Matches Won After Chosing Batting",fontsize=22)
        plt.show()

    def man(self):
        details=(data["player_of_match"].value_counts()[:20])
        #print(details)
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel('Player Names',fontsize=20)
        plt.ylabel('No Of Man Of Match Awards',fontsize=20)
        plt.title("No Of Man Of Match Awards Won By Top 20 Players",fontsize=22)
        plt.show()

    def fielder(self):
        try:
            details = data1[(data1["fielder"].isnull() == False)]["fielder"].value_counts()[:20]
            # print(details)
            details.plot(kind="bar",figsize=(14,8),fontsize=20)
            plt.subplots_adjust(bottom=0.25)
            plt.xlabel('Player Names',fontsize=20)
            plt.ylabel('No Of Catches',fontsize=20)
            plt.title("Top 20 Fielders",fontsize=22)
            plt.show()
        except BaseException as ex:
            print(ex)

    def bowlers(self):
        details = data1[(data1["player_dismissed"] != "notout") & (data1["dismissal_kind"] != "run out")& (data1["dismissal_kind"] != "retired hurt")]["bowler"].value_counts()[:20]
        # print(details)
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel('Player Names',fontsize=20)
        plt.ylabel('No Of Wickets',fontsize=20)
        plt.title("Top 20 Bowlers",fontsize=22)
        plt.show()

    def number_wins(self):
        details = data["winner"].value_counts()
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel('Team Names',fontsize=20)
        plt.ylabel('No Of Matches Won',fontsize=20)
        plt.title("No Of Matches Won By Teams",fontsize=22)
        plt.show()

    def number_matches(self):
        details = data["season"].value_counts()
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel('Season',fontsize=20)
        plt.ylabel('No Of Matches ',fontsize=20)
        plt.title("No Of Matches In Each Season",fontsize=22)
        plt.show()

    def venues(self):
        details = (data["venue"].value_counts())
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("Venue Name",fontsize=20)
        plt.ylabel("No Of Matches",fontsize=20)
        plt.title("No Of Matches At Each Venue",fontsize=22)
        plt.show()

    def dlvenues(self):
        details = data[data["dl_applied"] == 1]["venue"].value_counts()
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("Venue Name",fontsize=20)
        plt.ylabel("No Of Times DL Applied",fontsize=20)
        plt.title("No Of Times DL Applied At A Venue",fontsize=22)
        plt.show()

    def notnormal(self):
        details = (data[data["result"] != "normal"]["venue"].value_counts())
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("Venue Name",fontsize=20)
        plt.ylabel("No Of Result Is Not Normal",fontsize=20)
        plt.title("No Of Times Result Is Not Normal At A Venue",fontsize=22)
        plt.show()

    def umpire1(self):
        details = (data["umpire1"].value_counts())
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("Umpire Name",fontsize=20)
        plt.ylabel("No Of Times Umpired",fontsize=20)
        plt.title("No Of Times A Umpire Has Done Umpiring In IPL",fontsize=22)
        plt.show()

    def umpire2(self):
        details = (data["umpire2"].value_counts())
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("Umpire Name",fontsize=20)
        plt.ylabel("No Of Times Umpired",fontsize=20)
        plt.title("No Of Times A Umpire Has Done Umpiring In IPL",fontsize=22)
        plt.show()

    def resulttype(self):
        details = (data["result"].value_counts())
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("Result Type",fontsize=20)
        plt.ylabel("No Of Matches ",fontsize=20)
        plt.title("No Of Times This Result Happened",fontsize=22)
        plt.show()

    def dlapplied(self):
        details = (data["dl_applied"].value_counts())
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("DL Applied(1) or Not(0)",fontsize=20)
        plt.ylabel("No Of Matches ",fontsize=20)
        plt.title("No Of Times DL Is Applied",fontsize=22)
        plt.show()

    def tossdecision(self):
        details = (data["toss_decision"].value_counts())
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("Toss Decision",fontsize=20)
        plt.ylabel("No Of Matches ",fontsize=20)
        plt.title("Which Is More Prefered(Bat Or Field)",fontsize=22)
        plt.show()

    def teamruns(self):
        details = data1.groupby(data1.batting_team).total_runs.sum()
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("Team Name",fontsize=20)
        plt.ylabel(" Total No Of Runs ",fontsize=20)
        plt.title("Total No Of Runs By All Teams",fontsize=22)
        plt.show()

    def overruns(self):
        details = data1.groupby([data1.over]).total_runs.sum()
        details.plot(kind="pie",figsize=(14,8))
        plt.title("Total Runs In Different Overs",fontsize=22)
        plt.show()

    def batsmanruns(self):
        details = data1.groupby(data1.batsman).batsman_runs.sum().sort_values(ascending=False).head(20)
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("Batsman Name",fontsize=20)
        plt.ylabel(" Total No Of Runs ",fontsize=20)
        plt.title("Total No Of Runs By Top 20 Batsman",fontsize=22)
        plt.show()

    def chasingruns(self):
        df = data1.loc[data1.inning == 2, :]
        details = df.groupby(data1.batsman).batsman_runs.sum().sort_values(ascending=False).head(20)
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("Batsman Name",fontsize=20)
        plt.ylabel(" Total No Of Runs ",fontsize=20)
        plt.title("Total No Of Runs By Top 20 Chasing Batsman",fontsize=22)
        plt.show()

    def centbatsman(self):
        runs_series = data1.groupby([data1.match_id, data1.batsman]).total_runs.sum()
        runs_df = pd.DataFrame(runs_series)
        runs_df = runs_df.reset_index()
        condition = runs_df.total_runs >= 100
        player_100df = runs_df.loc[condition, :]
        details = player_100df.groupby(player_100df.batsman).total_runs.count().sort_values(ascending=False).head(20)
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("Batsman Name",fontsize=20)
        plt.ylabel(" Total No Of Centuries ",fontsize=20)
        plt.title("Total No Of Centuries By Top 20 Batsman",fontsize=22)
        plt.show()

    def dismissals(self):
        details = data1[data1["dismissal_kind"] != "notout"]["dismissal_kind"].value_counts()
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("Type Of Dismissal",fontsize=20)
        plt.ylabel("No Of Matches ",fontsize=20)
        plt.title(" Count Of Dismissal Types",fontsize=22)
        plt.show()

    def overwickets(self):
        condition = (data1.dismissal_kind != 'run out') & (data1.dismissal_kind != 'retired hurt') & (data1.dismissal_kind != 'notout')
        df = data1.loc[condition, :]
        details = df.groupby([df.over]).over.count()
        details.plot(kind="pie",figsize=(14,8),fontsize=12)
        plt.xlabel("Over Number",fontsize=20)
        plt.ylabel("No Of Wickets",fontsize=20)
        plt.title(" Count Of Wickets In Different Overs",fontsize=22)
        plt.show()

    def bowlerruns(self):
        details = data1.groupby(data1.bowler).total_runs.mean().sort_values().head(11)
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel("Bowler Name",fontsize=20)
        plt.ylabel("No Of Runs Per Ball",fontsize=20)
        plt.title("Top 10 Economic Bowlers",fontsize=22)
        plt.show()

    def bowlerwickets(self):

        details = data1[(data1["player_dismissed"] != "notout") & (data1["dismissal_kind"] != "run out") & (data1["dismissal_kind"] != "retired hurt")]["bowler"].value_counts()[:20]
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel('Player Names',fontsize=20)
        plt.ylabel('No Of Wickets',fontsize=20)
        plt.title('Top 20 Bowlers With Most Number Of Wickets',fontsize=22)
        plt.show()

    def maxwickets(self):
        details = data1[(data1["over"] > 15) & (data1["player_dismissed"] != "notout") & (data1["dismissal_kind"] != "run out") & (data1["dismissal_kind"] != "retired hurt")]["bowler"].value_counts()[:20]
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel('Players Name',fontsize=20)
        plt.ylabel('No Of Wickets',fontsize=20)
        plt.title("Top 20 Bowlers With Most Number Of Wickets In Death Overs::Death Overs Specialist",fontsize=22)
        plt.show()

    def minruns(self):
        del_series = data1.groupby(data1.bowler).total_runs.count()
        del_df = pd.DataFrame(del_series).reset_index()
        del_df.columns = ['bowler', 'delivery']
        bowlers = del_df.loc[del_df.delivery >= 90, :].bowler
        condition = (data1.over > 15) & (data1.bowler.isin(bowlers))
        df = data1.loc[condition, :]
        details = df.groupby(df.bowler).total_runs.mean().sort_values().head(10)
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel('Bowlers Name',fontsize=20)
        plt.ylabel('Runs Per Ball',fontsize=20)
        plt.title('Best Economy In Death Overs',fontsize=20)
        plt.title('Death Overs Specialist',fontsize=22)
        plt.show()

    def runouts(self):
        condition = data1.dismissal_kind == 'run out'
        df = data1.loc[condition, :]
        details = df.groupby(df.fielder).batsman.count().sort_values(ascending=False).head(20)
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel('Fielders Name',fontsize=20)
        plt.ylabel('No Of Run Outs',fontsize=20)
        plt.title("Top 20 Fielders With Most Number Of Run Outs",fontsize=22)
        plt.show()

    def catches(self):
        condition = (data1.dismissal_kind == 'caught and bowled') | (data1.dismissal_kind == 'caught')
        df = data1.loc[condition, :]
        details = df.groupby(df.fielder).batsman.count().sort_values(ascending=False).head(20)
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel('Fielders Name',fontsize=20)
        plt.ylabel('No Of Catches',fontsize=20)
        plt.title("Top 20 Fielders With Most Number Of Catches",fontsize=22)
        plt.show()

    def keepers(self):
        condition = data1.dismissal_kind == 'stumped'
        df = data1.loc[condition, :]
        details = df.groupby(df.fielder).batsman.count().sort_values(ascending=False).head(20)
        details.plot(kind="bar",figsize=(14,8),fontsize=12)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel('Fielders Name',fontsize=20)
        plt.ylabel('No Of Catches And Stumpout By Keepers',fontsize=20)
        plt.title("Top 20 Keepers",fontsize=22)
        plt.show()

    def selectedbat1(self):
        try:
            value = self.combo1.currentText()
            if value=='SELECT ANY PLAYER':
                QMessageBox.about(self, "Error", "No Player Selected!!!")
                QMessageBox.setBaseSize(self,QSize(800, 120))
            else:
                pass
            values = data1.batsman.unique()
            values.sort()
            for i in range(0,461):
                if value == values[i]:
                    df = data1.loc[data1.batsman == values[i], :]
                    details=df.groupby(df.bowling_team).batsman_runs.sum().sort_values(ascending=False)
                    #print(details)
                    details.plot(kind="bar",figsize=(14,8),fontsize=12)
                    plt.subplots_adjust(bottom=0.25)
                    plt.xlabel('Team Name',fontsize=20)
                    plt.ylabel('No Of Runs',fontsize=20)
                    plt.title(values[i] +"'s Runs Against Various Teams",fontsize=22)
                    plt.show()

                else:
                    pass
            #details.to_csv('againstteams.csv')
        except BaseException as ex:
            print(ex)

    def selectedbat2(self):
        try:
            value = self.combo1.currentText()
            if value == 'SELECT ANY PLAYER':
                QMessageBox.about(self, "Error", "No Player Selected!!!")
                QMessageBox.setBaseSize(self, QSize(800, 120))
            else:
                pass

            values = data1.batsman.unique()
            values.sort()
            for i in range(0,461):
                if value == values[i]:
                    df = data1.loc[data1.batsman == values[i], :]
                    details=df.groupby(df.bowler).batsman_runs.sum().sort_values(ascending=False).head(20)
                    #print(details)
                    details.plot(kind="bar",figsize=(14,8),fontsize=12)
                    plt.subplots_adjust(bottom=0.25)
                    plt.xlabel('Bowler Name',fontsize=20)
                    plt.ylabel('No Of Runs',fontsize=20)
                    plt.title(values[i] +"'s Top Scores Against Top 20 Bowlers",fontsize=22)
                    plt.show()

                else:
                    pass
            #details.to_csv('againstteams.csv')
        except BaseException as ex:
            print(ex)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = Demo2()
    sys.exit(app.exec_())