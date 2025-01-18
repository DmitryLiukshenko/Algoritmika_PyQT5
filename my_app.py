from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class FirstWin(QWidget):
    def __init(self):
        super().__init__()
        
        self.graphic()

        self.set_appear()

        self.coonects()

        self.show()


    def graphic(self):
        self.hello_text = QLabel('Hi')
        self.instruction = QLabel('Инструкции')
        self.btn_next = QPushButton('Переход')

        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(self.l_line)

    def set_appear(self):
        self.setWindowTitle('ОКНО')
        self.resize(400, 400)

    def next_click(self):
        #self.second_win = 
        self.hide()


    def coonects(self):
        self.btn_next.clicked.connect(self.nex_click)

app = QApplication([])
mw = FirstWin()
app.exec_()