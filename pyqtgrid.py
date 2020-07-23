import sys
from Pyqt5.QtWidget import QApplication, QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

  app = QApplication(sys.argv)
  win = QWidget()
  grid = QGridLayout()
  
  for i in range(0,5):
    for j in range(0,5):
      grid.addWidget(QPushButton(str(i)+str(j)),i,j)
      
  win.setLayout(grid)
  win.setWindowTittle("PyQt5 GridLayout)
  win.setGeometry(50,50,200,200)
  win.show()
  sys.exit(app.exec_())
  
if __name__ = '__main__':
  window()
