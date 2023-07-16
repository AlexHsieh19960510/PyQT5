# 1.常用的滑鼠事件(1)
# 事件	                    說明
# mousePressEvent	    按下滑鼠。
# mouseReleaseEvent	    放開滑鼠。
# mouseDoubleClickEvent	連點兩下滑鼠。
# mouseMoveEvent	    按下移動滑鼠，設定 setMouseTracking(True) 可不需要按下滑鼠。
# wheelEvent	        捲動滑鼠滾輪。
# enterEvent	        滑鼠進入。
# leaveEvent	        滑鼠移出。


# 2.常用的滑鼠事件(2)
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def mousePress(self):
    print("press")

Form.mousePressEvent  = mousePress    # 新增按下滑鼠事件，事件發生時執行 mousePress 函式

Form.show()
sys.exit(app.exec_())


# 3.常用的滑鼠事件(3)
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def mousePress(self):
    print("press")

Form.mousePressEvent  = mousePress

label = QtWidgets.QLabel(Form)
label.setGeometry(10,10,100,50)
label.setStyleSheet("font-size:24px;")

def mouseMove(self):
    label.setText(f"{self.x()}, {self.y()}")   # 透過 QLabel 顯示滑鼠座標

Form.setMouseTracking(True)        # 設定不需要按下滑鼠，就能偵測滑鼠移動
Form.mouseMoveEvent  = mouseMove   # 滑鼠移動事件發生時，執行 mouseMove 函式

Form.show()
sys.exit(app.exec_())


# 4.偵測事件後可以取得的數值(1)
# 方法	                說明
# x()	        滑鼠在綁定元件裡的 x 座標 ( 綁定元件左上角為 0,0 )。
# y()	        滑鼠在綁定元件裡的 y 座標 ( 綁定元件左上角為 0,0 )。
# globalX()	    滑鼠在電腦螢幕裡的 x 座標。
# globalY()	    滑鼠在電腦螢幕裡的 y 座標。
# button()	    按下哪個滑鼠鍵，1 左鍵，2 右鍵，4 中鍵或滾輪。
# timestamp()	按下滑鼠鍵電腦時間 ( 毫秒 )。


# 5.偵測事件後可以取得的數值(2)
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(10,10,100,50)
label.setStyleSheet("font-size:24px;")

def mousePress(self):
    print(self.button())
    if self.button() == 1:
        label.setText("按下左鍵")
    elif self.button() == 2:
        label.setText("按下右鍵")
    else:
        label.setText("")

Form.mousePressEvent  = mousePress    # 新增按下滑鼠事件，事件發生時執行 mousePress 函式

Form.show()
sys.exit(app.exec_())


# 6.偵測事件後可以取得的數值(3)
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
        self.label.setGeometry(10,10,100,50)
        self.label.setStyleSheet("font-size:24px;")

    def mousePressEvent(self, event):
        print(event.button())
        if event.button() == 1:
            self.label.setText("按下左鍵")
        elif event.button() == 2:
            self.label.setText("按下右鍵")
        else:
            self.label.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())

















