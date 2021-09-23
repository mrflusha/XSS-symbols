import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import html

class App(QDialog):




    def __init__(self):
        super().__init__()
        self.title = 'idontknowwhy'
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 100
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        
        self.show()
    

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()
        layout.setColumnStretch(1, 2)
        layout.setColumnStretch(1, 4)
        button = QPushButton('click')


        self.a = QLineEdit(self)
        self.to_hex = QLineEdit(self)
        self.to_htm = QLineEdit(self)
        
        layout.addWidget(QLabel("Type:"),0,0)
        layout.addWidget(self.a,0,1)
        layout.addWidget(button,1,1)
        layout.addWidget(self.to_hex,2,1)
        layout.addWidget(self.to_htm,3,1)
        layout.addWidget(QLabel("Hex:"),2,0)
        layout.addWidget(QLabel("html:"),3,0)
        

        self.horizontalGroupBox.setLayout(layout)
        button.clicked.connect(self.slot_method)
    @pyqtSlot()
    def slot_method(self):
        b = self.a.text()
        hex_str = ""
        htm_str = html.escape(b)


            


    	
        for i in range(len(b)):
            hex_str +="%"+str(b[i].encode("utf-8").hex())

            

        self.to_hex.setText(hex_str)
        self.to_htm.setText(htm_str)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
