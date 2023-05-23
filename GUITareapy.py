import sys
import os
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GUITarea import *

class Ui_Dialog(QtWidgets.QMainWindow,Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #-------------------------
     
        #-------------------------
        self.pushButton.clicked.connect(self.analizar)
        
    def analizar(self):
        if self.NombreA.text()!="" and self.TextoAE.text()!="" and self.TextoAE_2.text()!="":
            vocales = "aeoui"
            contV = 0
            contC = 0
            mult = int(self.TextoAE_2.text())
            palabra = str(self.TextoAE.text())
            for char in self.TextoAE.text().lower():
                if char.isalpha():
                    if char in vocales:
                        contV+=1
                    else:
                        contC+=1
            vocal = int(contV)*int(mult)
            const = int(contC)*int(mult)
            self.NumeroV.setText(str(vocal))
            self.NumeroC.setText(str(const))
            print(str(contC), str(contV), self.TextoAE_2.text())
            archivo = open(str(self.NombreA.text())+".txt","x")
            for i in range(mult):
                archivo.write(palabra+"\n")
            archivo.close()
            
				
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_Dialog()
    window.show()
    app.exec_()
