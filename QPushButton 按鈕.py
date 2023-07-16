# 1.加入 QPushButton 按鈕
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

btn = QtWidgets.QPushButton(Form)   # 在 Form 中加入一個 QPushButton
btn.setText("我是按鈕")               # 按鈕文字

Form.show()
sys.exit(app.exec_())


# 2.QPushButton 位置設定(1)
# 方法	            參數	    說明
# move()	        x, y	設定 QPushButton 在擺放的父元件中的 xy 座標，x 往右為正，y 往下為正，尺寸根據內容自動延伸。
# setGeometry()	x, y, w, h	設定 QPushButton 在擺放的父元件中的 xy 座標和長寬尺寸，x 往右為正，y 往下為正，如果超過長寬尺寸，預設會被裁切無法顯示。


# 3.QPushButton 位置設定(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

btn1 = QtWidgets.QPushButton(Form)
btn1.setText("按鈕 1")
btn1.move(50,30)                 # 移動到 (50,30)

btn2 = QtWidgets.QPushButton(Form)
btn2.setText("按鈕 2")
btn2.setGeometry(50,60,100,50)   # 移動到 (50,60)，大小 100x50

Form.show()
sys.exit(app.exec_())


# 4.QPushButton 樣式設定(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

btn = QtWidgets.QPushButton(Form)
btn.setText("按鈕")
btn.setGeometry(50,50,100,50)
btn.setStyleSheet('''
    background:#ff0;
    color:#f00;
    font-size:20px;
    border:2px solid #000;
''')

Form.show()
sys.exit(app.exec_())


# 5.QPushButton 樣式設定(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

btn = QtWidgets.QPushButton(Form)
btn.setText("按鈕")
btn.setGeometry(50,50,100,50)
btn.setStyleSheet('''
    QPushButton {
        font-size:20px;
        color: #f00;
        background: #ff0;
        border: 2px solid #000;
    }
    QPushButton:hover {
        color: #ff0;
        background: #f00;
    }
''')

Form.show()
sys.exit(app.exec_())


# 6.停用 QPushButton(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

btn = QtWidgets.QPushButton(Form)
btn.setText("按鈕")
btn.setGeometry(50,50,100,50)
btn.setDisabled(True)

Form.show()
sys.exit(app.exec_())


# 7.停用 QPushButton(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

btn = QtWidgets.QPushButton(Form)
btn.setText("按鈕")
btn.setGeometry(50,50,100,50)
btn.setStyleSheet('''
    QPushButton {
        font-size:20px;
        color: #f00;
        background: #ff0;
        border: 2px solid #000;
    }
    QPushButton:disabled {
        color:#fff;
        background:#ccc;
        border: 2px solid #aaa;
    }
''')
btn.setDisabled(True)

Form.show()
sys.exit(app.exec_())


# 8.QPushButton 點擊事件(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

a = 0
def show():
    global a
    a = a + 1
    label.setText(str(a))       # 更新 QLabel 內容

label = QtWidgets.QLabel(Form)
label.setText("0")
label.setStyleSheet("font-size:20px;")
label.setGeometry(50,30,100,30)

btn = QtWidgets.QPushButton(Form)
btn.setText("增加數字")
btn.setGeometry(50,60,100,30)
btn.clicked.connect(show)       # 點擊時執行 show 函式

Form.show()
sys.exit(app.exec_())


# 9.QPushButton 點擊事件(2)
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show(e):
    label.setText(e)

label = QtWidgets.QLabel(Form)
label.setText("A")
label.setStyleSheet("font-size:20px;")
label.setGeometry(50,30,100,30)

btn1 = QtWidgets.QPushButton(Form)
btn1.setText("A")
btn1.setGeometry(50,60,50,30)
btn1.clicked.connect(lambda:show("A"))  # 使用 lambda 函式

btn2 = QtWidgets.QPushButton(Form)
btn2.setText("B")
btn2.setGeometry(110,60,50,30)
btn2.clicked.connect(lambda:show("B"))  # 使用 lambda 函式

Form.show()
sys.exit(app.exec_())


# 10.QPushButton 點擊事件(3)
from PyQt5 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("A")
        self.label.setStyleSheet("font-size:20px;")
        self.label.setGeometry(50,30,100,30)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText("B")
        self.btn2.setGeometry(110,60,50,30)
        self.btn2.clicked.connect(lambda:self.showMsg("B"))  # 使用 lambda 函式

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("A")
        self.btn1.setGeometry(50,60,50,30)
        self.btn1.clicked.connect(lambda:self.showMsg("A"))  # 使用 lambda 函式

    def showMsg(self, e):
        self.label.setText(e)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())