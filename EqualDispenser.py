from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pandas as pd
import numpy as np
import os

dosyalar = ''

def ebob_bul(self):
  for i in reversed(range(1, max(self))):
        if sum([j % i for j in self]) == 0:
            return i
            break
def sefas_dataset(liste,ksad,ksad2):
  ishowspeed = list(np.zeros(len(liste)))
  ishow = []
  for fsdgsd in ishowspeed:
    ishow.append(int(fsdgsd))
  ds = []
  c = pd.read_csv(liste[0]).columns
  for sa in c:
    ds.append(sa)
  ds = ds[1:]
  dfts = pd.DataFrame(columns=ds)
  dft = pd.DataFrame(columns=ds)
  lenght_liste = len(liste)
  kck = []
  for lk in liste:
    df = pd.read_csv(lk)
    dfl = len(df)
    l = str(dfl)[-1:]
    if int(l) == 5:
      pass
    elif int(l) > 5 and int(l) != 0:
      sa = int(l)-5
      df= df[-sa:]
      frames = [dfts,df]
      dfts = pd.concat(frames)
      dfl = dfl-sa
    elif int(l) < 5 and int(l) != 0:
      sax = int(l)
      dfl = dfl-sax
      df = df[-sax:]
      frames = [dfts,df]
      dfts = pd.concat(frames)
    elif int(l) == 0:
      pass
    kck.append(dfl)
  l = []
  ebob = ebob_bul(kck)
  b=[]
  for i in kck:
    b.append(int(i/ebob))
  for ic in range(ebob):
    for ix in range(len(b)):
      for c in range(1,b[ix]+1):
        ks = pd.read_csv(liste[ix])
        dsx = []
        for dsas in ks.iloc[ishow[ix]]:
          dsx.append(dsas)
        dsx = dsx[1:]
        dft.loc[len(dft)] = dsx
        ishow[ix] = ishow[ix] + 1
  dfts = dfts[ds]
  dft.to_csv(ksad)
  dfts.to_csv(ksad2)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 375)
        MainWindow.setMinimumSize(QtCore.QSize(625, 375))
        MainWindow.setMaximumSize(QtCore.QSize(625, 375))
        MainWindow.setStyleSheet("")
        self.a1 = QtWidgets.QWidget(MainWindow)
        self.a1.setObjectName("a1")
        self.a2 = QtWidgets.QFrame(self.a1)
        self.a2.setGeometry(QtCore.QRect(0, 0, 631, 81))
        self.a2.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.a2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.a2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.a2.setObjectName("a2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.a2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(353, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.a5 = QtWidgets.QLabel(self.a2)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(18)
        self.a5.setFont(font)
        self.a5.setStyleSheet("color: rgb(255, 255, 255);")
        self.a5.setObjectName("a5")
        self.horizontalLayout.addWidget(self.a5)
        spacerItem1 = QtWidgets.QSpacerItem(353, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.a6 = QtWidgets.QLabel(self.a2)
        self.a6.setStyleSheet("color: rgb(255, 255, 255);")
        self.a6.setObjectName("a6")
        self.horizontalLayout.addWidget(self.a6)
        self.a7 = QtWidgets.QFrame(self.a1)
        self.a7.setGeometry(QtCore.QRect(10, 90, 611, 291))
        self.a7.setMinimumSize(QtCore.QSize(0, 0))
        self.a7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.a7.setStyleSheet("")
        self.a7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.a7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.a7.setObjectName("a7")
        self.a8 = QtWidgets.QFrame(self.a7)
        self.a8.setGeometry(QtCore.QRect(400, 10, 191, 181))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.a8.setFont(font)
        self.a8.setStyleSheet("background-color:white;\n"
"color:black;")
        self.a8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.a8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.a8.setObjectName("a8")
        self.a11 = QtWidgets.QLabel(self.a8)
        self.a11.setGeometry(QtCore.QRect(30, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.a11.setFont(font)
        self.a11.setStyleSheet("")
        self.a11.setText("")
        self.a11.setObjectName("a11")
        self.a12 = QtWidgets.QLabel(self.a8)
        self.a12.setGeometry(QtCore.QRect(30, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.a12.setFont(font)
        self.a12.setObjectName("a12")
        self.a12_2 = QtWidgets.QLabel(self.a8)
        self.a12_2.setGeometry(QtCore.QRect(30, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.a12_2.setFont(font)
        self.a12_2.setObjectName("a12_2")
        self.a11_3 = QtWidgets.QLabel(self.a8)
        self.a11_3.setGeometry(QtCore.QRect(30, 130, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.a11_3.setFont(font)
        self.a11_3.setStyleSheet("")
        self.a11_3.setText("")
        self.a11_3.setObjectName("a11_3")
        self.a8_2 = QtWidgets.QFrame(self.a7)
        self.a8_2.setGeometry(QtCore.QRect(20, 10, 371, 251))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.a8_2.setFont(font)
        self.a8_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;")
        self.a8_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.a8_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.a8_2.setObjectName("a8_2")
        self.a13_2 = QtWidgets.QLineEdit(self.a8_2)
        self.a13_2.setGeometry(QtCore.QRect(30, 50, 211, 31))
        self.a13_2.setStyleSheet("border:1px solid ;")
        self.a13_2.setFrame(False)
        self.a13_2.setObjectName("a13_2")
        self.a9_2 = QtWidgets.QLabel(self.a8_2)
        self.a9_2.setGeometry(QtCore.QRect(30, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.a9_2.setFont(font)
        self.a9_2.setObjectName("a9_2")
        self.a11_2 = QtWidgets.QLabel(self.a8_2)
        self.a11_2.setGeometry(QtCore.QRect(620, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.a11_2.setFont(font)
        self.a11_2.setStyleSheet("")
        self.a11_2.setText("")
        self.a11_2.setObjectName("a11_2")
        self.a10 = QtWidgets.QLabel(self.a8_2)
        self.a10.setGeometry(QtCore.QRect(30, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.a10.setFont(font)
        self.a10.setObjectName("a10")
        self.a14_3 = QtWidgets.QLineEdit(self.a8_2)
        self.a14_3.setGeometry(QtCore.QRect(30, 130, 151, 31))
        self.a14_3.setStyleSheet("border:1px solid black;")
        self.a14_3.setFrame(False)
        self.a14_3.setObjectName("a14_3")
        self.a14_2 = QtWidgets.QLineEdit(self.a8_2)
        self.a14_2.setGeometry(QtCore.QRect(200, 130, 151, 31))
        self.a14_2.setStyleSheet("border:1px solid black;")
        self.a14_2.setFrame(True)
        self.a14_2.setObjectName("a14_2")
        self.a10_2 = QtWidgets.QLabel(self.a8_2)
        self.a10_2.setGeometry(QtCore.QRect(200, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.a10_2.setFont(font)
        self.a10_2.setObjectName("a10_2")
        self.a15_2 = QtWidgets.QPushButton(self.a8_2)
        self.a15_2.setGeometry(QtCore.QRect(250, 50, 101, 31))
        self.a15_2.setStyleSheet("border:1px solid black;")
        self.a15_2.setAutoDefault(False)
        self.a15_2.setDefault(False)
        self.a15_2.setFlat(True)
        self.a15_2.setObjectName("a15_2")
        self.a15_2.clicked.connect(self.getfiles)
        self.a15 = QtWidgets.QPushButton(self.a8_2)
        self.a15.setGeometry(QtCore.QRect(30, 190, 321, 31))
        self.a15.setStyleSheet("border:1px solid black;")
        self.a15.setAutoDefault(False)
        self.a15.setDefault(False)
        self.a15.setFlat(False)
        self.a15.setObjectName("a15")
        self.frame = QtWidgets.QFrame(self.a7)
        self.frame.setGeometry(QtCore.QRect(400, 200, 191, 61))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.a15_3 = QtWidgets.QPushButton(self.frame)
        self.a15_3.setGeometry(QtCore.QRect(30, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.a15_3.setFont(font)
        self.a15_3.setStyleSheet("color:blue;")
        self.a15_3.setAutoDefault(False)
        self.a15_3.setDefault(False)
        self.a15_3.setFlat(True)
        self.a15_3.setObjectName("a15_3")
        MainWindow.setCentralWidget(self.a1)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getfiles(self):
      global dosyalar
      dlg = QFileDialog()
      if dlg.exec_():
        filenames = dlg.selectedFiles()
        for i in filenames:
          if self.a13_2.text() == '':
            dosyalar +=i
          else:
            ksds = ','+i
            dosyalar += ksds
        self.a13_2.setText(dosyalar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EqualDispenser"))
        self.a5.setText(_translate("MainWindow", "EqualDispenser"))
        self.a6.setText(_translate("MainWindow", "By @cyberm0n"))
        self.a12.setText(_translate("MainWindow", "Çıktılar"))
        self.a12_2.setText(_translate("MainWindow", "Ekstralar"))
        self.a9_2.setText(_translate("MainWindow", "Dosya Adları"))
        self.a10.setText(_translate("MainWindow", "Çıktı"))
        self.a10_2.setText(_translate("MainWindow", "Ekstra"))
        self.a15_2.setText(_translate("MainWindow", "Seç"))
        self.a15_2.setShortcut(_translate("MainWindow", "Return"))
        self.a15.setText(_translate("MainWindow", "Tamamla"))
        self.a15.setShortcut(_translate("MainWindow", "Return"))
        self.a15_3.setText(_translate("MainWindow", "Kılavuz"))
        self.a15_3.setShortcut(_translate("MainWindow", "Return"))

def go():
  os.system("start https://github.com/cyberm0n/equaldispenser")

def e():
    absd=ui.a13_2.text().strip().split(',')
    absk=ui.a14_3.text().strip()
    abls= ui.a14_2.text().strip()
    ui.a13_2.setText('')
    ui.a14_3.setText('')
    ui.a14_2.setText('')
    sefas_dataset(absd,absk,abls)
    ui.a11.setText(absk)
    ui.a11_3.setText(abls)

Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()
ui.a15.clicked.connect(e)
ui.a15_3.clicked.connect(go)

sys.exit(Uygulama.exec_())
