# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newUiForFinalProject.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import socket
import sys
import results_pb2

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
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 479, 251, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.searchButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MV Boli"))
        font.setBold(True)
        font.setWeight(75)
        self.searchButton.setFont(font)
        self.searchButton.setAutoDefault(False)
        self.searchButton.setDefault(False)
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.horizontalLayout.addWidget(self.searchButton)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 300, 41))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelMust = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelMust.setObjectName(_fromUtf8("labelMust"))
        self.verticalLayout.addWidget(self.labelMust)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 139, 251, 60))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.must = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.must.setObjectName(_fromUtf8("must"))
        self.verticalLayout_2.addWidget(self.must)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 220, 300, 41))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelNot = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.labelNot.setObjectName(_fromUtf8("labelNot"))
        self.verticalLayout_3.addWidget(self.labelNot)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 260, 251, 60))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.notWord = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.notWord.setObjectName(_fromUtf8("not"))
        self.verticalLayout_4.addWidget(self.notWord)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 340, 300, 41))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lableMaybe = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.lableMaybe.setObjectName(_fromUtf8("lableMaybe"))
        self.verticalLayout_5.addWidget(self.lableMaybe)
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(9, 379, 251, 60))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.maybe = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.maybe.setObjectName(_fromUtf8("maybe"))
        self.verticalLayout_6.addWidget(self.maybe)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(273, 80, 41, 461))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 10, 750, 68))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.lableNameOfProgram = QtGui.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Narkisim"))
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.lableNameOfProgram.setFont(font)
        self.lableNameOfProgram.setObjectName(_fromUtf8("lableNameOfProgram"))
        self.verticalLayout_7.addWidget(self.lableNameOfProgram)
        self.resultBox = QtGui.QTextEdit(self.centralwidget)
        self.resultBox.setGeometry(QtCore.QRect(320, 96, 461, 441))
        self.resultBox.setObjectName(_fromUtf8("resultBox"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.search)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.searchButton.setText(_translate("MainWindow", "SEARCH", None))
        self.labelMust.setText(_translate("MainWindow", "Enter your word(s) that is in your search :", None))
        self.labelNot.setText(_translate("MainWindow", "Enter your word(s) that not in your search :", None))
        self.lableMaybe.setText(_translate("MainWindow", "Enter word(s) that maybe is in your search :", None))
        self.lableNameOfProgram.setText(_translate("MainWindow", "The Three Musketeers Search Engine ", None))

    def search(self):

        import sample_pb2
        s = socket.socket()
        s.connect(("localhost",9999))

        #self.webView.load(QUrl('copy.html'))
        must=str(self.must.text()).rsplit()
        one_must=str(self.notWord.text()).rsplit()
        must_not=str(self.maybe.text()).rsplit()
        #from indexing import setter
        #setter(must,must_not,one_must)
        data = sample_pb2.Data()
        for item in must :
            mb = data.mustbe.add()
            mb.mustbe = item
        for item in must_not :
            mb = data.mustnotbe.add()
            mb.mustnotbe = item
        for item in one_must :
            mb = data.onlybe.add() #repeated
            mb.onlybe = item #string
        res = data.SerializeToString()
        print res
        s.send(res)
        finalRes = s.recv(100000)

        final_links = results_pb2.Data()

        final_links.ParseFromString(finalRes)
        links = []

        for item in final_links.repeatLinks:
            links.append(item.containLinks)

        print links
        for item in links:
            self.resultBox.setText(item + '/n')

        s.close()



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

