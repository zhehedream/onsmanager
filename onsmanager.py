#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'onsmanager.ui'
#
# Created: Mon Jul 25 15:20:42 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    data=[]
    ons_cmd=''
    config=''
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(792, 478)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 410, 211, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 410, 211, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 791, 411))
        self.listWidget.setIconSize(QtCore.QSize(128,128))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(22)
        self.listWidget.setFont(font)
        self.listWidget.setViewMode(QtGui.QListView.ListMode)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 792, 28))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu = QtGui.QMenu(self.menuBar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menuBar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_NScripter = QtGui.QAction(MainWindow)
        self.action_NScripter.setObjectName(_fromUtf8("action_NScripter"))
        self.action_4 = QtGui.QAction(MainWindow)
        self.action_4.setObjectName(_fromUtf8("action_4"))
        self.action_5 = QtGui.QAction(MainWindow)
        self.action_5.setObjectName(_fromUtf8("action_5"))
        self.action_6 = QtGui.QAction(MainWindow)
        self.action_6.setObjectName(_fromUtf8("action_6"))
        self.action_7 = QtGui.QAction(MainWindow)
        self.action_7.setObjectName(_fromUtf8("action_7"))
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_NScripter)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menu_2.addAction(self.action_7)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.connectbutton()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "OnsManager   Made By Zhehe   2016.07.24", None))
        self.pushButton.setText(_translate("MainWindow", "全屏模式启动", None))
        self.pushButton_2.setText(_translate("MainWindow", "窗口模式启动", None))
        self.menu.setTitle(_translate("MainWindow", "管理", None))
        self.menu_2.setTitle(_translate("MainWindow", "帮助", None))
        self.action.setText(_translate("MainWindow", "窗口化运行", None))
        self.action_2.setText(_translate("MainWindow", "全屏运行", None))
        self.action_NScripter.setText(_translate("MainWindow", "设置NScript引导器", None))
        self.action_4.setText(_translate("MainWindow", "添加说明文字", None))
        self.action_5.setText(_translate("MainWindow", "退出", None))
        self.action_6.setText(_translate("MainWindow", "如何添加项目？", None))
        self.action_7.setText(_translate("MainWindow", "关于", None))

    def connectbutton(self):
        self.pushButton.clicked.connect(self.runasfs)
        self.pushButton_2.clicked.connect(self.run)
        self.action.triggered.connect(self.run)
        self.action_2.triggered.connect(self.runasfs)
        self.action_NScripter.triggered.connect(self.inputcmd)
        self.action_4.triggered.connect(self.inputdescribe)
        self.action_6.triggered.connect(self.howtoadd)
        self.action_7.triggered.connect(self.about)
        self.action_5.triggered.connect(QtCore.QCoreApplication.instance().quit)
    
    def additem(self,png,text,name):
        item=QtGui.QListWidgetItem(text)
        item.setIcon(QtGui.QIcon(png))
        self.listWidget.addItem(item)
        self.data.append(name)
        self.listWidget.setCurrentRow(0)

    def howtoadd(self):
        QtGui.QMessageBox.about(None, '如何添加', "将游戏文件夹复制到脚本同一目录下，\n或者用ln -s建立链接" )

    def about(self):
        QtGui.QMessageBox.about(None, '关于', "一个简单的Onscripter前端" )

    def runasfs(self):
        import os
        if len(self.data)==0:
            return;
        cmd='cd '+self.data[self.listWidget.currentRow()]+' && '+self.ons_cmd+' --fullscreen &';
        os.system(cmd);

    def run(self):
        import os
        if len(self.data)==0:
            return;
        cmd='cd '+self.data[self.listWidget.currentRow()]+' && '+self.ons_cmd+' &';
        os.system(cmd);

    def inputcmd(self):
        cmd,ok = QtGui.QInputDialog.getText(None,"NScript Path","Command:",QtGui.QLineEdit.Normal,self.ons_cmd);
        if ok and (not len(cmd)==0):
            self.ons_cmd=cmd
            f=open(self.config,'w')
            f.write(cmd)
            f.close()

    def inputdescribe(self):
        temp=self.listWidget.selectedItems()[0].text()
        temp=temp.split('\n')
        if len(temp)<2:
           temp=''
        else:
           temp=temp[1]
        describe,ok = QtGui.QInputDialog.getText(None,"添加说明文字","说明文字:",QtGui.QLineEdit.Normal,temp);
        if ok:
            f=open(self.data[self.listWidget.currentRow()]+'/describe.txt','w')
            f.write(describe)
            f.close()
        refreshitem(self)
        #if ok and (not len(describe)==0):

def refreshitem(ui):
    import os

    ui.listWidget.clear()
    ui.data=[]
    root = os.getcwd();
    default=root+"/default_icon.png";
    config=root+"/onscmd.txt"
    f=open(config,'r')
    ons_cmd=f.readline().strip('\n')
    f.close()
    ui.ons_cmd=ons_cmd
    ui.config=config
    for i in os.listdir(root):
        pathname=os.path.join(root,i);
        if os.path.isdir(pathname):
            if i[0]!='.':
                icon=pathname+"/icon.png";
                if not os.path.exists(icon):
                    icon=default;
                gamename=i;
                describe=pathname+"/describe.txt";
                if os.path.exists(describe):
                    f=open(describe,'r')
                    line=f.readline()
                    f.close()
                else:
                    line=''
                text=i+'\n'+line;
                ui.additem(icon,text,i)


if __name__ == "__main__":
    import sys,os
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    refreshitem(ui)
    sys.exit(app.exec_())

