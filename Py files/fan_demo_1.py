from PyQt5 import QtCore, QtGui, QtWidgets
from new_team import Ui_Dialog as new_t
from points_calculator import player_points
from open_1 import Ui_Form as open_1
from eval import Ui_Form as eval_1

import sqlite3
conn_obj=sqlite3.connect("Players.db")
cursor_obj=conn_obj.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.avail_points = 1000
        self.used_points = 0
        self.totalcount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        # INITIALIZING LISTS
        self.a = []  # bowler names list
        self.b = []  # batsman nameslist
        self.c = []  # allrounder names list
        self.d = []  # wicketer names list
        self.list1 = []  # selectedplayer's list
        self.stats = {}
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 588)
        MainWindow.setMinimumSize(QtCore.QSize(618, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 35, 651, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 97, 231, 23))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 116, 20))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(9, 66, 231, 25))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_5.setAcceptDrops(True)
        self.lineEdit_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_5.setFrame(True)
        self.lineEdit_5.setDragEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_3.addWidget(self.lineEdit_5, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(370, 70, 203, 25))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7, 0, QtCore.Qt.AlignRight)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_4.addWidget(self.lineEdit_6, 0, QtCore.Qt.AlignRight)
        self.lineEdit_6.raise_()
        self.label_7.raise_()
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(370, 100, 204, 25))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8, 0, QtCore.Qt.AlignRight)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_5.addWidget(self.lineEdit_7, 0, QtCore.Qt.AlignRight)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(9, 128, 600, 388))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_6)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_6.addWidget(self.listWidget_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_6)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_6.addWidget(self.listWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 20))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.disable_rbs()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionNEW_Team.triggered.connect(self.newt_pop)
        self.radioButton.clicked.connect(self.butnspress)
        self.radioButton_2.clicked.connect(self.butnspress)
        self.radioButton_3.clicked.connect(self.butnspress)
        self.radioButton_4.clicked.connect(self.butnspress)
        self.listWidget_2.itemDoubleClicked.connect(self.removelist1)
        self.listWidget.itemDoubleClicked.connect(self.removelist2)
        self.actionSAVE_Team.triggered.connect(self.file_save)
        self.actionOPEN_Team.triggered.connect(self.open_team)
        self.actionEVALUATE_Team.triggered.connect(self.evaluate)
        self.actionEVALUATE_Team.triggered.connect(self.evaluate)





    def disable_rbs(self):
        self.radioButton.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.radioButton_3.setEnabled(False)
        self.radioButton_4.setEnabled(False)

    def enable_rbs(self):
        self.radioButton.setEnabled(True)
        self.radioButton_2.setEnabled(True)
        self.radioButton_3.setEnabled(True)
        self.radioButton_4.setEnabled(True)

