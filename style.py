# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'style.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 550)
        Form.setMinimumSize(QtCore.QSize(300, 360))
        Form.setMaximumSize(QtCore.QSize(300, 550))
        self.send_block = QtWidgets.QLineEdit(Form)
        self.send_block.setGeometry(QtCore.QRect(30, 460, 241, 71))
        self.send_block.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.send_block.setObjectName("send_block")
        self.recv_block = QtWidgets.QTextBrowser(Form)
        self.recv_block.setGeometry(QtCore.QRect(30, 21, 241, 421))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.recv_block.setFont(font)
        self.recv_block.setObjectName("recv_block")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.recv_block.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
