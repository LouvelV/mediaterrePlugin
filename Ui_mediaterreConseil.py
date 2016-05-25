# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_mediaterreConseil.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_mediaterreConseil(object):
    def setupUi(self, mediaterreConseil):
        mediaterreConseil.setObjectName("mediaterreConseil")
        mediaterreConseil.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(mediaterreConseil)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(mediaterreConseil)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), mediaterreConseil.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), mediaterreConseil.reject)
        QtCore.QMetaObject.connectSlotsByName(mediaterreConseil)

    def retranslateUi(self, mediaterreConseil):
        mediaterreConseil.setWindowTitle(QtGui.QApplication.translate("mediaterreConseil", "mediaterreConseil", None, QtGui.QApplication.UnicodeUTF8))
