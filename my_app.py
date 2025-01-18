from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

     
class MainWin(QWidget):
   def __init__(self):
       ''' окно, в котором располагается приветствие '''
       super().__init__()


       # создаём и настраиваем графические элементы:
       self.initUI()


       #устанавливает связи между элементами
       self.connects()


       #устанавливает, как будет выглядеть окно (надпись, размер, место)
       self.set_appear()


       # старт:
       self.show()


   def initUI(self):
       ''' создаёт графические элементы '''
       self.btn_next = QPushButton('qwe', self)
       self.hello_text = QLabel('txt_hello')
       self.instruction = QLabel('txt_instruction')


       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
       self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
       self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
       self.setLayout(self.layout_line)
  
   def next_click(self):
       #self.tw = TestWin()
       self.hide()


   def connects(self):
       self.btn_next.clicked.connect(self.next_click)

   ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
   def set_appear(self):
       self.setWindowTitle('txt_title')
       self.resize(400, 400)
       self.move(200, 100)


app = QApplication([])
mw = MainWin()
app.exec_()
