import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    textLabel = QLabel(widget)
    textLabel.setText("this is text")
    textLabel.move(110, 85)

    button1 = QPushButton(widget)
    button1.setText("Button 1")
    button1.move(64, 32)
    button1.clicked.connect(button1_clicked)

    button2 = QPushButton(widget)
    button2.setText("Button 2")
    button2.move(64,64)
    button2.clicked.connect(button2_clicked)

    widget.setGeometry(50,50,320,200)
    widget.setWindowTitle("PyQt5 Button")
    widget.show()
    sys.exit(app.exec_())


def button1_clicked():
    print("Button 1 Clicked ")
def button2_clicked():
    print("Button 2 Clicked")

if __name__ == '__main__':
    window()
