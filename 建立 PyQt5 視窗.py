# 1.建立 PyQt5 視窗
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv) # 視窗程式開始

Form = QtWidgets.QWidget()             # 放入基底元件
Form.show()                            # 顯示元件

sys.exit(app.exec_())                  # 視窗程式結束


# 2.調整視窗樣式(1)
#       方法	        參數	        說明
# setWindowTitle()	    str	        設定標題。
# resize()	        width, height	設定開啟視窗時的長寬。
# setStyleSheet()	    style	    使用網頁 CSS 樣式設定樣式 ( 不支援 CSS3 語法 )。
# width()		                    取得視窗寬度。
# height()		                    取得視窗高度。


# 3.調整視窗樣式(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")      # 設定標題
Form.resize(320, 240)                   # 設定長寬尺寸
Form.setStyleSheet("background:#fcc;")  # 使用網頁 CSS 樣式設定背景

print(Form.width())                     # 印出寬度
print(Form.height())                    # 印出高度

Form.show()
sys.exit(app.exec_())


# 4.在視窗中放入其他元件(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(320, 240)
Form.setStyleSheet("background:#fcc;")

print(Form.width())
print(Form.height())

label = QtWidgets.QLabel(Form)     # 在 Form 裡加入 label
label.move(50,50)                  # 移動到 (50, 50) 的位置
label.setText("hello world")       # 寫入文字
label.setStyleSheet("font-size:30px; color:#00c")  # 設定樣式

Form.show()
sys.exit(app.exec_())


# 5.在視窗中放入其他元件(2)
from PyQt5 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")      # 建立 MainWindow 視窗
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)
        self.setStyleSheet("background:#fcc;")
        self.ui()

    def ui(self):
        label = QtWidgets.QLabel(self)
        label.move(50,50)
        label.setText("hello world")
        label.setStyleSheet("font-size:30px; color:#00c")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())


