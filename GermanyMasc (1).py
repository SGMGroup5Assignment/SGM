# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GermanyMasc.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#import getext




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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(978, 910)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.TitleLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.TitleLayout.setObjectName(_fromUtf8("TitleLayout"))
        self.TitleLabel = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rockwell"))
        font.setPointSize(24)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName(_fromUtf8("TitleLabel"))
        self.TitleLayout.addWidget(self.TitleLabel)
        
        #English Radio Button
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(580, 10, 191, 111))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.EnglishBtnLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.EnglishBtnLayout.setObjectName(_fromUtf8("EnglishBtnLayout"))
        self.EnglishBtn = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(11)
        self.EnglishBtn.setFont(font)
        self.EnglishBtn.setObjectName(_fromUtf8("EnglishBtn"))
        self.EnglishBtnLayout.addWidget(self.EnglishBtn)
        
        #German Radio Button
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(770, 10, 191, 111))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.GermanBtnLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.GermanBtnLayout.setObjectName(_fromUtf8("GermanBtnLayout"))
        self.GermanBtn = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(11)
        self.GermanBtn.setFont(font)
        self.GermanBtn.setObjectName(_fromUtf8("GermanBtn"))
        self.GermanBtnLayout.addWidget(self.GermanBtn)
        
        #Zoom Button Box
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(380, 10, 161, 111))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.ZoomLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.ZoomLayout.setObjectName(_fromUtf8("ZoomLayout"))
        self.ZoomBox = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(11)
        self.ZoomBox.setFont(font)
        self.ZoomBox.setObjectName(_fromUtf8("ZoomBox"))
        self.ZoomLayout.addWidget(self.ZoomBox)
        
        #Country Layout
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 140, 461, 81))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.CountryInfoLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.CountryInfoLayout.setObjectName(_fromUtf8("CountryInfoLayout"))
        #Country Title
        self.CountryInfoLabel = QtGui.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CountryInfoLabel.setFont(font)
        self.CountryInfoLabel.setObjectName(_fromUtf8("CountryInfoLabel"))
        self.CountryInfoLayout.addWidget(self.CountryInfoLabel)
        
        #Uni Info Layout
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(500, 140, 461, 81))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.UniInfoLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.UniInfoLayout.setObjectName(_fromUtf8("UniInfoLayout"))
        #Uni Label
        self.UniInfoLabel = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UniInfoLabel.setFont(font)
        self.UniInfoLabel.setObjectName(_fromUtf8("UniInfoLabel"))
        self.UniInfoLayout.addWidget(self.UniInfoLabel)
        
        #Country Pic
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 230, 161, 161))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.CountryPicLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.CountryPicLayout.setObjectName(_fromUtf8("CountryPicLayout"))
        self.CountryPicLabel = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.CountryPicLabel.setObjectName(_fromUtf8("CountryPicLabel"))
        self.CountryPicLayout.addWidget(self.CountryPicLabel)
        self.CountryPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("GermanyMain.jpg")))
        self.CountryPicLabel.setObjectName(_fromUtf8("Germany"))
        
        #Uni Pic
        self.verticalLayoutWidget_8 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(800, 230, 161, 161))
        self.verticalLayoutWidget_8.setObjectName(_fromUtf8("verticalLayoutWidget_8"))
        self.UniPicLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_8)
        self.UniPicLayout.setObjectName(_fromUtf8("UniPicLayout"))
        self.UniPicLabel = QtGui.QLabel(self.verticalLayoutWidget_8)
        self.UniPicLabel.setObjectName(_fromUtf8("UniPicLabel"))
        self.UniPicLayout.addWidget(self.UniPicLabel)
        self.UniPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Darmstadt.jpg")))
        self.UniPicLabel.setObjectName(_fromUtf8("Darmstadt"))
        
        #Country Text Layout
        self.verticalLayoutWidget_9 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(180, 230, 291, 161))
        self.verticalLayoutWidget_9.setObjectName(_fromUtf8("verticalLayoutWidget_9"))
        self.CountryTextLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_9)
        self.CountryTextLayout.setObjectName(_fromUtf8("CountryTextLayout"))
        #Country Text
        self.CountryTextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget_9)
        self.CountryTextEdit.setObjectName(_fromUtf8("CountryTextEdit"))
        self.CountryTextLayout.addWidget(self.CountryTextEdit)
        self.verticalLayoutWidget_10 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(500, 230, 291, 161))
        self.verticalLayoutWidget_10.setObjectName(_fromUtf8("verticalLayoutWidget_10"))
        self.UniTextLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_10)
        self.UniTextLayout.setObjectName(_fromUtf8("UniTextLayout"))
        self.UniTextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget_10)
        self.UniTextEdit.setObjectName(_fromUtf8("UniTextEdit"))
        self.UniTextLayout.addWidget(self.UniTextEdit)
        
        #Accom Title Layout
        self.verticalLayoutWidget_11 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(10, 400, 461, 80))
        self.verticalLayoutWidget_11.setObjectName(_fromUtf8("verticalLayoutWidget_11"))
        self.AccomTitleLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_11)
        self.AccomTitleLayout.setObjectName(_fromUtf8("AccomTitleLayout"))
        #Accom Title Label
        self.AccomTitleLabel = QtGui.QLabel(self.verticalLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AccomTitleLabel.setFont(font)
        self.AccomTitleLabel.setObjectName(_fromUtf8("AccomTitleLabel"))
        self.AccomTitleLayout.addWidget(self.AccomTitleLabel)
        
        # Funding Title Layout
        self.verticalLayoutWidget_12 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(500, 400, 461, 81))
        self.verticalLayoutWidget_12.setObjectName(_fromUtf8("verticalLayoutWidget_12"))
        self.FundingTitleLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_12)
        self.FundingTitleLayout.setObjectName(_fromUtf8("FundingTitleLayout"))
        
        #Funding Title Label
        self.FundingTitleLabel = QtGui.QLabel(self.verticalLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FundingTitleLabel.setFont(font)
        self.FundingTitleLabel.setObjectName(_fromUtf8("FundingTitleLabel"))
        self.FundingTitleLayout.addWidget(self.FundingTitleLabel)
        
        #Accom text layout
        self.verticalLayoutWidget_13 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(10, 490, 461, 141))
        self.verticalLayoutWidget_13.setObjectName(_fromUtf8("verticalLayoutWidget_13"))
        self.AccomTextLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_13)
        self.AccomTextLayout.setObjectName(_fromUtf8("AccomTextLayout"))
        self.AccomTextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget_13)
        self.AccomTextEdit.setObjectName(_fromUtf8("AccomTextEdit"))
        self.AccomTextLayout.addWidget(self.AccomTextEdit)
        
        #Funding text layout
        self.verticalLayoutWidget_14 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(500, 490, 461, 141))
        self.verticalLayoutWidget_14.setObjectName(_fromUtf8("verticalLayoutWidget_14"))
        self.FundingTextLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_14)
        self.FundingTextLayout.setObjectName(_fromUtf8("FundingTextLayout"))
        #Text Edit
        self.FundingTextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget_14)
        self.FundingTextEdit.setObjectName(_fromUtf8("FundingTextEdit"))
        self.FundingTextLayout.addWidget(self.FundingTextEdit)
        
        #Student Title Layout
        self.verticalLayoutWidget_15 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(10, 640, 951, 80))
        self.verticalLayoutWidget_15.setObjectName(_fromUtf8("verticalLayoutWidget_15"))
        self.StudentTitleLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_15)
        self.StudentTitleLayout.setObjectName(_fromUtf8("StudentTitleLayout"))
        #Student title label
        self.StudentTitleLabel = QtGui.QLabel(self.verticalLayoutWidget_15)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.StudentTitleLabel.setFont(font)
        self.StudentTitleLabel.setObjectName(_fromUtf8("StudentTitleLabel"))
        self.StudentTitleLayout.addWidget(self.StudentTitleLabel)
        
        #Student One Layout
        self.verticalLayoutWidget_16 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_16.setGeometry(QtCore.QRect(20, 730, 301, 121))
        self.verticalLayoutWidget_16.setObjectName(_fromUtf8("verticalLayoutWidget_16"))
        self.Student1TextLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_16)
        self.Student1TextLayout.setObjectName(_fromUtf8("Student1TextLayout"))
        #Student One Text
        self.Student1TextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget_16)
        self.Student1TextEdit.setObjectName(_fromUtf8("Student1TextEdit"))
        self.Student1TextLayout.addWidget(self.Student1TextEdit)
        
        #Student Two Layout
        self.verticalLayoutWidget_17 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_17.setGeometry(QtCore.QRect(340, 730, 301, 121))
        self.verticalLayoutWidget_17.setObjectName(_fromUtf8("verticalLayoutWidget_17"))
        self.Student2TextLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_17)
        self.Student2TextLayout.setObjectName(_fromUtf8("Student2TextLayout"))
        #Student Two Text
        self.Student2TextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget_17)
        self.Student2TextEdit.setObjectName(_fromUtf8("Student2TextEdit"))
        self.Student2TextLayout.addWidget(self.Student2TextEdit)
        
        #Student Three Layout
        self.verticalLayoutWidget_18 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_18.setGeometry(QtCore.QRect(660, 730, 291, 121))
        self.verticalLayoutWidget_18.setObjectName(_fromUtf8("verticalLayoutWidget_18"))
        self.Student3TextLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_18)
        self.Student3TextLayout.setObjectName(_fromUtf8("Student3TextLayout"))
        #Student Three Label
        self.Student3TextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget_18)
        self.Student3TextEdit.setObjectName(_fromUtf8("Student3TextEdit"))
        self.Student3TextLayout.addWidget(self.Student3TextEdit)
        
        #Main Window
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.TitleLabel.setText(_translate("MainWindow", "AviateNEducate", None))
        self.EnglishBtn.setText(_translate("MainWindow", "English", None))
        self.GermanBtn.setText(_translate("MainWindow", "Deutsch", None))
        self.ZoomBox.setText(_translate("MainWindow", "Enlarge Window", None))
        self.CountryInfoLabel.setText(_translate("MainWindow", "Information on the Germany", None))
        self.UniInfoLabel.setText(_translate("MainWindow", "University of Darmstadt", None))
        self.CountryPicLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.CountryPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("GermanyMain.jpg")))
        self.CountryPicLabel.setObjectName(_fromUtf8("Germany"))
        self.UniPicLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.UniPicLabel.setPixmap(QtGui.QPixmap(_fromUtf8("Darmstadt.jpg")))
        self.UniPicLabel.setObjectName(_fromUtf8("Darmstadt"))
        self.AccomTitleLabel.setText(_translate("MainWindow", "Accomodation", None))
        self.FundingTitleLabel.setText(_translate("MainWindow", "Funding", None))
        self.StudentTitleLabel.setText(_translate("MainWindow", "Past Student Experience", None))


