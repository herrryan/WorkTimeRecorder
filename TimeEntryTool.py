# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TimeEntryTool.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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

class Ui_baseWindow(object):
    def setupUi(self, baseWindow):
        baseWindow.setObjectName(_fromUtf8("baseWindow"))
        baseWindow.resize(763, 482)
        baseWindow.setAutoFillBackground(True)
        self.buttonBox = QtGui.QDialogButtonBox(baseWindow)
        self.buttonBox.setGeometry(QtCore.QRect(360, 420, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayoutWidget_2 = QtGui.QWidget(baseWindow)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(70, 80, 521, 80))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout.addWidget(self.dateEdit, 1, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout.addWidget(self.doubleSpinBox, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.commandLinkButton = QtGui.QCommandLinkButton(baseWindow)
        self.commandLinkButton.setGeometry(QtCore.QRect(40, 380, 231, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.pushButton = QtGui.QPushButton(baseWindow)
        self.pushButton.setGeometry(QtCore.QRect(610, 140, 101, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(baseWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), baseWindow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), baseWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(baseWindow)

    def retranslateUi(self, baseWindow):
        baseWindow.setWindowTitle(_translate("baseWindow", "Time Entry Tool for WOKO", None))
        self.comboBox.setItemText(0, _translate("baseWindow", "M62", None))
        self.comboBox.setItemText(1, _translate("baseWindow", "Housing Office", None))
        self.comboBox.setItemText(2, _translate("baseWindow", "Others", None))
        self.label.setText(_translate("baseWindow", "Date", None))
        self.label_2.setText(_translate("baseWindow", "Time (h)", None))
        self.label_3.setText(_translate("baseWindow", "Task", None))
        self.label_4.setText(_translate("baseWindow", "For Whom?", None))
        self.commandLinkButton.setText(_translate("baseWindow", "Export to WOKO Excel", None))
        self.pushButton.setText(_translate("baseWindow", "+ New Time Entry", None))

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QDialog()
window = Ui_baseWindow()
window.setupUi(MainWindow)
MainWindow.show()

sys.exit(app.exec_())