# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SGM2Group5.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import random
import gettext
fr = gettext.translation('fr', localedir='locale', languages=['fr'])
fr.install()

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

class Ui_AviateNEducate(object):
    def setupUi(self, AviateNEducate):
        AviateNEducate.setObjectName(_fromUtf8("AviateNEducate"))
        AviateNEducate.resize(1129, 1000)
        self.centralwidget = QtGui.QWidget(AviateNEducate)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 311, 85))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.TitleLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.TitleLayout.setObjectName(_fromUtf8("TitleLayout"))
        self.AviateNEducate_Title = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Iskoola Pota"))
        font.setPointSize(24)
        self.AviateNEducate_Title.setFont(font)
        self.AviateNEducate_Title.setObjectName(_fromUtf8("AviateNEducate_Title"))
        self.TitleLayout.addWidget(self.AviateNEducate_Title)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(560, 200, 311, 151))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.UniLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.UniLayout.setObjectName(_fromUtf8("UniLayout"))


        #Section for Uni Text

        self.UniTextEdit = QtGui.QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.UniTextEdit.setObjectName(_fromUtf8("UniTextEdit"))
        self.UniLayout.addWidget(self.UniTextEdit)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 360, 181, 80))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.SecondMenuLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.SecondMenuLayout.setObjectName(_fromUtf8("SecondMenuLayout"))
        self.AccomInfo = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AccomInfo.setFont(font)
        self.AccomInfo.setObjectName(_fromUtf8("AccomInfo"))
        self.SecondMenuLayout.addWidget(self.AccomInfo)
        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(20, 200, 211, 151))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.CountryPicLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.CountryPicLayout.setObjectName(_fromUtf8("CountryPicLayout"))
        self.CountryPicLabel = QtGui.QLabel(self.horizontalLayoutWidget_6)
        self.CountryPicLabel.setObjectName(_fromUtf8("CountryPicLabel"))
        self.CountryPicLayout.addWidget(self.CountryPicLabel)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(560, 450, 531, 151))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.FundingLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.FundingLayout.setObjectName(_fromUtf8("FundingLayout"))
        self.FundingTextEdit = QtGui.QPlainTextEdit(self.horizontalLayoutWidget_3)
        self.FundingTextEdit.setObjectName(_fromUtf8("FundingTextEdit"))
        self.FundingLayout.addWidget(self.FundingTextEdit)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 450, 531, 151))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.AccomLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.AccomLayout.setObjectName(_fromUtf8("AccomLayout"))
        self.AccomTextEdit = QtGui.QPlainTextEdit(self.horizontalLayoutWidget_4)
        self.AccomTextEdit.setObjectName(_fromUtf8("AccomTextEdit"))
        self.AccomLayout.addWidget(self.AccomTextEdit)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 610, 1071, 80))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.ThirdMenuLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.ThirdMenuLayout.setObjectName(_fromUtf8("ThirdMenuLayout"))
        self.StudnetInfo = QtGui.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.StudnetInfo.setFont(font)
        self.StudnetInfo.setObjectName(_fromUtf8("StudentInfo"))
        self.ThirdMenuLayout.addWidget(self.StudnetInfo)
        self.horizontalLayoutWidget_7 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(60, 710, 321, 191))
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.Student1ExpLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.Student1ExpLayout.setObjectName(_fromUtf8("Student1ExpLayout"))
        self.Student1PicLabel = QtGui.QLabel(self.horizontalLayoutWidget_7)
        self.Student1PicLabel.setObjectName(_fromUtf8("Student1PicLabel"))
        self.Student1ExpLayout.addWidget(self.Student1PicLabel)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 110, 531, 80))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.FirstMenuLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.FirstMenuLayout.setObjectName(_fromUtf8("FirstMenuLayout"))
        self.CountryInfo = QtGui.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CountryInfo.setFont(font)
        self.CountryInfo.setObjectName(_fromUtf8("CountryInfo"))
        self.FirstMenuLayout.addWidget(self.CountryInfo)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(640, 10, 221, 61))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.FirstComboBox = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.FirstComboBox.setObjectName(_fromUtf8("FirstComboBox"))
        self.CountryLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(11)
        self.CountryLabel.setFont(font)
        self.CountryLabel.setObjectName(_fromUtf8("CountryLabel"))
        self.FirstComboBox.addWidget(self.CountryLabel)

        # Language selection box
        self.countryComboBox = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.countryComboBox.setObjectName(_fromUtf8("countryComboBox"))
        self.FirstComboBox.addWidget(self.countryComboBox)
        self.countryComboBox.addItem("English")
        self.countryComboBox.addItem("French")
        self.countryComboBox.addItem("German")



        self.verticalLayoutWidget_6 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(870, 10, 221, 61))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.SecondComboBox = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.SecondComboBox.setObjectName(_fromUtf8("SecondComboBox"))
        self.ColourSelectLabel = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(11)
        self.ColourSelectLabel.setFont(font)
        self.ColourSelectLabel.setObjectName(_fromUtf8("ColourSelectLabel"))
        self.SecondComboBox.addWidget(self.ColourSelectLabel)

        # Colour selection box
        self.ColourComboBox = QtGui.QComboBox(self.verticalLayoutWidget_6)
        self.ColourComboBox.setObjectName(_fromUtf8("ColourComboBox"))
        self.SecondComboBox.addWidget(self.ColourComboBox)
        self.ColourComboBox.addItem(" ")
        self.ColourComboBox.addItem("Green")
        self.ColourComboBox.addItem("Yellow")
        self.ColourComboBox.addItem("Blue")
        self.ColourComboBox.addItem("Orange")
        self.ColourComboBox.addItem("Purple")
        self.ColourComboBox.addItem("Pink")
        self.ColourComboBox.addItem("Red")

        self.verticalLayoutWidget_7 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(390, 10, 187, 80))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Zoom = QtGui.QCheckBox(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Zoom.setFont(font)
        self.Zoom.setObjectName(_fromUtf8("Zoom"))
        self.verticalLayout.addWidget(self.Zoom)
        self.verticalLayoutWidget_8 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(560, 110, 301, 80))
        self.verticalLayoutWidget_8.setObjectName(_fromUtf8("verticalLayoutWidget_8"))
        self.FirstMenuLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_8)
        self.FirstMenuLayout_2.setObjectName(_fromUtf8("FirstMenuLayout_2"))
        self.UniInfo = QtGui.QLabel(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UniInfo.setFont(font)
        self.UniInfo.setObjectName(_fromUtf8("UniInfo"))
        self.FirstMenuLayout_2.addWidget(self.UniInfo)
        self.verticalLayoutWidget_9 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(560, 360, 531, 80))
        self.verticalLayoutWidget_9.setObjectName(_fromUtf8("verticalLayoutWidget_9"))
        self.SecondMenuLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_9)
        self.SecondMenuLayout_2.setObjectName(_fromUtf8("SecondMenuLayout_2"))
        self.Funding = QtGui.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Funding.setFont(font)
        self.Funding.setObjectName(_fromUtf8("Funding"))
        self.SecondMenuLayout_2.addWidget(self.Funding)
        self.verticalLayoutWidget_10 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(239, 199, 311, 151))
        self.verticalLayoutWidget_10.setObjectName(_fromUtf8("verticalLayoutWidget_10"))
        self.CountryInfoLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_10)
        self.CountryInfoLayout.setObjectName(_fromUtf8("CountryInfoLayout"))
        self.CountryTextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget_10)
        self.CountryTextEdit.setObjectName(_fromUtf8("CountryTextEdit"))
        self.CountryInfoLayout.addWidget(self.CountryTextEdit)
        #Uni layout box
        self.verticalLayoutWidget_11 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(870, 120, 221, 61))
        self.verticalLayoutWidget_11.setObjectName(_fromUtf8("verticalLayoutWidget_11"))
        self.UniLayoutBox = QtGui.QVBoxLayout(self.verticalLayoutWidget_11)
        self.UniLayoutBox.setObjectName(_fromUtf8("UniLayoutBox"))
        self.ColourSelectLabel_2 = QtGui.QLabel(self.verticalLayoutWidget_11)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(11)
        #Uni drop down box
        self.ColourSelectLabel_2.setFont(font)
        self.ColourSelectLabel_2.setObjectName(_fromUtf8("ColourSelectLabel_2"))
        self.UniLayoutBox.addWidget(self.ColourSelectLabel_2)

        #Uni Combo Section
        self.UniComboBox = QtGui.QComboBox(self.verticalLayoutWidget_11)
        self.UniComboBox.setObjectName(_fromUtf8("UniComboBox"))
        self.UniLayoutBox.addWidget(self.UniComboBox)

        self.uniSelected = QtGui.QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.uniSelected.setGeometry(QtCore.QRect(560, 200, 311, 151))
        self.uniSelected.setObjectName(_fromUtf8("uniSelected"))



        self.horizontalLayoutWidget_8 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(880, 200, 211, 151))
        self.horizontalLayoutWidget_8.setObjectName(_fromUtf8("horizontalLayoutWidget_8"))
        self.CountryPicLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.CountryPicLayout_2.setObjectName(_fromUtf8("CountryPicLayout_2"))
        self.UniversityPicLabel = QtGui.QLabel(self.horizontalLayoutWidget_8)
        self.UniversityPicLabel.setObjectName(_fromUtf8("UniversityPicLabel"))
        self.CountryPicLayout_2.addWidget(self.UniversityPicLabel)
        self.verticalLayoutWidget_12 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(230, 360, 111, 80))
        self.verticalLayoutWidget_12.setObjectName(_fromUtf8("verticalLayoutWidget_12"))
        self.FundCheapLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_12)
        self.FundCheapLayout.setObjectName(_fromUtf8("FundCheapLayout"))
        self.LCostRadioButton = QtGui.QRadioButton(self.verticalLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.LCostRadioButton.setFont(font)
        self.LCostRadioButton.setObjectName(_fromUtf8("LCostRadioButton"))
        self.FundCheapLayout.addWidget(self.LCostRadioButton)
        self.verticalLayoutWidget_13 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(390, 360, 115, 80))
        self.verticalLayoutWidget_13.setObjectName(_fromUtf8("verticalLayoutWidget_13"))
        self.FundExpensLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_13)
        self.FundExpensLayout.setObjectName(_fromUtf8("FundExpensLayout"))
        self.HCostRadioButton = QtGui.QRadioButton(self.verticalLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        self.HCostRadioButton.setFont(font)
        self.HCostRadioButton.setObjectName(_fromUtf8("HCostRadioButton"))
        self.FundExpensLayout.addWidget(self.HCostRadioButton)
        self.horizontalLayoutWidget_9 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(410, 710, 301, 191))
        self.horizontalLayoutWidget_9.setObjectName(_fromUtf8("horizontalLayoutWidget_9"))
        self.Student2ExpLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.Student2ExpLayout.setObjectName(_fromUtf8("Student2ExpLayout"))
        self.Student2PicLabel = QtGui.QLabel(self.horizontalLayoutWidget_9)
        self.Student2PicLabel.setObjectName(_fromUtf8("Student2PicLabel"))
        self.Student2ExpLayout.addWidget(self.Student2PicLabel)
        self.horizontalLayoutWidget_10 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(740, 710, 311, 191))
        self.horizontalLayoutWidget_10.setObjectName(_fromUtf8("horizontalLayoutWidget_10"))
        self.Student3ExpLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.Student3ExpLayout.setObjectName(_fromUtf8("Student3ExpLayout"))
        self.Student3PicLabel = QtGui.QLabel(self.horizontalLayoutWidget_10)
        self.Student3PicLabel.setObjectName(_fromUtf8("Student3PicLabel"))
        self.Student3ExpLayout.addWidget(self.Student3PicLabel)
        self.horizontalLayoutWidget_11 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(60, 920, 321, 191))
        self.horizontalLayoutWidget_11.setObjectName(_fromUtf8("horizontalLayoutWidget_11"))
        self.Student1ExpLayoutText = QtGui.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.Student1ExpLayoutText.setObjectName(_fromUtf8("Student1ExpLayoutText"))
        self.Student1TextEdit = QtGui.QPlainTextEdit(self.horizontalLayoutWidget_11)
        self.Student1TextEdit.setObjectName(_fromUtf8("Student1TextEdit"))
        self.Student1ExpLayoutText.addWidget(self.Student1TextEdit)
        self.horizontalLayoutWidget_12 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(410, 920, 301, 191))
        self.horizontalLayoutWidget_12.setObjectName(_fromUtf8("horizontalLayoutWidget_12"))
        self.Student2ExpLayoutText = QtGui.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.Student2ExpLayoutText.setObjectName(_fromUtf8("Student2ExpLayoutText"))
        self.Student2TextEdit = QtGui.QPlainTextEdit(self.horizontalLayoutWidget_12)
        self.Student2TextEdit.setObjectName(_fromUtf8("Student2TextEdit"))
        self.Student2ExpLayoutText.addWidget(self.Student2TextEdit)
        self.horizontalLayoutWidget_13 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(740, 920, 311, 191))
        self.horizontalLayoutWidget_13.setObjectName(_fromUtf8("horizontalLayoutWidget_13"))
        self.Student3ExpLayoutText = QtGui.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.Student3ExpLayoutText.setObjectName(_fromUtf8("Student3ExpLayoutText"))
        self.Student3TextEdit = QtGui.QPlainTextEdit(self.horizontalLayoutWidget_13)
        self.Student3TextEdit.setObjectName(_fromUtf8("Student3TextEdit"))
        self.Student3ExpLayoutText.addWidget(self.Student3TextEdit)

        AviateNEducate.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(AviateNEducate)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        AviateNEducate.setStatusBar(self.statusbar)

        self.retranslateUi(AviateNEducate)
        QtCore.QMetaObject.connectSlotsByName(AviateNEducate)

    def retranslateUi(self, AviateNEducate):
        AviateNEducate.setWindowTitle(_translate("AviateNEducate", "AviateNEducate", None))
        self.AviateNEducate_Title.setText(_translate("AviateNEducate", "AviateNEducate", None))
        self.AccomInfo.setText(_translate("AviateNEducate", "Accommodation ", None))
        self.CountryPicLabel.setText(_translate("AviateNEducate", "TextLabel", None))
        self.StudnetInfo.setText(_translate("AviateNEducate", "Student Experience", None))
        self.Student1PicLabel.setText(_translate("AviateNEducate", "TextLabel", None))
        self.CountryInfo.setText(_translate("AviateNEducate", "Information on the Country", None))
        self.CountryLabel.setText(_translate("AviateNEducate", "Select Language:", None))
        self.ColourSelectLabel.setText(_translate("AviateNEducate", "Select Colour:", None))
        self.Zoom.setText(_translate("AviateNEducate", "Enlarge Window", None))
        self.UniInfo.setText(_translate("AviateNEducate", "University Options", None))
        self.Funding.setText(_translate("AviateNEducate", "Funding", None))
        self.ColourSelectLabel_2.setText(_translate("AviateNEducate", "Select University:", None))
        self.UniversityPicLabel.setText(_translate("AviateNEducate", "TextLabel", None))
        self.LCostRadioButton.setText(_translate("AviateNEducate", "Low Cost", None))
        self.HCostRadioButton.setText(_translate("AviateNEducate", "High Cost", None))
        self.Student2PicLabel.setText(_translate("AviateNEducate", "TextLabel", None))
        self.Student3PicLabel.setText(_translate("AviateNEducate", "TextLabel", None))

    def dispmodule(self, text):
        self.uniSelected.setText(text)

    #Information and pictures for each university
    def loaduni(self,text):
        if text == "Dublin Institute of Technology":
            self.UniversityPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("DIT.jpg")))
            self.UniversityPicLabel.setObjectName(_fromUtf8("DIT"))
            self.CountryPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Ireland.jpg")))
            self.CountryPicLabel.setObjectName(_fromUtf8("Ireland"))
            self.Student1PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womanone.jpg")))
            self.Student1PicLabel.setObjectName(_fromUtf8("p1"))
            self.Student2PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("manone.jpg")))
            self.Student2PicLabel.setObjectName(_fromUtf8("p2"))
            self.Student3PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womantwo.jpg")))
            self.Student3PicLabel.setObjectName(_fromUtf8("p3"))
    
        if text == "Dublin City University":
            self.UniversityPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("DCU.jpg")))
            self.UniversityPicLabel.setObjectName(_fromUtf8("DCU"))
            self.CountryPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Ireland.jpg")))
            self.CountryPicLabel.setObjectName(_fromUtf8("Ireland"))
            self.Student1PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("mantwo.jpg")))
            self.Student1PicLabel.setObjectName(_fromUtf8("p4"))
            self.Student2PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womanthree.jpg")))
            self.Student2PicLabel.setObjectName(_fromUtf8("p5"))
            self.Student3PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("manthree.jpg")))
            self.Student3PicLabel.setObjectName(_fromUtf8("p6"))

        if text == "University College Dublin":
            self.UniversityPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("UCD.jpg")))
            self.UniversityPicLabel.setObjectName(_fromUtf8("UCD"))
            self.CountryPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Ireland.jpg")))
            self.CountryPicLabel.setObjectName(_fromUtf8("Ireland"))
            self.Student1PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womanfour.jpg")))
            self.Student1PicLabel.setObjectName(_fromUtf8("p7"))
            self.Student2PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("manfour.jpg")))
            self.Student2PicLabel.setObjectName(_fromUtf8("p8"))
            self.Student3PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womanone.jpg")))
            self.Student3PicLabel.setObjectName(_fromUtf8("p9"))
    
        if text == "Hochschule Darmstadt":
            self.UniversityPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Darmstadt.jpg")))
            self.UniversityPicLabel.setObjectName(_fromUtf8("Darmstadt"))
            self.CountryPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Germany.jpg")))
            self.CountryPicLabel.setObjectName(_fromUtf8("Germany"))
            self.Student1PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womanone.jpg")))
            self.Student1PicLabel.setObjectName(_fromUtf8("p10"))
            self.Student2PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womantwo.jpg")))
            self.Student2PicLabel.setObjectName(_fromUtf8("p11"))
            self.Student3PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womanthree.jpg")))
            self.Student3PicLabel.setObjectName(_fromUtf8("p12"))

        if text == "Freie Universität Berlin":
            self.UniversityPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Berlin.jpg")))
            self.UniversityPicLabel.setObjectName(_fromUtf8("Berlin"))
            self.CountryPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Germany.jpg")))
            self.CountryPicLabel.setObjectName(_fromUtf8("Germany"))
            self.Student1PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womanfour.jpg")))
            self.Student1PicLabel.setObjectName(_fromUtf8("p13"))
            self.Student2PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("manone.jpg")))
            self.Student2PicLabel.setObjectName(_fromUtf8("p14"))
            self.Student3PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("mantwo.jpg")))
            self.Student3PicLabel.setObjectName(_fromUtf8("p15"))
    
        if text == "Universität zu KölnNetworking":
            self.UniversityPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Koln.jpg")))
            self.UniversityPicLabel.setObjectName(_fromUtf8("Koln"))
            self.CountryPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Germany.jpg")))
            self.CountryPicLabel.setObjectName(_fromUtf8("Germany"))
            self.Student1PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("manthree.jpg")))
            self.Student1PicLabel.setObjectName(_fromUtf8("p16"))
            self.Student2PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("manfour.jpg")))
            self.Student2PicLabel.setObjectName(_fromUtf8("p17"))
            self.Student3PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womanone.jpg")))
            self.Student3PicLabel.setObjectName(_fromUtf8("p18"))

        if text == "University of Paris":
            self.UniversityPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Paris.jpg")))
            self.UniversityPicLabel.setObjectName(_fromUtf8("Paris"))
            self.CountryPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("France.jpg")))
            self.CountryPicLabel.setObjectName(_fromUtf8("France"))
            self.Student1PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womantwo.jpg")))
            self.Student1PicLabel.setObjectName(_fromUtf8("p19"))
            self.Student2PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womanthree.jpg")))
            self.Student2PicLabel.setObjectName(_fromUtf8("p20"))
            self.Student3PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("manfour.jpg")))
            self.Student3PicLabel.setObjectName(_fromUtf8("p21"))
    
        if text == "University of Lyon":
            self.UniversityPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Lyon.jpg")))
            self.UniversityPicLabel.setObjectName(_fromUtf8("Lyon"))
            self.CountryPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("France.jpg")))
            self.CountryPicLabel.setObjectName(_fromUtf8("France"))
            self.Student1PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womanfour.jpg")))
            self.Student1PicLabel.setObjectName(_fromUtf8("p22"))
            self.Student2PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("manone.jpg")))
            self.Student2PicLabel.setObjectName(_fromUtf8("p23"))
            self.Student3PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("mantwo.jpg")))
            self.Student3PicLabel.setObjectName(_fromUtf8("p24"))
        
        if text == "University of Marseille":
            self.UniversityPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Marseille.jpg")))
            self.UniversityPicLabel.setObjectName(_fromUtf8("Marseille"))
            self.CountryPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("France.jpg")))
            self.CountryPicLabel.setObjectName(_fromUtf8("France"))
            self.Student1PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("manthree.jpg")))
            self.Student1PicLabel.setObjectName(_fromUtf8("p25"))
            self.Student2PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womanfour.jpg")))
            self.Student2PicLabel.setObjectName(_fromUtf8("p26"))
            self.Student3PicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("womanone.jpg")))
            self.Student3PicLabel.setObjectName(_fromUtf8("p27"))

    #Pictures for each differnt language
    #def loadpictures(self, text):

        #if text == "English":
        #if text == "German":
        #if text == "French":
        

    #Uni drop down insertions
    def loadmodules(self, text):
        self.UniComboBox.clear()
        if text == "English":
            self.UniComboBox.addItem("--------Ireland--------")
            self.UniComboBox.addItem("Dublin Institute of Technology")
            self.UniComboBox.addItem("Dublin City University")
            self.UniComboBox.addItem("University College Dublin")
            self.UniComboBox.addItem("--------Germany--------")
            self.UniComboBox.addItem("Hochschule Darmstadt")
            self.UniComboBox.addItem("Freie Universität Berlin")
            self.UniComboBox.addItem("Universität zu KölnNetworking")
            self.UniComboBox.addItem("--------France--------")
            self.UniComboBox.addItem("University of Paris")
            self.UniComboBox.addItem("University of Lyon")
            self.UniComboBox.addItem("University of Marseille")
            self.AccomInfo.setText(_translate("AviateNEducate", "Accommodation ", None))
            self.StudnetInfo.setText(_translate("AviateNEducate", "Student Experience", None))
            self.CountryInfo.setText(_translate("AviateNEducate", "Information on the Country", None))
            self.CountryLabel.setText(_translate("AviateNEducate", "Select Language:", None))
            self.ColourSelectLabel.setText(_translate("AviateNEducate", "Select Colour:", None))
            self.Zoom.setText(_translate("AviateNEducate", "Enlarge Window", None))
            self.UniInfo.setText(_translate("AviateNEducate", "University Options", None))
            self.Funding.setText(_translate("AviateNEducate", "Funding", None))
            self.ColourSelectLabel_2.setText(_translate("AviateNEducate", "Select University:", None))
            self.LCostRadioButton.setText(_translate("AviateNEducate", "Low Cost", None))
            self.HCostRadioButton.setText(_translate("AviateNEducate", "High Cost", None))

        elif text == "German":
            self.UniComboBox.addItem("--------Irland--------")
            self.UniComboBox.addItem("Dublin Institute of Technology")
            self.UniComboBox.addItem("Dublin City University")
            self.UniComboBox.addItem("University College Dublin")
            self.UniComboBox.addItem("--------Deutschland--------")
            self.UniComboBox.addItem("Hochschule Darmstadt")
            self.UniComboBox.addItem("Freie Universität Berlin")
            self.UniComboBox.addItem("Universität zu KölnNetworking")
            self.UniComboBox.addItem("--------Frankreich--------")
            self.UniComboBox.addItem("University of Paris")
            self.UniComboBox.addItem("University of Lyon")
            self.UniComboBox.addItem("University of Marseille")
            self.AccomInfo.setText(_translate("AviateNEducate", "Unterkunft ", None))
            self.StudnetInfo.setText(_translate("AviateNEducate", "Studentenerfahrung", None))
            self.CountryInfo.setText(_translate("AviateNEducate", "Informationen über das Land", None))
            self.CountryLabel.setText(_translate("AviateNEducate", "Sprache auswählen:", None))
            self.ColourSelectLabel.setText(_translate("AviateNEducate", "Farbe auswählen:", None))
            self.Zoom.setText(_translate("AviateNEducate", "Fenster vergrößern", None))
            self.UniInfo.setText(_translate("AviateNEducate", "Universitätsoptionen", None))
            self.Funding.setText(_translate("AviateNEducate", "Finanzierung", None))
            self.ColourSelectLabel_2.setText(_translate("AviateNEducate", "Universität wählen:", None))
            self.LCostRadioButton.setText(_translate("AviateNEducate", "Kostengünstig", None))
            self.HCostRadioButton.setText(_translate("AviateNEducate", "Hohe Kosten", None))
          
        elif text == "French":
            self.UniComboBox.addItem("--------Irlande--------")
            self.UniComboBox.addItem("Dublin Institute of Technology")
            self.UniComboBox.addItem("Dublin City University")
            self.UniComboBox.addItem("University College Dublin")
            self.UniComboBox.addItem("--------Allemagne--------")
            self.UniComboBox.addItem("Hochschule Darmstadt")
            self.UniComboBox.addItem("Freie Universität Berlin")
            self.UniComboBox.addItem("Universität zu KölnNetworking")
            self.UniComboBox.addItem("--------France--------")
            self.UniComboBox.addItem("University of Paris")
            self.UniComboBox.addItem("University of Lyon")
            self.UniComboBox.addItem("University of Marseille")
            self.AccomInfo.setText(_translate("AviateNEducate", "Hébergement ", None))
            self.StudnetInfo.setText(_translate("AviateNEducate", "Expérience étudiante", None))
            self.CountryInfo.setText(_translate("AviateNEducate", "Informations sur le pays", None))
            self.CountryLabel.setText(_translate("AviateNEducate", "Choisir la langue:", None))
            self.ColourSelectLabel.setText(_translate("AviateNEducate", "Sélectionnez la couleur:", None))
            self.Zoom.setText(_translate("AviateNEducate", "Agrandir la fenêtre", None))
            self.UniInfo.setText(_translate("AviateNEducate", "Options universitaires", None))
            self.Funding.setText(_translate("AviateNEducate", "Financement", None))
            self.ColourSelectLabel_2.setText(_translate("AviateNEducate", "Sélectionnez Université:", None))
            self.LCostRadioButton.setText(_translate("AviateNEducate", "À bas prix", None))
            self.HCostRadioButton.setText(_translate("AviateNEducate", "Coût élevé", None))
        
        else:
            self.UniComboBox.clear()

    def loadcolours(self, text):
        if text == "Green":
            self.ColourComboBox.setStyleSheet("background-color:white")
            self.centralwidget.setStyleSheet("background-color:#b4ff8e ")
            self.CountryTextEdit.setStyleSheet("background-color: white")
            self.UniTextEdit.setStyleSheet("background-color: white")
            self.FundingTextEdit.setStyleSheet("background-color: white")
            self.AccomTextEdit.setStyleSheet("background-color: white")
            self.ColourComboBox.setStyleSheet("background-color: white")
            self.UniComboBox.setStyleSheet("background-color: white")
            self.countryComboBox.setStyleSheet("background-color: white")
            self.Student1TextEdit.setStyleSheet("background-color: white")
            self.Student2TextEdit.setStyleSheet("background-color: white")
            self.Student3TextEdit.setStyleSheet("background-color: white")


        elif text == "Yellow":
            self.ColourComboBox.setStyleSheet("background-color:white ")
            self.centralwidget.setStyleSheet("background-color:#e8ff8e ")
            self.CountryTextEdit.setStyleSheet("background-color: white")
            self.UniTextEdit.setStyleSheet("background-color: white")
            self.FundingTextEdit.setStyleSheet("background-color: white")
            self.AccomTextEdit.setStyleSheet("background-color: white")
            self.ColourComboBox.setStyleSheet("background-color: white")
            self.UniComboBox.setStyleSheet("background-color: white")
            self.countryComboBox.setStyleSheet("background-color: white")
            self.Student1TextEdit.setStyleSheet("background-color: white")
            self.Student2TextEdit.setStyleSheet("background-color: white")
            self.Student3TextEdit.setStyleSheet("background-color: white")

        elif text == "Blue":
            self.ColourComboBox.setStyleSheet("background-color:white")
            self.centralwidget.setStyleSheet("background-color:#8ec8ff ")
            self.CountryTextEdit.setStyleSheet("background-color: white")
            self.UniTextEdit.setStyleSheet("background-color: white")
            self.FundingTextEdit.setStyleSheet("background-color: white")
            self.AccomTextEdit.setStyleSheet("background-color: white")
            self.ColourComboBox.setStyleSheet("background-color: white")
            self.UniComboBox.setStyleSheet("background-color: white")
            self.countryComboBox.setStyleSheet("background-color: white")
            self.Student1TextEdit.setStyleSheet("background-color: white")
            self.Student2TextEdit.setStyleSheet("background-color: white")
            self.Student3TextEdit.setStyleSheet("background-color: white")

        elif text == "Orange":
            self.ColourComboBox.setStyleSheet("background-color:white")
            self.centralwidget.setStyleSheet("background-color:#f7be6a ")
            self.CountryTextEdit.setStyleSheet("background-color: white")
            self.UniTextEdit.setStyleSheet("background-color: white")
            self.FundingTextEdit.setStyleSheet("background-color: white")
            self.AccomTextEdit.setStyleSheet("background-color: white")
            self.ColourComboBox.setStyleSheet("background-color: white")
            self.UniComboBox.setStyleSheet("background-color: white")
            self.countryComboBox.setStyleSheet("background-color: white")
            self.Student1TextEdit.setStyleSheet("background-color: white")
            self.Student2TextEdit.setStyleSheet("background-color: white")
            self.Student3TextEdit.setStyleSheet("background-color: white")

        elif text == "Purple":
            self.ColourComboBox.setStyleSheet("background-color:white")
            self.centralwidget.setStyleSheet("background-color:#b79bff ")
            self.CountryTextEdit.setStyleSheet("background-color: white")
            self.UniTextEdit.setStyleSheet("background-color: white")
            self.FundingTextEdit.setStyleSheet("background-color: white")
            self.AccomTextEdit.setStyleSheet("background-color: white")
            self.ColourComboBox.setStyleSheet("background-color: white")
            self.UniComboBox.setStyleSheet("background-color: white")
            self.countryComboBox.setStyleSheet("background-color: white")
            self.Student1TextEdit.setStyleSheet("background-color: white")
            self.Student2TextEdit.setStyleSheet("background-color: white")
            self.Student3TextEdit.setStyleSheet("background-color: white")

        elif text == "Pink":
            self.ColourComboBox.setStyleSheet("background-color:white")
            self.centralwidget.setStyleSheet("background-color:#ff9bec ")
            self.CountryTextEdit.setStyleSheet("background-color: white")
            self.UniTextEdit.setStyleSheet("background-color: white")
            self.FundingTextEdit.setStyleSheet("background-color: white")
            self.AccomTextEdit.setStyleSheet("background-color: white")
            self.ColourComboBox.setStyleSheet("background-color: white")
            self.UniComboBox.setStyleSheet("background-color: white")
            self.countryComboBox.setStyleSheet("background-color: white")
            self.Student1TextEdit.setStyleSheet("background-color: white")
            self.Student2TextEdit.setStyleSheet("background-color: white")
            self.Student3TextEdit.setStyleSheet("background-color: white")

        elif text == "Red":
            self.ColourComboBox.setStyleSheet("background-color:white")
            self.centralwidget.setStyleSheet("background-color:#ff7a7a ")
            self.CountryTextEdit.setStyleSheet("background-color: white")
            self.UniTextEdit.setStyleSheet("background-color: white")
            self.FundingTextEdit.setStyleSheet("background-color: white")
            self.AccomTextEdit.setStyleSheet("background-color: white")
            self.ColourComboBox.setStyleSheet("background-color: white")
            self.UniComboBox.setStyleSheet("background-color: white")
            self.countryComboBox.setStyleSheet("background-color: white")
            self.Student1TextEdit.setStyleSheet("background-color: white")
            self.Student2TextEdit.setStyleSheet("background-color: white")
            self.Student3TextEdit.setStyleSheet("background-color: white")

        else:
            self.ColourComboBox.clear()

