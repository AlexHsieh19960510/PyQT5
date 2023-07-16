# 1.建立 PyQt5 視窗(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setText("測試文字")
label.setStyleSheet("font-size:20px;")
label.setGeometry(50,30,100,30)

btn = QtWidgets.QPushButton(Form)
btn.setText("開啟新視窗")
btn.setStyleSheet("font-size:16px;")
btn.setGeometry(40,60,120,40)

Form.show()
sys.exit(app.exec_())


# 2.建立 PyQt5 視窗(2)
from PyQt5 import QtWidgets
import sys

class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("測試文字")
        self.label.setStyleSheet("font-size:20px;")
        self.label.setGeometry(50,30,100,30)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("開啟新視窗")
        self.btn.setStyleSheet("font-size:16px;")
        self.btn.setGeometry(40,60,120,40)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWindow()
    Form.show()
    sys.exit(app.exec_())


# 3.主視窗點擊按鈕，開啟新視窗(1)
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setText("測試文字")
label.setStyleSheet("font-size:20px;")
label.setGeometry(50,30,100,30)

btn = QtWidgets.QPushButton(Form)
btn.setText("開啟新視窗")
btn.setStyleSheet("font-size:16px;")
btn.setGeometry(40,60,120,40)
btn.clicked.connect(lambda:Form2.show())  # 使用 lambda 函式，顯示新視窗

Form2 = QtWidgets.QWidget()               # 建立新視窗
Form2.setWindowTitle("oxxo.studio.2")
Form2.resize(300, 200)

btn2 = QtWidgets.QPushButton(Form2)
btn2.setText("test")
btn2.setGeometry(110,60,50,30)

Form.show()
sys.exit(app.exec_())


# 4.主視窗點擊按鈕，開啟新視窗(2)
from PyQt5 import QtWidgets
import sys

# 主視窗
class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("測試文字")
        self.label.setStyleSheet("font-size:20px;")
        self.label.setGeometry(50,30,100,30)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("開啟新視窗")
        self.btn.setStyleSheet("font-size:16px;")
        self.btn.setGeometry(40,60,120,40)
        self.btn.clicked.connect(self.showNewWindow)

    def showNewWindow(self):
        self.nw = newWindow()       # 連接新視窗
        self.nw.show()              # 顯示新視窗
        x = self.nw.pos().x()       # 取得新視窗目前 x 座標
        y = self.nw.pos().y()       # 取得新視窗目前 y 座標
        self.nw.move(x+100, y+100)  # 移動新視窗位置

# 新視窗
class newWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio.2")
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("test")
        self.btn.setStyleSheet("font-size:16px;")
        self.btn.setGeometry(40,60,120,40)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWindow()
    Form.show()
    sys.exit(app.exec_())


# 5.點擊按鈕修改其他視窗文字
from PyQt5 import QtWidgets
import sys

class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("測試文字")
        self.label.setStyleSheet("font-size:20px;")
        self.label.setGeometry(50,30,100,30)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("開啟新視窗")
        self.btn.setStyleSheet("font-size:16px;")
        self.btn.setGeometry(40,60,120,40)
        self.btn.clicked.connect(self.showNewWindow)        # 點擊按鈕，開啟新視窗

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText("在新視窗裡顯示文字")
        self.btn2.setStyleSheet("font-size:16px;")
        self.btn2.setGeometry(40,100,200,40)
        self.btn2.clicked.connect(self.changeNewWindowText) # 點擊按鈕，改變新視窗裡的文字

    def showNewWindow(self):
        self.nw = newWindow()
        self.nw.show()
        x = self.nw.pos().x()
        y = self.nw.pos().y()
        self.nw.move(x+50, y+50)
        self.nw.btn.clicked.connect(self.changeText)        # 點擊按鈕，改變主視窗裡的文字

    def changeText(self):
        self.label.setText("點擊按鈕囉")

    def changeNewWindowText(self):
        self.nw.label.setText("主視窗也點擊按鈕囉")

class newWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio.2")
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("")
        self.label.setStyleSheet("font-size:20px;")
        self.label.setGeometry(50,30,200,30)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("test")
        self.btn.setStyleSheet("font-size:16px;")
        self.btn.setGeometry(40,60,120,40)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWindow()
    Form.show()
    sys.exit(app.exec_())






