# new team window
    def newt_pop(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui_t= new_t()
        self.ui_t.setupUi(self.Dialog)
        self.ui_t.savebutton.clicked.connect(self.save_t)
        self.Dialog.show()

    def save_t(self):
        self.txt_1=self.ui_t.lineEdit.text()
        cursor_obj.execute("SELECT DISTINCT Name FROM teams")
        l = cursor_obj.fetchall()
        for i in l:
            if i[0] == self.txt_1:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team with same name already exists!!\nPlease choose another name")
                msg.setWindowTitle("Invalid Team Name")
                msg.exec_()
                return 0
        if len(self.txt_1) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You cannot leave the field blank!!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        elif self.txt_1.isnumeric():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please enter a valid teamname\n(Name must contain atleast one character)!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        else:
            self.reset()
            self.Dialog.hide()
            self.lineEdit.setText("0")
            self.lineEdit_2.setText("0")
            self.lineEdit_3.setText("0")
            self.lineEdit_4.setText("0")
            self.lineEdit_5.setText("1000")
            self.lineEdit_6.setText("0")
            self.lineEdit_7.setText(self.txt_1)
            self.enable_rbs()

    def butnspress(self):
        Batsman = 'BAT'
        WicketKeeper = 'WK'
        Allrounder = 'AR'
        Bowler = 'BWL'
        sql1 = "SELECT Player,Value from stats WHERE Ctg = '" + Batsman + "';"
        sql2 = "SELECT Player,Value from stats WHERE Ctg = '" + WicketKeeper + "';"
        sql3 = "SELECT Player,Value from stats WHERE Ctg ='" + Allrounder + "';"
        sql4 = "SELECT Player,Value from stats WHERE Ctg = '" + Bowler + "';"

        cursor_obj.execute(sql1)
        x = cursor_obj.fetchall()
        cursor_obj.execute(sql4)
        y = cursor_obj.fetchall()
        cursor_obj.execute(sql3)
        z = cursor_obj.fetchall()
        cursor_obj.execute(sql2)
        w = cursor_obj.fetchall()

        batsmen = set()
        bowlers = set()
        allrounders = set()
        wcktkeepers = set()

        for k in x:
            batsmen.add(k[0])
            self.b.append(k[0])
            self.stats[k[0]] = k[1]
        for k in y:
            bowlers.add(k[0])
            self.stats[k[0]] = k[1]
            self.a.append(k[0])
        for k in w:
            wcktkeepers.add(k[0])
            self.stats[k[0]] = k[1]
            self.d.append(k[0])
        for k in z:
            allrounders.add(k[0])
            self.stats[k[0]] = k[1]
            self.c.append(k[0])

        self.li=set(self.list1)

        if self.radioButton.isChecked() == True:
            self.listWidget_2.clear()
            b1=batsmen-self.li
            for i in b1:
                item = QtWidgets.QListWidgetItem(i)
                self.listWidget_2.addItem(item)
        elif self.radioButton_2.isChecked() == True:
            self.listWidget_2.clear()
            b2=bowlers-self.li
            for i in b2:
                item = QtWidgets.QListWidgetItem(i)
                self.listWidget_2.addItem(item)
        elif self.radioButton_3.isChecked() == True:
            self.listWidget_2.clear()
            b3=allrounders-self.li
            for i in b3:
                item = QtWidgets.QListWidgetItem(i)
                self.listWidget_2.addItem(item)

        elif self.radioButton_4.isChecked() == True:
            self.listWidget_2.clear()
            b4=wcktkeepers-self.li
            for i in b4:
                item = QtWidgets.QListWidgetItem(i)
                self.listWidget_2.addItem(item)

    def removelist1(self,item):
        self.conditions_1(item.text(),item)
        self.totalcount = self.listWidget.count()

    def a_u(self,cat):
        self.avail_points -= self.stats[cat]
        self.used_points += self.stats[cat]

    def setting(self,item):
        self.lineEdit_5.setText(str(self.avail_points))
        self.lineEdit_6.setText(str(self.used_points))
        self.lineEdit_2.setText(str(self.bowlerscount))
        self.lineEdit.setText(str(self.batsmencount))
        self.lineEdit_3.setText(str(self.alrdscount))
        self.lineEdit_4.setText(str(self.wicketerscount))
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        self.listWidget.addItem(item.text())
        self.list1.append(item.text())


    def conditions_1(self,cat,item):
        self.error(cat)
        if cat in self.d and self.wicketerscount < 1 and self.totalcount < 11 and self.avail_points > -1:
                self.wicketerscount += 1
                self.a_u(cat)
                self.setting(item)

        elif cat in self.c and self.totalcount < 11 and self.avail_points > -1 and self.alrdscount<3:
                self.alrdscount += 1
                self.a_u(cat)
                self.setting(item)

        elif self.totalcount < 11 and self.avail_points > -1:
            if cat in self.b:
                self.batsmencount += 1
                self.a_u(cat)

                self.setting(item)
            if cat in self.a:
                self.bowlerscount += 1
                self.a_u(cat)
                self.setting(item)


    def conditions_3(self,cat):
        self.error(cat)
        if cat in self.a:
            self.bowlerscount += 1
        elif cat in self.d:
            self.wicketerscount += 1
        elif cat in self.c:
            self.alrdscount += 1
        elif cat in self.b:
            self.batsmencount += 1


        self.lineEdit_2.setText(str(self.bowlerscount))
        self.lineEdit.setText(str(self.batsmencount))
        self.lineEdit_3.setText(str(self.alrdscount))
        self.lineEdit_4.setText(str(self.wicketerscount))



    def removelist2(self,item):
        self.butnspress()
        self.listWidget.takeItem(self.listWidget.row(item))
        if item.text() in self.d:
            if self.radioButton_4.isChecked() == True:
                self.listWidget_2.addItem(item.text())
        elif item.text() in self.c:
            if self.radioButton_3.isChecked() == True:
                self.listWidget_2.addItem(item.text())
        elif item.text() in self.b:
            if self.radioButton.isChecked() == True:
                self.listWidget_2.addItem(item.text())
        elif item.text() in self.a:
            if self.radioButton_2.isChecked() == True:
                self.listWidget_2.addItem(item.text())

        self.list1.remove(item.text())
        self.totalcount = self.listWidget.count()
        self.conditions_2(item.text())

    def conditions_2(self,cat):
        self.avail_points += self.stats[cat]
        self.used_points -= self.stats[cat]
        if cat in self.a:
            self.bowlerscount -= 1
        elif cat in self.d:
            self.wicketerscount -= 1
        elif cat in self.c:
            self.alrdscount -= 1
        elif cat in self.b:
            self.batsmencount -= 1

        self.lineEdit_5.setText(str(self.avail_points))
        self.lineEdit_6.setText(str(self.used_points))
        self.lineEdit_2.setText(str(self.bowlerscount))
        self.lineEdit.setText(str(self.batsmencount))
        self.lineEdit_3.setText(str(self.alrdscount))
        self.lineEdit_4.setText(str(self.wicketerscount))







    def error(self,cat):
        self.msg = QtWidgets.QMessageBox()
        if cat in self.d:
            if self.wicketerscount > 0:
                self.msg.setIcon(QtWidgets.QMessageBox.Critical)
                # self.msg.setText("Error")
                self.msg.setInformativeText('Only 1 wicketkeeper is allowed!')
                self.msg.setWindowTitle("Error")
                self.msg.exec_()
        if cat in self.c:
            if self.alrdscount > 2:
                self.msg.setIcon(QtWidgets.QMessageBox.Critical)
                # self.msg.setText("Error")
                self.msg.setInformativeText('Allrounders not more than 3')
                self.msg.setWindowTitle("Error")
                self.msg.exec_()

        if self.totalcount > 10:
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            self.msg.setInformativeText('No more than 11 players allowed!')
            self.msg.setWindowTitle("Selection Error")
            self.msg.exec_()

        if self.totalcount < 11:
            return 0
        if self.wicketerscount < 1:
            return 0
        if self.avail_points <= -1:
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            self.msg.setInformativeText('Not enough points!')
            self.msg.setWindowTitle("Selection Cricket")
            self.msg.exec_()


        return 1

    def error_1(self):
        self.msg = QtWidgets.QMessageBox()
        if self.wicketerscount > 1:
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            # self.msg.setText("Error")
            self.msg.setInformativeText('Only 1 wicketkeeper is allowed!')
            self.msg.setWindowTitle("Error")
            self.msg.exec_()
            return 0
        elif self.alrdscount > 3:
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            # self.msg.setText("Error")
            self.msg.setInformativeText('Allrounders not more than 3')
            self.msg.setWindowTitle("Error")
            self.msg.exec_()
            return 0
        elif self.totalcount >=12:
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            self.msg.setInformativeText('No more than 11 players allowed!')
            self.msg.setWindowTitle("Selection Error")
            self.msg.exec_()
            return 0
        elif self.totalcount < 11:
            return 0
        elif self.wicketerscount < 1:
            return 0
        elif self.avail_points <= -1:
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            self.msg.setInformativeText('Not enough points!')
            self.msg.setWindowTitle("Selection Cricket")
            self.msg.exec_()
            return 0

        return 1

    def file_save(self):
        if not self.error_1():  # IF THERE IS AN ERROR
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setInformativeText(' 😪Insufficient Players OR Points !!')
            msg.setWindowTitle("Fantasy Cricket")
            msg.exec_()
        elif self.error_1():  # IF NO ERROR
            try:
                cursor_obj.execute("SELECT DISTINCT name FROM teams;")
                x = cursor_obj.fetchall()
                for i in x:
                    if self.lineEdit_7.text() == i[0]:  # CHECKING IF THE TEAMNAME ALREADY EXISTS
                        print('Updating')
                        cursor_obj.execute(
                            "DELETE  FROM teams WHERE name='" + self.lineEdit_7.text() + "';")  # DELETING TO UPDATE TEAM
            except:
                print('error')
            for i in range(self.listWidget.count()):

                try:
                    cursor_obj.execute("INSERT INTO teams (name,players,value) VALUES (?,?,?)",
                                     (self.lineEdit_7.text(), self.list1[i], player_points[self.list1[i]]))

                    # self.file_evaluate()
                except:
                    print('error in operation!')
            conn_obj.commit()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setInformativeText('Team Saved Successfully')
            msg.setWindowTitle("Fantasy Cricket")
            msg.exec_()

        else:
            print('---error in operation')

# Open team window
    def open_team(self):
        self.Form = QtWidgets.QWidget()
        self.ui = open_1()
        self.ui.setupUi(self.Form)
        self.Form.show()
        self.ui.pushButton.clicked.connect(self.open_team_next)

    def open_team_next(self):
        self.reset()
        teamname=self.ui.comboBox.currentText()
        self.lineEdit_7.setText(teamname)
        self.enable_rbs()
        cursor_obj.execute("SELECT Players FROM teams WHERE Name= '" + teamname + "';")
        x=cursor_obj.fetchall()
        score=[]
        for i in x:
            cursor_obj.execute("SELECT Value FROM stats WHERE Player='" + i[0] + "';")
            y = cursor_obj.fetchone()
            score.append(y[0])
        sum = 0
        for i in score:
            sum += i
        self.listWidget.clear()
        self.butnspress()
        for i in x:
            self.listWidget.addItem(i[0])
            self.list1.append(i[0])
            self.conditions_3(i[0])
            self.used_points = sum
            self.avail_points = 1000 - sum
            self.lineEdit_5.setText(str(self.avail_points))
            self.lineEdit_6.setText(str(self.used_points))
            self.Form.close()

    def reset(self):
        self.enable_rbs()
        self.butnspress()
        self.used_points = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.totalcount = 0
        self.avail_points = 1000
        self.lineEdit_5.setText(str(self.avail_points))
        self.lineEdit_6.setText(str(self.used_points))
        self.lineEdit_2.setText(str(self.bowlerscount))
        self.lineEdit.setText(str(self.batsmencount))
        self.lineEdit_3.setText(str(self.alrdscount))
        self.lineEdit_4.setText(str(self.wicketerscount))
        self.list1.clear()
        self.butnspress()

        self.listWidget.clear()


    def evaluate(self):
        self.Form = QtWidgets.QWidget()
        self.ui_9 = eval_1()
        self.ui_9.setupUi(self.Form)
        self.Form.show()
        cursor_obj.execute("SELECT DISTINCT Name FROM teams;")
        self.team_eval=cursor_obj.fetchall()
        for x in self.team_eval:
            self.ui_9.comboBox.addItem(x[0])
        self.ui_9.comboBox_2.addItem("Match 1")
        self.ui_9.pushButton.clicked.connect(self.eval_2)

    def eval_2(self):
        self.ui_9.l1.clear()
        self.ui_9.l2.clear()
        self.team_name=self.ui_9.comboBox.currentText()
        cursor_obj.execute("SELECT Players FROM teams WHERE Name= '"+self.team_name+"';")
        ll1=cursor_obj.fetchall()
        for m in ll1:
            self.ui_9.l1.addItem(m[0])

        cursor_obj.execute("SELECT Value FROM teams WHERE Name= '" + self.team_name + "';")
        ll2=cursor_obj.fetchall()

        self.sum_1=0
        for n in ll2:
            self.ui_9.l2.addItem(str(n[0]))
            self.sum_1+=int(n[0])

        self.ui_9.lineEdit.setText(str(self.sum_1))









    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.label_5.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.label_3.setText(_translate("MainWindow", "AllRounders(AR)"))
        self.label_2.setText(_translate("MainWindow", "Wicket-keeper(WK)"))
        self.radioButton.setText(_translate("MainWindow", "BAT"))
        self.radioButton_2.setText(_translate("MainWindow", "BOW"))
        self.radioButton_3.setText(_translate("MainWindow", "AR"))
        self.radioButton_4.setText(_translate("MainWindow", "WK"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Your Selections</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Points Available "))
        self.label_7.setText(_translate("MainWindow", "Points Used"))
        self.label_8.setText(_translate("MainWindow", "Team Name"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