#Zoom Code
    def zoomie(self, state):
        if state == QtCore.Qt.Checked:
            # self.setGeometry(10, 20, 2000, 2000)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Iskoola Pota"))
            font.setPointSize(28)
            self.AviateNEducate_Title.setFont(font)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Verdana"))
            font.setPointSize(13)
            self.centralwidget.setFont(font)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Verdana"))
            font.setPointSize(15)
            self.AccomInfo.setFont(font)
            self.CountryLabel.setFont(font)
            self.ColourSelectLabel.setFont(font)
            font.setPointSize(15)
            self.Zoom.setFont(font)
            self.UniInfo.setFont(font)
            self.Funding.setFont(font)
            self.ColourSelectLabel_2.setFont(font)
            self.UniversityPicLabel.setFont(font)
            font.setPointSize(12)
            self.LCostRadioButton.setFont(font)
            self.HCostRadioButton.setFont(font)
            font.setPointSize(15)
            self.Student2PicLabel.setFont(font)
            self.Student3PicLabel.setFont(font)
        else:
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Rockwell"))
            font.setPointSize(28)
            self.AviateNEducate_Title.setFont(font)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Verdana"))
            font.setPointSize(13)
            self.centralwidget.setFont(font)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Verdana"))
            font.setPointSize(15)
            self.AccomInfo.setFont(font)
            self.CountryLabel.setFont(font)
            self.ColourSelectLabel.setFont(font)
            font.setPointSize(11)
            self.Zoom.setFont(font)
            self.UniInfo.setFont(font)
            self.Funding.setFont(font)
            self.ColourSelectLabel_2.setFont(font)
            self.UniversityPicLabel.setFont(font)
            font.setPointSize(10)
            self.LCostRadioButton.setFont(font)
            self.HCostRadioButton.setFont(font)
            font.setPointSize(15)
            self.Student2PicLabel.setFont(font)
            self.Student3PicLabel.setFont(font)

