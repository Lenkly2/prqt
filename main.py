from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from interface import *
import pyautogui
import sys
import random
a = 0
class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click)
    def click(self):
        sign = ''
        if self.ui.radioButton.isChecked():
            sign = '0123456789'
        if self.ui.radioButton_2.isChecked():
            sign = 'qwertyuiopasdfghjklzxcvbnm'
        result = ''
        for i in range(8):
            result += random.choice(sign)
        self.ui.label_2.setText(result)
        statusdel += 1
        a = random.randint(1,1000)
app = QApplication([])
ex = Widget()
ex.show()

app.exec_()
sys.exit(app.exec_())