# Zoom Code
    def zoomie(self, state):
        if state == QtCore.Qt.Checked:
            # self.setGeometry(10, 20, 2000, 2000)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Rockwell"))
            font.setPointSize(20)
            self.TitleLabel.setFont(font)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Verdana"))
            font.setPointSize(10)
            self.centralwidget.setFont(font)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Verdana"))
            font.setPointSize(12)
            self.EnglishBtn.setFont(font)
            self.GermanBtn.setFont(font)
            self.ZoomBox.setFont(font)
            font.setPointSize(12)
            self.CountryInfoLabel.setFont(font)
            self.CountryTextEdit.setFont(font)
            self.UniInfoLabel.setFont(font)
            self.UniTextEdit.setFont(font)
            self.AccomTitleLabel.setFont(font)
            self.AccomTextEdit.setFont(font)
            self.FundingTitleLabel.setFont(font)
            self.FundingTextEdit.setFont(font)
            self.StudentTitleLabel.setFont(font)
            self.Student1TextEdit.setFont(font)
            self.Student2TextEdit.setFont(font)
            self.Student3TextEdit.setFont(font)

        else:
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Rockwell"))
            font.setPointSize(18)
            self.TitleLabel.setFont(font)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Verdana"))
            font.setPointSize(8)
            self.centralwidget.setFont(font)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Verdana"))
            font.setPointSize(10)
            self.EnglishBtn.setFont(font)
            self.GermanBtn.setFont(font)
            self.ZoomBox.setFont(font)
            font.setPointSize(10)
            self.CountryInfoLabel.setFont(font)
            self.CountryTextEdit.setFont(font)
            self.UniInfoLabel.setFont(font)
            self.UniTextEdit.setFont(font)
            self.AccomTitleLabel.setFont(font)
            self.AccomTextEdit.setFont(font)
            self.FundingTitleLabel.setFont(font)
            self.FundingTextEdit.setFont(font)
            self.StudentTitleLabel.setFont(font)
            self.Student1TextEdit.setFont(font)
            self.Student2TextEdit.setFont(font)
            self.Student3TextEdit.setFont(font)

    def English(self):
        self.AccomTextEdit.clear()
        self.CountryTextEdit.clear()
        self.UniTextEdit.clear()
        self.FundingTextEdit.clear()
        self.Student1TextEdit.clear()
        self.Student2TextEdit.clear()
        self.Student3TextEdit.clear()
        self.GermanBtn.setChecked(False)
        self.AccomTextEdit.insertPlainText("Your college or university will have an accommodation officer or someone in student services that can advise you on getting a place. Try speaking to them first. Usually, there are notice boards all over the college campus with notices: seeking flatmates, advertising rented houses and offering lodgings. Check out the college website. Don't panic and take the first place you look at. Ask someone with experience of living in rented accommodation to come with you and to check stuff like the heating, who you're living with, how long it will take you to get to college and if the kitchen is okay for cooking. Check out the local newspapers for the area you're moving to. There are often loads of classified ads with houses or rooms to let. Make sure to get a copy of the paper as soon as it comes out, as everyone will be fighting for the best deals.")
        self.CountryTextEdit.insertPlainText("German is one of the most important cultural languages. German was spoken and written by Goethe, Mozart, Beethoven, Freud, Klimt and Einstein, and numerous other great artists and scientists.")
        self.UniTextEdit.insertPlainText("Since its foundation in 1877, TU Darmstadt has played its part in addressing the urgent issues of the future with pioneering achievements and outstanding research and teaching. TU Darmstadt focusses on selected, highly relevant problem areas. Technology is at the heart of all our disciplines at TU Darmstadt. The Natural Sciences as well as Social Sciences and Humanities cooperate closely with Engineering.")
        self.FundingTextEdit.insertPlainText("Double Degree Outgoings (Europe) have the opportunity to be promoted for their time abroad. The funding is based on the funding program of the German-French University (DFH), but the same funding is available with similar requirements for all Double Degree Outgoings in other European countries. The funding amount is € 270 per month, but is limited to 10 months per year due to its orientation to the French system. The maximum promotion period is 2 years, with shorter stays being pro rata. The academic year of the TU Darmstadt is decisive for the calculation of the funding, so that many semester stays can be funded with less than € 1,350 per semester. Further information is given to the nominated students in the form of a separate information event.")
        self.Student1TextEdit.insertPlainText("Wouldn't change a thing. Great course, great mates, great uni life and a brilliant community feel as you walk around. What more could you ask for. Uni life vs social life is a challenge, as with all uni's, but thankfully the local towns 8 pub! give you lots of choice. Social nights and SU events are well planned and inclusive. The course is above the rest with its hands on approach and helpful lectures")
        self.Student2TextEdit.insertPlainText("I have absolutely loved my uni experience so far. I have made some great friends and have learned so much about my course and it has built up confidence in myself.")
        self.Student3TextEdit.insertPlainText("As a mature student i've enjoyed it, it has certainly been interesting learning new things and changing my mind on issues. The social side has been fun, the Student Union has made sure that it has")
    
    def German(self):
        self.AccomTextEdit.clear()
        self.CountryTextEdit.clear()
        self.UniTextEdit.clear()
        self.FundingTextEdit.clear()
        self.Student1TextEdit.clear()
        self.Student2TextEdit.clear()
        self.Student3TextEdit.clear()
        self.EnglishBtn.setChecked(False)
        self.AccomTextEdit.insertPlainText("Ihr College oder Universität wird eine Unterkunft Offizier oder jemand in Studenten Dienstleistungen, die Sie beraten können, einen Platz zu bekommen. Versuchen Sie zuerst mit ihnen zu sprechen. In der Regel gibt es Anschlagtafeln auf dem ganzen College-Campus mit Notizen: sucht Mitbewohner, Werbung Mietwohnungen und bietet Unterkunft. Schauen Sie sich die College-Website. Keine Panik und nimm den ersten Platz, den du siehst. Fragen Sie jemanden mit Erfahrung des Lebens in Mietwohnungen, um mit Ihnen zu kommen und um Zeug wie die Heizung zu überprüfen, mit wem Sie leben, wie lange es dauert, bis Sie aufs College kommen und wenn die Küche für das Kochen in Ordnung ist. Schauen Sie sich die Lokalzeitungen für den Bereich an, in den Sie sich bewegen. Es gibt oft viele Kleinanzeigen mit Häusern oder Räumen zu vermieten. Achten Sie darauf, eine Kopie des Papiers zu bekommen, sobald es herauskommt, da jeder für die besten Angebote kämpft.")
        self.CountryTextEdit.insertPlainText("Deutsch ist eine der bedeutendsten Kultursprachen. Deutsch wurde von Goethe, Mozart, Beethoven, Freud, Klimt und Einstein und zahlreichen anderen großen Künstlern und Wissenschaftlern gesprochen und geschrieben.")
        self.UniTextEdit.insertPlainText("Seit ihrer Gründung im Jahre 1877 hat die TU Darmstadt ihre Rolle bei der Bewältigung der dringenden Fragen der Zukunft mit Pionierleistungen und herausragender Forschung und Lehre gespielt. Die TU Darmstadt konzentriert sich auf ausgewählte, hoch relevante Problemfelder. Technologie steht im Mittelpunkt aller Disziplinen der TU Darmstadt. Sowohl die Naturwissenschaften als auch die Sozialwissenschaften und Geisteswissenschaften arbeiten eng mit dem Ingenieurwesen zusammen.")
        self.FundingTextEdit.insertPlainText("Double Degree Outgoings (Europa) haben die Möglichkeit für ihre Zeit im Ausland gefördert zu werden. Die Förderung richtet sich nach dem Förderprogramm der Deutsch-Französischen Hochschule (DFH), jedoch ist die gleiche Förderung mit ähnlichen Anforderungen für alle Double Degree Outgoings im europäischen Ausland verfügbar. Die Förderungshöhe beträgt 270 € pro Monat, ist jedoch aufgrund der Orientierung an dem französischen System auf 10 Monate pro Jahr beschränkt. Die Förderungshöchstdauer beträgt maximal 2 Jahre wobei kürzere Aufenthalte anteilig berechnet werden. Für die Berechnung der Förderung ist das akademische Jahr der TU Darmstadt maßgeblich, sodass leider manche Semesteraufenthalte mit weniger als 1.350 € pro Semester gefördert werden können. Weitere Informationen erhalten die nominierten Studierenden in Form einer separaten Informationsveranstaltung.")
        self.Student1TextEdit.insertPlainText("Würde nichts ändern. Toller Kurs, tolle Kumpel, tolles Uni-Leben und eine brillante Community fühlen, wie Sie herumlaufen. Was willst du noch mehr? Uni Leben vs soziales Leben ist eine Herausforderung, wie bei allen Uni's, aber dankbar die lokalen Städte 8 Pub! Gib dir viel Auswahl Soziale Nächte und SU-Veranstaltungen sind gut geplant und inklusive. Der Kurs ist über den Rest mit seinen Händen auf Ansatz und hilfreiche Vorlesungen")
        self.Student2TextEdit.insertPlainText("Ich habe meine bisherige Erfahrung absolut geliebt. Ich habe einige tolle Freunde gemacht und habe so viel über meinen Kurs gelernt und es hat Vertrauen in mich aufgebaut.")
        self.Student3TextEdit.insertPlainText("Als reifer Schüler habe ich es genossen, es ist sicherlich interessant, neue Dinge zu lernen und meine Gedanken auf Probleme zu ändern. Die soziale Seite hat Spaß gemacht, die Studentenschaft hat dafür gesorgt, dass sie es hat")

    def home(self):
        self.ZoomBox.stateChanged.connect(self.zoomie)
        self.GermanBtn.toggled.connect(self.German)
        self.EnglishBtn.toggled.connect(self.English)
        #self.countryComboBox.activated[str].connect(self.loadmodules)
        #self.UniComboBox.activated[str].connect(self.loaduni)
        #self.countryComboBox.activated[str].connect(self.loadpictures)
        #self.ColourComboBox.activated[str].connect(self.loadcolours)
        #self.UniComboBox.activated[str].connect(self.dispmodule)
        #self.Zoom.stateChanged.connect(self.zoomie)
        #self.UniComboBox.activated[str].connect(self.costs)
        #self.UniComboBox.activated[str].connect(self.accom)
        #self.countryComboBox.activated[str].connect(self.country)
        #self.UniComboBox.activated[str].connect(self.funding)


if __name__ == "__main__":
    import sys
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.home()
    MainWindow.setWindowIcon(QtGui.QIcon('planeicon.png'))
    MainWindow.show()
    app.exec_()

