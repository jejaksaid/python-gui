import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#Create a window with a button. If you click the button, the dialog will popup.

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    button1 = QPushButton(win)
    button1.setText("Show Dialog!")
    button1.move(100,100)
    button1.clicked.connect(showDialog)
    win.setWindowTitle("Click Button")
    win.show()
    sys.exit(app.exec_())

'''A dialog is created with QMessageBox(). Don’t forget to import this from PyQt5.
Then use the methods setIcon(), setText(), setWindowTitle() to set the window decoration.
You can configure the dialogs buttons with setStandardButtons().'''
def showDialog():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Message box pop up window")
    msgBox.setWindowTitle("QMessageBox Example")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.buttonClicked.connect(msgButtonClick)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('Ok Clicked')

def msgButtonClick(i):
    print("Button clicked is:", i.text())

if __name__ == '__main__':
    window()
