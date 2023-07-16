# 1.QLabel 標籤
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)   # 在 Form 裡加入標籤
label.setText("hello world")     # 設定標籤文字

Form.show()
sys.exit(app.exec_())


# 2.QLabel 位置設定(1)
# 方法	                        參數	                說明
# move()	                    x, y	            設定 QLabel 在擺放的父元件中的 xy 座標，x 往右為正，y 往下為正，尺寸根據內容自動延伸。
# setGeometry()	            x, y, w, h	            設定 QLabel 在擺放的父元件中的 xy 座標和長寬尺寸，x 往右為正，y 往下為正，如果超過長寬尺寸，預設會被裁切無法顯示。
# setContentsMargins()	left, top, right, bottom	QLabel 的邊界寬度。


# 3.QLabel 位置設定(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label1 = QtWidgets.QLabel(Form)
label1.setText("hello world, how are you?")
label1.move(50, 50)

label2 = QtWidgets.QLabel(Form)
label2.setText("hello world, how are you?")
label2.setGeometry(50, 80, 100, 100)

Form.show()
sys.exit(app.exec_())


# 4.QLabel 文字設定(1)
# 方法	                參數	            說明
# setWordWrap()	        bool	        是否換行，預設 Fasle 不換行，設定 True 換行。
# setAlignment()	QtCore.Qt.Align	    對齊方式，預設 QtCore.Qt.AlignLeft，可設定 QtCore.Qt.AlignCenter、QtCore.Qt.AlignRight。
# setFont()	        QtGui.QFont()	    文字樣式設定，需搭配 QtGui.QFont()。

# 使用 QtGui.QFont() 產生的文字樣式，可以使用下列方法設定：

# 方法	                參數	    說明
# font.setFamily()	    name	字體名稱。
# setPointSize	        int	    字體大小。
# setBold()	            bool	是否粗體，預設 False。
# setItalic()	        bool	是否斜體，預設 False。
# setStrikeOut()	    bool	是否加入刪除線，預設 False。
# setUnderline()	    bool	是否加入底線，預設 False。


# 5.QLabel 文字設定(2)
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setText("hello world, how are you?")
label.setGeometry(30, 30, 100, 100)

label.setContentsMargins(0,0,0,0)          # 設定邊界
label.setWordWrap(True)                    # 可以換行
label.setAlignment(QtCore.Qt.AlignCenter)  # 對齊方式

font = QtGui.QFont()                       # 加入文字設定
font.setFamily('Verdana')                  # 設定字體
font.setPointSize(20)                      # 文字大小
font.setBold(True)                         # 粗體
font.setItalic(True)                       # 斜體
font.setStrikeOut(True)                    # 刪除線
font.setUnderline(True)                    # 底線
label.setFont(font)

Form.show()
sys.exit(app.exec_())


# 6.QLabel 加入圖片
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(20, 20, 200, 150)

img = QtGui.QImage("mona.jpg")                 # 讀取圖片
label.setPixmap(QtGui.QPixmap.fromImage(img))  # 加入圖片

Form.show()
sys.exit(app.exec_())


# 7.使用 StyleSheet 設定 QLabel 樣式(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setText("hello world, how are you?")
label.setGeometry(20, 20, 200, 150)
label.setWordWrap(True)

label.setStyleSheet('''
    background:#fff;
    color:#f00;
    font-size:20px;
    font-weight:bold;
    border:2px dashed #000;
    padding:20px;
    text-align:center;
''')

Form.show()
sys.exit(app.exec_())


# 8.使用 StyleSheet 設定 QLabel 樣式(2)
from PyQt5 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)
        self.setStyleSheet("background:#fcc;")
        self.ui()

    def ui(self):
        label = QtWidgets.QLabel(self)
        label.setText("hello world, how are you?")
        label.setGeometry(20, 20, 200, 150)
        label.setWordWrap(True)

        label.setStyleSheet('''
            background:#fff;
            color:#f00;
            font-size:20px;
            font-weight:bold;
            border:2px dashed #000;
            padding:20px;
            text-align:center;
        ''')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())

























