#1.安裝PyQt5
pip install PyQt5(terminal輸入)


#2.PyQt5例子(1)
from PyQt5 import QtWidgets, QtCore
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

pushButton = QtWidgets.QPushButton(MainWindow)
pushButton.setGeometry(QtCore.QRect(100, 70, 113, 32))
pushButton.setObjectName("pushButton")
pushButton.setText("PushButton")

MainWindow.show()
sys.exit(app.exec_())


#3.PyQt5例子(2)
from PyQt5 import QtWidgets, QtCore
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)
        self.ui()

    def ui(self):
        pushButton = QtWidgets.QPushButton(self)
        pushButton.setGeometry(QtCore.QRect(100, 70, 113, 32))
        pushButton.setObjectName("pushButton")
        pushButton.setText("PushButton")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWidget()
    MainWindow.show()
    sys.exit(app.exec_())