#This section displays the different university options
    def accom(self,text):
        if text == "Dublin Institute of Technology":
            self.UniTextEdit.clear()
            self.UniTextEdit.insertPlainText(_("The Dublin Institute of Technology is class"))
        elif text == "Dublin City University":
            self.UniTextEdit.clear()
            self.UniTextEdit.insertPlainText(_("The Dublin City University YAS"))
        elif text == "University College Dublin":
            self.UniTextEdit.clear()
            self.UniTextEdit.insertPlainText(_("The University College Dublin HMMM"))
        elif text == "Hochschule Darmstadt":
            self.UniTextEdit.clear()
            self.UniTextEdit.insertPlainText(_("Hochschule Darmstadt GERMAYN"))
        elif text == "Freie Universität Berlin":
            self.UniTextEdit.clear()
            self.UniTextEdit.insertPlainText(_("Freie Universität Berlin YUP"))
        elif text == "Universität zu KölnNetworking":
            self.UniTextEdit.clear()
            self.UniTextEdit.insertPlainText(_("Universität zu KölnNetworking"))
        elif text == "University of Paris":
            self.UniTextEdit.clear()
            self.UniTextEdit.insertPlainText(_("University of Paris"))
        elif text == "University of Lyon":
            self.UniTextEdit.clear()
            self.UniTextEdit.insertPlainText(_("University of Lyon"))
        elif text == "University of Marseille":
            self.UniTextEdit.clear()
            self.UniTextEdit.insertPlainText(_("University of Marseille"))

    def costs(self, text):

        if text == "Dublin Institute of Technology":
                self.HCostRadioButton.toggled.connect(self.highdub)
                self.LCostRadioButton.toggled.connect(self.lowdub)
        elif text == "Dublin City University":
                self.HCostRadioButton.toggled.connect(self.highdub)
                self.LCostRadioButton.toggled.connect(self.lowdub)
        elif text == "University College Dublin":
                self.HCostRadioButton.toggled.connect(self.highdub)
                self.LCostRadioButton.toggled.connect(self.lowdub)
        elif text == "Hochschule Darmstadt":
                self.HCostRadioButton.toggled.connect(self.highhoch)
                self.LCostRadioButton.toggled.connect(self.lowhoch)
        elif text == "Freie Universität Berlin":
                self.HCostRadioButton.toggled.connect(self.highber)
                self.LCostRadioButton.toggled.connect(self.lowber)
        elif text == "Universität zu KölnNetworking":
                self.HCostRadioButton.toggled.connect(self.highkol)
                self.LCostRadioButton.toggled.connect(self.lowkol)
        elif text == "University of Paris":
                self.HCostRadioButton.toggled.connect(self.highpar)
                self.LCostRadioButton.toggled.connect(self.lowpar)
        elif text == "University of Lyon":
                self.HCostRadioButton.toggled.connect(self.highly)
                self.LCostRadioButton.toggled.connect(self.lowly)
        elif text == "University of Marseille":
                self.HCostRadioButton.toggled.connect(self.highmar)
                self.LCostRadioButton.toggled.connect(self.lowmar)



    def lowmar(self):
        self.AccomTextEdit.clear()
        self.HCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("Le petit prince,45 per night")

    def highmar(self):
        self.AccomTextEdit.clear()
        self.LCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("La Rein, 10 per night")

    def lowly(self):
        self.AccomTextEdit.clear()
        self.HCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("L'hotel de Lafyette, 25 per night")

    def highly(self):
        self.AccomTextEdit.clear()
        self.LCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("La poisson, 10k per night")

    def lowpar(self):
        self.AccomTextEdit.clear()
        self.HCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("La Croissant, 25k per night")

    def highpar(self):
        self.AccomTextEdit.clear()
        self.LCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("Les Miserables, 10 per night")

    def highkol(self):
        self.AccomTextEdit.clear()
        self.LCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("Das Auto, 25k per night")

    def lowbkol(self):
        self.AccomTextEdit.clear()
        self.HCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("Das Hund, like 5 euro")

    def highber(self):
        self.AccomTextEdit.clear()
        self.LCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("Das Brot, 20k per night")


    def lowber(self):
        self.AccomTextEdit.clear()
        self.HCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("Das Marmelade, like 5 euro")

    def highhoch(self):
        self.AccomTextEdit.clear()
        self.LCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("Das Geld, 15k per night")

    def lowhoch(self):
        self.AccomTextEdit.clear()
        self.HCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("Das Kase, like 5 euro")

    def highdub(self):
        self.AccomTextEdit.clear()
        self.LCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("Shelbourne, 15k per night")

    def lowdub(self):

        self.AccomTextEdit.clear()
        self.HCostRadioButton.setChecked(False)
        self.AccomTextEdit.insertPlainText("Super cheap hotel, like 5 euro")

    def home(self):

        self.countryComboBox.activated[str].connect(self.loadmodules)
        self.UniComboBox.activated[str].connect(self.loaduni)
        #self.countryComboBox.activated[str].connect(self.loadpictures)
        self.ColourComboBox.activated[str].connect(self.loadcolours)
        self.UniComboBox.activated[str].connect(self.dispmodule)
        self.Zoom.stateChanged.connect(self.zoomie)
        self.UniComboBox.activated[str].connect(self.costs)
        self.UniComboBox.activated[str].connect(self.accom)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_AviateNEducate()
    ui.setupUi(MainWindow)
    ui.home()
    MainWindow.setWindowIcon(QtGui.QIcon('planeicon.png'))
    MainWindow.show()
    app.exec_()