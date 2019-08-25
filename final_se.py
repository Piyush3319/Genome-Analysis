# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'se.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
import re
import sys


from PyQt5 import QtCore, QtGui, QtWidgets
from valid import Ui_MainWindow   
class Ui_Dialog(object):
    def open_gene_seq_file(self):
        i = 0
        flag = 0
        count = 1
        buff = ""
        info_line = 0
        path = self.lineEdit.text()
        fp = open(path, 'r')
        nf = open("upload.txt", 'w')
        # open file and read one line at a time

        for line in fp:
            # print(line)
            i = i + 1
            # check if line is information line
            if line[0] == '>':
                # if information line is repeated
                if info_line == 1:
                    flag = 0
                    break
                buff = "\n" + str(count) + "\t"
                buff += line[1:].rstrip() + "\t"
                #nf.write(buff)
                flag = 1
                count += 1
                info_line = 1

            else:
                info_line = 0
                if bool(re.match('^[AGTC]+$', line)):
                    flag = 1
                    buff += line.rstrip()
                else:
                    flag = 0  # false
                    break
            # write data to new file
            nf.write(buff)
            del buff
            buff = ""
        fp.close()  
        nf.close()
        if flag:
            print("valid file")
            self.val= QtGui.QMainWindow()
            self.ui=Ui_MainWindow()
            self.ui.setupUi(self.val)
            self.val.show()
            
            
        else:
            print("invalid file")
        pass
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(940, 583)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:rgb(137, 206, 206)\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(0, 170, 255);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 190, 251, 21))
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"font: 75 16pt \"Calibri\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(320, 180, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 260, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_gene_seq_file)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(180, 40, 651, 91))
        self.label_4.setStyleSheet("font: 20pt \"Algerian\";")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 260, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter The File Name"))
        self.pushButton.setText(_translate("Dialog", "Check validity"))
        self.label_4.setText(_translate("Dialog", "SOFTWARE ENGINEERING PROJECT      "))
        self.pushButton_2.setText(_translate("Dialog", "select"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    fp2 = open("upload.txt",'r')
    content = fp.readlines()
    for line in content:
        print(line)

