# 1.QCheckBox 複選按鈕
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

cb_a = QtWidgets.QCheckBox(Form)    # 複選按鈕 A
cb_a.setGeometry(30, 60, 50, 20)
cb_a.setText("A")

cb_b = QtWidgets.QCheckBox(Form)    # 複選按鈕 B
cb_b.setGeometry(80, 60, 50, 20)
cb_b.setText("B")

cb_c = QtWidgets.QCheckBox(Form)    # 複選按鈕 C
cb_c.setGeometry(130, 60, 50, 20)
cb_c.setText("C")

Form.show()
sys.exit(app.exec_())


# 2.QCheckBox 位置設定(1)
# 方法	            參數	    說明
# move()	        x, y	設定 QCheckBox 在擺放的父元件中的 xy 座標，x 往右為正，y 往下為正，尺寸根據內容自動延伸。
# setGeometry()	x, y, w, h	設定 QCheckBox 在擺放的父元件中的 xy 座標和長寬尺寸，x 往右為正，y 往下為正，如果超過長寬尺寸，預設會被裁切無法顯示。


# 3.QCheckBox 位置設定(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

cb_a = QtWidgets.QCheckBox(Form)    # 複選按鈕 A
cb_a.move(30, 60)
cb_a.setText("A")

cb_b = QtWidgets.QCheckBox(Form)    # 複選按鈕 B
cb_b.move(80, 60)
cb_b.setText("B")

cb_c = QtWidgets.QCheckBox(Form)    # 複選按鈕 C
cb_c.setGeometry(130, 60, 50, 20)
cb_c.setText("C")

cb_d = QtWidgets.QCheckBox(Form)    # 複選按鈕 D
cb_d.setGeometry(180, 60, 50, 20)
cb_d.setText("D")

Form.show()
sys.exit(app.exec_())


# 4.QCheckBox 狀態設定(1)
# 方法	        參數	    說明
# setDisabled()	bool	是否停用，預設 False 啟用，可設定 True 停用。
# setChecked()	bool	是否勾選，預設 False 不勾選，可設定 True 勾選，若同一組有多個勾選，則以最後一個為主。
# toggle()		        勾選狀態切換。


# 5.QCheckBox 狀態設定(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

cb_a = QtWidgets.QCheckBox(Form)    # 複選按鈕 A
cb_a.move(30, 60)
cb_a.setText("A")
cb_a.setChecked(True)               # 預先選取

cb_b = QtWidgets.QCheckBox(Form)    # 複選按鈕 B
cb_b.move(80, 60)
cb_b.setText("B")
cb_b.setDisabled(True)              # 停用

cb_c = QtWidgets.QCheckBox(Form)
cb_c.setGeometry(130, 60, 50, 20)
cb_c.setText("C")

Form.show()
sys.exit(app.exec_())


# 6.QCheckBox 樣式設定
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

# 設定 QCheckBox
style = '''
    QCheckBox {
        color: #00f;
    }
    QCheckBox:hover {
        color: #f00;
    }
    QCheckBox:checked {
        color: #fff;
        background: #000;
    }
'''

cb_a = QtWidgets.QCheckBox(Form)
cb_a.move(30, 60)
cb_a.setText("A")
cb_a.setStyleSheet(style)    # 套用 style

cb_b = QtWidgets.QCheckBox(Form)
cb_b.move(80, 60)
cb_b.setText("B")
cb_b.setStyleSheet(style)    # 套用 style

cb_c = QtWidgets.QCheckBox(Form)
cb_c.move(130, 60)
cb_c.setText("C")
cb_c.setStyleSheet(style)    # 套用 style

Form.show()
sys.exit(app.exec_())


# 7.QCheckBox 點擊事件(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

arr = [""]* 3                  # 先新增一個串列放入文字
def show(cb, i):
    global a
    if cb.isChecked():
        arr[i] = cb.text()    # 如果該按鈕是勾選狀態，在串列的指定位置放入文字
    else:
        arr[i] = ""           # 如果該按鈕是勾選狀態，在串列的指定位置放入空字串
    output = "".join(arr)     # 組合串列內容為文字
    label.setText(output)     # label 顯示文字

label = QtWidgets.QLabel(Form)
label.setGeometry(30, 30, 100, 30)

cb_a = QtWidgets.QCheckBox(Form)
cb_a.move(30, 60)
cb_a.setText("A")
cb_a.clicked.connect(lambda:show(cb_a, 0))  # 點擊按鈕時，回傳兩個參數給 show 函式

cb_b = QtWidgets.QCheckBox(Form)
cb_b.move(80, 60)
cb_b.setText("B")
cb_b.clicked.connect(lambda:show(cb_b, 1))  # 點擊按鈕時，回傳兩個參數給 show 函式

cb_c = QtWidgets.QCheckBox(Form)
cb_c.move(130, 60)
cb_c.setText("C")
cb_c.clicked.connect(lambda:show(cb_c, 2))  # 點擊按鈕時，回傳兩個參數給 show 函式

Form.show()
sys.exit(app.exec_())


# 8.QCheckBox 點擊事件(2)
from PyQt5 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)
        self.arr = [""]* 3
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(30, 30, 100, 30)

        cb_a = QtWidgets.QCheckBox(self)
        cb_a.move(30, 60)
        cb_a.setText("A")
        cb_a.clicked.connect(lambda: self.showMsg(cb_a, 0))

        cb_b = QtWidgets.QCheckBox(self)
        cb_b.move(80, 60)
        cb_b.setText("B")
        cb_b.clicked.connect(lambda: self.showMsg(cb_b, 1))

        cb_c = QtWidgets.QCheckBox(self)
        cb_c.move(130, 60)
        cb_c.setText("C")
        cb_c.clicked.connect(lambda: self.showMsg(cb_c, 2))

    def showMsg(self, cb, i):
        if cb.isChecked():
            self.arr[i] = cb.text()
        else:
            self.arr[i] = ""
        output = "".join(self.arr)
        self.label.setText(output)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())
