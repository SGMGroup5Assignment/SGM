# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainPage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
    
        #this section holds logo in top left corner
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(900, 800)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 270, 91))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.logoLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.logoLayout.setObjectName(_fromUtf8("logoLayout"))
        self.logoPicLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.logoPicLabel.setText(_fromUtf8(""))
        self.logoPicLabel.setObjectName(_fromUtf8("logoPicLabel"))
        self.logoPicLabel.setObjectName(_fromUtf8("Logo"))
        self.logoPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("logo_SGM2.png")))
        self.logoLayout.addWidget(self.logoPicLabel)

        #this section contains all the buttons of countries and help
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 781, 101))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.buttonLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.buttonLayout.setObjectName(_fromUtf8("buttonLayout"))
        
        self.irelandBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.irelandBtn.setStyleSheet("background-color: #00bfff")
        self.irelandBtn.setFont(font)
        self.irelandBtn.setObjectName(_fromUtf8("irelandBtn"))
        self.buttonLayout.addWidget(self.irelandBtn)

        self.franceBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.franceBtn.setStyleSheet("background-color: #00bfff")
        self.franceBtn.setFont(font)
        self.franceBtn.setObjectName(_fromUtf8("franceBtn"))
        self.buttonLayout.addWidget(self.franceBtn)

        self.germanyBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.germanyBtn.setStyleSheet("background-color: #00bfff")
        self.germanyBtn.setFont(font)
        self.germanyBtn.setObjectName(_fromUtf8("germanyBtn"))
        self.buttonLayout.addWidget(self.germanyBtn)

        self.finlandBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.finlandBtn.setStyleSheet("background-color: #00bfff")
        self.finlandBtn.setFont(font)
        self.finlandBtn.setObjectName(_fromUtf8("finlandBtn"))
        self.buttonLayout.addWidget(self.finlandBtn)

        self.koreaBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.koreaBtn.setStyleSheet("background-color: #00bfff")
        self.koreaBtn.setFont(font)
        self.koreaBtn.setObjectName(_fromUtf8("koreaBtn"))
        self.buttonLayout.addWidget(self.koreaBtn)
        
        self.helpBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.helpBtn.setStyleSheet("background-color: yellow")
        self.helpBtn.setFont(font)
        self.helpBtn.setObjectName(_fromUtf8("helpBtn"))
        self.buttonLayout.addWidget(self.helpBtn)
        
        #this layout holds the text title of portal
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 20, 541, 91))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.titleLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.titleLayout.setObjectName(_fromUtf8("titleLayout"))
        self.mainTitle = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rockwell"))
        font.setPointSize(44)
        font.setBold(True)
        font.setWeight(75)
        self.mainTitle.setStyleSheet("background-color: grey") #remove from here if any issues occur
        self.mainTitle.setFont(font)
        self.mainTitle.setObjectName(_fromUtf8("mainTitle"))
        self.titleLayout.addWidget(self.mainTitle)
        
        #this layout holds the image of students on left hand side
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(410, 250, 381, 361))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.aboutTextLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.aboutTextLayout.setObjectName(_fromUtf8("aboutTextLayout"))
        self.AboutTextBrowser = QtGui.QTextBrowser(self.verticalLayoutWidget_3)
        self.AboutTextBrowser.setObjectName(_fromUtf8("AboutTextBrowser"))
        self.aboutTextLayout.addWidget(self.AboutTextBrowser)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 250, 350, 350))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.picAboutLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.picAboutLayout.setObjectName(_fromUtf8("picAboutLayout"))
        self.aboutPicLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.aboutPicLabel.setText(_fromUtf8(""))
        self.aboutPicLabel.setObjectName(_fromUtf8("aboutPicLabel"))
        self.picAboutLayout.addWidget(self.aboutPicLabel)
        self.aboutPicLabel.setObjectName(_fromUtf8("AboutImage"))
        self.aboutPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("study_abroad.jpg")))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "AviateNEducate Main Page", None))
        self.mainTitle.setText(_translate("MainWindow", "  AviateNEducate", None))
        self.irelandBtn.setText(_translate("AviateNEducate", "Ireland", None))
        self.franceBtn.setText(_translate("AviateNEducate", "France", None))
        self.germanyBtn.setText(_translate("AviateNEducate", "Germany", None))
        self.finlandBtn.setText(_translate("AviateNEducate", "Finland", None))
        self.koreaBtn.setText(_translate("AviateNEducate", "Korea", None))
        self.helpBtn.setText(_translate("AviateNEducate", "Help", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Background, QtCore.Qt.darkCyan)
    MainWindow.setPalette(palette)
    #ui.__init__()
    #MainWindow.setWindowIcon(QtGui.QIcon('planeicon.png'))
    MainWindow.show()
    app.exec_()
