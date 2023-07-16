# 1.QWebEngineView 顯示網頁元件(1)
pip install PyQtWebEngine



# 2.QWebEngineView 顯示網頁元件(2)
from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(800, 600)

widget = QtWebEngineWidgets.QWebEngineView(Form)  # 建立網頁顯示元件
widget.move(0,0)
widget.resize(800, 600)
widget.load(QtCore.QUrl("https://google.com"))    # 載入網頁

Form.show()
sys.exit(app.exec_())


# 3.網頁控制常用方法(1)
# 方法	                            說明
# load()	                    載入網頁。
# reload()	                    重新整理網頁。
# forward()	                    前一頁。
# back()	                    後一頁。
# stop()	                    停止載入網頁。
# title()	                    取得網頁標題。
# icon()	                    取得網頁圖示。
# selectedText()	            取得網頁中所選取的文字。
# loadFinished.connect(fn)	    網頁載入完成後要執行的函式。
# selectionChanged.connect(fn)	在網頁中發生選取事件時要執行的函式。


# 4.網頁控制常用方法(2)
from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(800, 600)

btn1 = QtWidgets.QPushButton(Form)
btn1.setGeometry(10,10,80,30)
btn1.setText("重新整理")
btn1.clicked.connect(lambda: widget.reload())  # 重新載入網頁

btn2 = QtWidgets.QPushButton(Form)
btn2.setGeometry(100,10,80,30)
btn2.setText("下一頁")
btn2.clicked.connect(lambda: widget.forward())  # 前往上一頁

btn3 = QtWidgets.QPushButton(Form)
btn3.setGeometry(190,10,80,30)
btn3.setText("上一頁")
btn3.clicked.connect(lambda: widget.back())    # 前往下一頁

btn4 = QtWidgets.QPushButton(Form)
btn4.setGeometry(280,10,80,30)
btn4.setText("停止")
btn4.clicked.connect(lambda: widget.stop())    # 停止網頁載入

input = QtWidgets.QLineEdit(Form)    # 建立單行輸入框
input.setGeometry(400,10,200,30)

def go():
    url = input.text()
    widget.load(QtCore.QUrl(url))    # 載入輸入的網址

btn5 = QtWidgets.QPushButton(Form)
btn5.setGeometry(600,10,80,30)
btn5.setText("前往")
btn5.clicked.connect(go)             # 按下前往按鈕，執行 go 函式

def finished():
    Form.setWindowTitle(widget.title())  # 更新視窗標題
    Form.setWindowIcon(widget.icon())    # 更新視窗圖示

def show():
    print(widget.selectedText())         # 印出選取的文字

widget = QtWebEngineWidgets.QWebEngineView(Form)
widget.move(0,60)
widget.resize(800, 540)
widget.load(QtCore.QUrl("https://google.com"))
widget.loadFinished.connect(finished)
widget.selectionChanged.connect(show)

Form.show()
sys.exit(app.exec_())


# 5.網頁控制常用方法(3)
from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(800, 600)
        self.web()
        self.ui()

    def web(self):
        self.widget = QtWebEngineWidgets.QWebEngineView(self)
        self.widget.move(0,60)
        self.widget.resize(800, 540)
        self.widget.load(QtCore.QUrl("https://google.com"))
        self.widget.loadFinished.connect(self.finished)
        self.widget.selectionChanged.connect(self.show)

    def ui(self):
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setGeometry(10,10,80,30)
        self.btn1.setText("重新整理")
        self.btn1.clicked.connect(lambda: self.widget.reload())

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setGeometry(100,10,80,30)
        self.btn2.setText("下一頁")
        self.btn2.clicked.connect(lambda: self.widget.forward())

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setGeometry(190,10,80,30)
        self.btn3.setText("上一頁")
        self.btn3.clicked.connect(lambda: self.widget.back())

        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.setGeometry(280,10,80,30)
        self.btn4.setText("停止")
        self.btn4.clicked.connect(lambda: self.widget.stop())

        self.btn5 = QtWidgets.QPushButton(self)
        self.btn5.setGeometry(600,10,80,30)
        self.btn5.setText("前往")
        self.btn5.clicked.connect(self.go)

        self.input = QtWidgets.QLineEdit(self)
        self.input.setGeometry(400,10,200,30)

    def go(self):
        url = self.input.text()
        self.widget.load(QtCore.QUrl(url))

    def finished(self):
        self.setWindowTitle(self.widget.title())
        self.setWindowIcon(self.widget.icon())

    def showMsg(self):
        print(self.widget.selectedText())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())
