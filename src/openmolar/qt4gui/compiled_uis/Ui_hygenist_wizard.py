# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hygenist_wizard.ui'
#
# Created: Thu Nov 19 21:47:06 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(266, 450)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.sp_radioButton = QtGui.QRadioButton(Dialog)
        self.sp_radioButton.setChecked(True)
        self.sp_radioButton.setObjectName("sp_radioButton")
        self.gridLayout.addWidget(self.sp_radioButton, 1, 0, 1, 2)
        self.extsp_radioButton = QtGui.QRadioButton(Dialog)
        self.extsp_radioButton.setChecked(False)
        self.extsp_radioButton.setObjectName("extsp_radioButton")
        self.gridLayout.addWidget(self.extsp_radioButton, 2, 0, 1, 2)
        self.twovisit1_radioButton = QtGui.QRadioButton(Dialog)
        self.twovisit1_radioButton.setEnabled(False)
        self.twovisit1_radioButton.setObjectName("twovisit1_radioButton")
        self.gridLayout.addWidget(self.twovisit1_radioButton, 3, 0, 1, 2)
        self.twovisit2_radioButton = QtGui.QRadioButton(Dialog)
        self.twovisit2_radioButton.setEnabled(False)
        self.twovisit2_radioButton.setObjectName("twovisit2_radioButton")
        self.gridLayout.addWidget(self.twovisit2_radioButton, 4, 0, 1, 2)
        self.label_2 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.dents_comboBox = QtGui.QComboBox(Dialog)
        self.dents_comboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.dents_comboBox.setFont(font)
        self.dents_comboBox.setObjectName("dents_comboBox")
        self.gridLayout.addWidget(self.dents_comboBox, 5, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.fee_doubleSpinBox = QtGui.QDoubleSpinBox(Dialog)
        self.fee_doubleSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fee_doubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fee_doubleSpinBox.setObjectName("fee_doubleSpinBox")
        self.gridLayout.addWidget(self.fee_doubleSpinBox, 6, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.ptFee_doubleSpinBox = QtGui.QDoubleSpinBox(Dialog)
        self.ptFee_doubleSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.ptFee_doubleSpinBox.setFont(font)
        self.ptFee_doubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ptFee_doubleSpinBox.setObjectName("ptFee_doubleSpinBox")
        self.gridLayout.addWidget(self.ptFee_doubleSpinBox, 7, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 51, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 2)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 9, 0, 1, 2)
        self.label_5 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 10, 0, 1, 2)
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 11, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 29, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 12, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 13, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_( u"Hygenist Wizard"))
        self.label.setText(_( u"Type"))
        self.sp_radioButton.setText(_( u"Scale and Polish"))
        self.extsp_radioButton.setText(_( u"Extensive Scaling"))
        self.twovisit1_radioButton.setText(_( u"Part 1 of 2 visit treatment"))
        self.twovisit2_radioButton.setText(_( u"Part 2 of 2 visit treatment"))
        self.label_2.setText(_( u"Dentist/Hygenist"))
        self.label_4.setText(_( u"Standard Fee"))
        self.label_3.setText(_( u"Charge to Patient"))
        self.label_5.setText(_( u"Notes"))
        self.checkBox.setText(_( u"OHI given"))

