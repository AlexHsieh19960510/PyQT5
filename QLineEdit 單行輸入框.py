# 1.QLineEdit 單行輸入框
from PyQt5 import QtWidgets, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

input = QtWidgets.QLineEdit(Form)   # 建立單行輸入框
input.setGeometry(20,20,100,20)     # 設定位置和尺寸

Form.show()
sys.exit(app.exec_())


# 2.QLineEdit 位置設定(1)
# 方法	            參數	    說明
# move()	        x, y	設定 QLineEdit 在擺放的父元件中的 xy 座標，x 往右為正，y 往下為正，尺寸根據內容自動延伸。
# setGeometry()	x, y, w, h	設定 QLineEdit 在擺放的父元件中的 xy 座標和長寬尺寸，x 往右為正，y 往下為正，如果超過長寬尺寸，輸入的文字會被裁切無法顯示。


# 3.QLineEdit 位置設定(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

input_1 = QtWidgets.QLineEdit(Form)   # 第一個輸入框
input_1.move(20,20)

input_2 = QtWidgets.QLineEdit(Form)   # 第二個輸入框
input_2.setGeometry(20,50,100,20)

Form.show()
sys.exit(app.exec_())


# 4.QLineEdit 樣式設定
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

input_1 = QtWidgets.QLineEdit(Form)
input_1.move(20,20)
input_1.setStyleSheet('''
    QLineEdit {
        border:1px solid #000;
    }
    QLineEdit:focus {
        border:2px solid #f00;
        background:#ff0;
    }
''')

input_2 = QtWidgets.QLineEdit(Form)
input_2.setGeometry(20,50,100,20)

Form.show()
sys.exit(app.exec_())


# 5.QLineEdit 常用方法(1)
# 方法	                參數	    說明
# setText()	            str	    預設輸入的文字內容。
# setReadOnly()	        bool	設定只能讀取，預設 False。
# setDisabled()	        bool	設定是否禁用，預設 False。
# setMaxLength()	    int	    輸入的最大字元數。
# setFocus()		            設定為焦點。
# setEchoMode()	        mode	設定 QtWidgets.QLineEdit.Password 表示為密碼 ( 看不見輸入內容 )。
# textChanged.connect()	fn	    文字改變時要執行的函式。
# text()		                取得輸入框內容。


# 6.QLineEdit 常用方法(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

input_1 = QtWidgets.QLineEdit(Form)
input_1.setGeometry(20,20,100,20)
input_1.setEchoMode(QtWidgets.QLineEdit.Password)
input_1.setText("12345")
input_1.setMaxLength(5)

input_2 = QtWidgets.QLineEdit(Form)
input_2.setGeometry(20,50,100,20)
input_2.setFocus()

Form.show()
sys.exit(app.exec_())


# 7.取得 QLineEdit 輸入字內容(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show():
    label.setText(input.text())

input = QtWidgets.QLineEdit(Form)
input.setGeometry(20,20,100,20)
input.textChanged.connect(show)

label = QtWidgets.QLabel(Form)
label.setGeometry(20,50,100,20)

Form.show()
sys.exit(app.exec_())


# 8.取得 QLineEdit 輸入字內容(2)
from PyQt5 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.input = QtWidgets.QLineEdit(self)
        self.input.setGeometry(20,20,100,20)
        self.input.textChanged.connect(self.showMsg)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(20,50,100,20)

    def showMsg(self):
        self.label.setText(self.input.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())

