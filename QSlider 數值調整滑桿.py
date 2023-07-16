# 1.QSlider 數值調整滑桿
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

slider = QtWidgets.QSlider(Form)
slider.move(20,20)

Form.show()
sys.exit(app.exec_())


# 2.QSlider 格式設定
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

slider_1 = QtWidgets.QSlider(Form)   # 預設垂直
slider_1.move(20,20)

slider_2 = QtWidgets.QSlider(Form)
slider_2.setOrientation(1)           # 設定為水平
slider_2.move(50,20)

Form.show()
sys.exit(app.exec_())


# 3.QSlider 加入刻度線(1)
# type	    等同方法	            說明
#   1	QSlider.TicksAbove	    上方加入刻度線。
#   2	QSlider.TicksBelow	    下方加入刻度線。
#   3	QSlider.TicksBothSides	兩側 ( 上下或左右 ) 加入刻度線。
#   4	QSlider.TicksLeft	    左側加入刻度線。
#   5	QSlider.TicksRight	    右側加入刻度線。


# 4.QSlider 加入刻度線(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

slider_1 = QtWidgets.QSlider(Form)
slider_1.move(20,20)
slider_1.setOrientation(1)
slider_1.setTickPosition(2)          # 下方加入刻度線
slider_1.setTickInterval(10)         # 刻度線間距 ( 會有十條刻度線 )

slider_2 = QtWidgets.QSlider(Form)
slider_2.move(20,60)
slider_2.setOrientation(1)
slider_2.setTickPosition(3)          # 上下都加入刻度線
slider_2.setTickInterval(20)         # 刻度線間距 ( 會有五條刻度線 )

Form.show()
sys.exit(app.exec_())


# 5.QSlider 樣式設定
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

slider = QtWidgets.QSlider(Form)
slider.setGeometry(20,20,200,30)
slider.setOrientation(1)
slider.setStyleSheet('''
    QSlider {
        border-radius: 10px;
    }
    QSlider::groove:horizontal {
        height: 5px;
        background: #000;
    }
    QSlider::handle:horizontal{
        background: #f00;
        width: 16px;
        height: 16px;
        margin:-6px 0;
        border-radius:8px;
    }
    QSlider::sub-page:horizontal{
        background:#f90;
    }
''')

Form.show()
sys.exit(app.exec_())


# 6.QSlider 常用方法
# 方法	                    參數	        說明
# setValue()	            int	        設定預設數值。
# setInvertedAppearance()	bool	    是否由小到大，預設 False 小到大，True 大到小。
# setTickPosition()	        type	    設定刻度線位置。
# setTickInterval()	        int	        設定刻度線間隔。
# setRange()	            min, max	設定數值調整範圍。
# setMaximum()	            int	        設定數值調整的最大值。
# setMinimum()	            int	        設定數值調整的最小值。
# valueChanged.connect()	fn	        數值調整時要執行的函式。
# value()		                        取得目前調整的數值。
# tickInterval()		                取得目前刻度的間隔。


# 7.顯示數值調整滑桿的數值(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(20,20,100,30)

def show():
    label.setText(str(slider.value()))

slider = QtWidgets.QSlider(Form)
slider.setGeometry(20,40,100,30)
slider.setRange(0, 100)
slider.setOrientation(1)
slider.valueChanged.connect(show)

Form.show()
sys.exit(app.exec_())


# 8.顯示數值調整滑桿的數值(2)
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
        self.label.setGeometry(20,20,100,30)

        self.slider = QtWidgets.QSlider(self)
        self.slider.setGeometry(20,40,100,30)
        self.slider.setRange(0, 100)
        self.slider.setOrientation(1)
        self.slider.valueChanged.connect(self.showMsg)

    def showMsg(self):
        self.label.setText(str(self.slider.value()))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())































