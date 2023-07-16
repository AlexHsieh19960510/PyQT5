# 1.偵測視窗(1)
# 方法	            說明
# x()	        視窗在螢幕裡的 x 座標。
# y()	        視窗在螢幕裡的 y 座標。
# width()	    視窗的寬度。
# height()	    視窗的高度。
# windowTitle()	視窗的標題。


# 2.偵測視窗(2)
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(10,10,200,200)

label.setText(f'''
    x: {Form.x()}
    y: {Form.y()}
    w: {Form.width()}
    h: {Form.height()}
    t: {Form.windowTitle()}
''')

Form.show()
sys.exit(app.exec_())


# 3.控制視窗(1)
#       方法	                    參數	                        說明
# setWindowTitle()	                str	                        視窗標題。
# resize()	                width(int), height(int)	            改變視窗尺寸。
# move()	                    x(int), y(int)	                設定視窗位置。
# setGeometry()	    x(int), y(int), width(int), height(int)	    設定視窗位置與尺寸。
# setFixedWidth()	            hwidth(int)	                    固定視窗寬度。
# setFixedHeight()	            height(int)	                    固定視窗高度。
# setFixedSize()	        width(int), height(int)	            固定視窗尺寸。
# showMinimized()		                                        視窗最小化。
# showMaximized()		                                        視窗最大化。
# showFullscreen()		                                        視窗全螢幕。
# showNormal()		                                            視窗恢復原本尺寸。


# 4.控制視窗(2)
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

btn1 = QtWidgets.QPushButton(Form)
btn1.setGeometry(10,10,100,30)
btn1.setText("最大化")
btn1.clicked.connect(lambda: Form.showMaximized())  # 最大化

btn2 = QtWidgets.QPushButton(Form)
btn2.setGeometry(110,10,100,30)
btn2.setText("恢復大小")
btn2.clicked.connect(lambda: Form.showNormal())     # 恢復原本大小

btn3 = QtWidgets.QPushButton(Form)
btn3.setGeometry(10,50,100,30)
btn3.setText("移動視窗")
btn3.clicked.connect(lambda: Form.move(100, 100))   # 移動到 (100, 100)

Form.show()
sys.exit(app.exec_())


# 5.視窗置中、取得螢幕資訊(1)
# 方法	        說明
# width()	電腦螢幕的寬度。
# height()	電腦螢幕的高度。


# 6.視窗置中、取得螢幕資訊(2)
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
screen = QtWidgets.QApplication.desktop()
screen_w = screen.width()            # 電腦螢幕寬度
screen_h = screen.height()           # 電腦螢幕高度

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)
Form_w = Form.width()                # 視窗寬度
Form_h = Form.height()               # 視窗高度

new_x = int((screen_w - Form_w)/ 2)   # 計算後的 x 座標
new_y = int((screen_h - Form_h)/ 2)   # 計算後的 y 座標
Form.move(new_x, new_y)              # 移動視窗

Form.show()
sys.exit(app.exec_())


# 7.視窗事件(1)
#   事件	      說明
# showEvent	    開啟視窗。
# closeEvent	關閉視窗。
# moveEvent	    移動視窗。
# resizeEvent	視窗尺寸改變。
# focusInEvent	視窗為焦點 ( 需要先使用 setFocus() 方法 )。
# focusOutEvent	視窗失去焦點，使用者操作其他視窗 ( 需要先使用 setFocus() 方法 )。


# 8.視窗事件(2)
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def close(self):
    print("close!!")

def move(self):
    print("move...")

def resize(self):
    print("resize")

def show(self):
    print("show")

def focusIn(self):
    print("focus in")

def focusOut(self):
    print("focus out")

Form.closeEvent = close
Form.moveEvent = move
Form.resizeEvent = resize
Form.showEvent = show
Form.setFocus()
Form.focusInEvent = focusIn
Form.focusOutEvent = focusOut

Form.show()
sys.exit(app.exec_())


# 9.視窗事件(3)
from PyQt5 import QtWidgets
from PyQt5.QtGui import QKeySequence
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)

        self.closeEvent = self.f_close
        self.moveEvent = self.f_move
        self.resizeEvent = self.f_resize
        self.showEvent = self.f_show
        self.setFocus()
        self.focusInEvent = self.f_focusIn
        self.focusOutEvent = self.f_focusOut

    def f_close(self, event):
        print("close!!")

    def f_move(self, event):
        print("move...")

    def f_resize(self, event):
        print("resize")

    def f_show(self, event):
        print("show")

    def f_focusIn(self, event):
        print("focus in")

    def f_focusOut(self, event):
        print("focus out")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())



