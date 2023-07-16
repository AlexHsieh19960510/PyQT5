# 1.QRadioButton 單選按鈕(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

rb_a = QtWidgets.QRadioButton(Form)    # 單選按鈕 A
rb_a.setGeometry(30, 30, 100, 20)
rb_a.setText("A")

rb_b = QtWidgets.QRadioButton(Form)    # 單選按鈕 B
rb_b.setGeometry(30, 60, 100, 20)
rb_b.setText("B")

Form.show()
sys.exit(app.exec_())


# 2.QRadioButton 單選按鈕(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

rb_a = QtWidgets.QRadioButton(Form)    # 單選按鈕 A
rb_a.setGeometry(30, 30, 100, 20)
rb_a.setText("A")

rb_b = QtWidgets.QRadioButton(Form)    # 單選按鈕 B
rb_b.setGeometry(30, 60, 100, 20)
rb_b.setText("B")

group1 = QtWidgets.QButtonGroup(Form)  # 按鈕群組
group1.addButton(rb_a)                 # 加入單選按鈕 A
group1.addButton(rb_b)                 # 加入單選按鈕 B

rb_c = QtWidgets.QRadioButton(Form)    # 單選按鈕 C
rb_c.setGeometry(150, 30, 100, 20)
rb_c.setText("C")

rb_d = QtWidgets.QRadioButton(Form)    # 單選按鈕 D
rb_d.setGeometry(150, 60, 100, 20)
rb_d.setText("D")

group2 = QtWidgets.QButtonGroup(Form)  # 按鈕群組
group2.addButton(rb_c)                 # 加入單選按鈕 C
group2.addButton(rb_d)                 # 加入單選按鈕 D

Form.show()
sys.exit(app.exec_())


# 3.QRadioButton 位置設定(1)
# 方法	            參數	    說明
# move()	        x, y	設定 QRadioButton 在擺放的父元件中的 xy 座標，x 往右為正，y 往下為正，尺寸根據內容自動延伸。
# setGeometry()	x, y, w, h	設定 QRadioButton 在擺放的父元件中的 xy 座標和長寬尺寸，x 往右為正，y 往下為正，如果超過長寬尺寸，預設會被裁切無法顯示。


# 4.QRadioButton 位置設定(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

rb_a = QtWidgets.QRadioButton(Form)  # 單選按鈕 A
rb_a.move(30, 30)
rb_a.setText("A")

rb_b = QtWidgets.QRadioButton(Form)  # 單選按鈕 C
rb_b.move(30, 60)
rb_b.setText("B")

rb_c = QtWidgets.QRadioButton(Form)  # 單選按鈕 D
rb_c.setGeometry(150, 30, 100, 20)
rb_c.setText("C")

rb_d = QtWidgets.QRadioButton(Form)  # 單選按鈕 E
rb_d.setGeometry(150, 60, 100, 20)
rb_d.setText("D")

Form.show()
sys.exit(app.exec_())


# 5.QRadioButton 狀態設定(1)
# 方法	        參數	    說明
# setDisabled()	bool	是否停用，預設 False 啟用，可設定 True 停用。
# setChecked()	bool	是否勾選，預設 False 不勾選，可設定 True 勾選，若同一組有多個勾選，則以最後一個為主。
# toggle()		        勾選狀態切換。


# 6.QRadioButton 狀態設定(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

rb_a = QtWidgets.QRadioButton(Form)
rb_a.setGeometry(30, 30, 100, 20)
rb_a.setText("A")

rb_b = QtWidgets.QRadioButton(Form)
rb_b.setGeometry(30, 60, 100, 20)
rb_b.setText("B")
rb_b.setDisabled(True)

rb_c = QtWidgets.QRadioButton(Form)
rb_c.setGeometry(30, 90, 100, 20)
rb_c.setText("C")
rb_c.setChecked(True)

Form.show()
sys.exit(app.exec_())


# 7.QRadioButton 樣式設定(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

rb_a = QtWidgets.QRadioButton(Form)
rb_a.setGeometry(30, 30, 100, 20)
rb_a.setText("A")
# 設定按鈕 A 的樣式
rb_a.setStyleSheet('''
    QRadioButton {
        color: #00f;
    }
    QRadioButton:hover {
        color:#f00;
    }
''')

rb_b = QtWidgets.QRadioButton(Form)
rb_b.setGeometry(30, 60, 100, 20)
rb_b.setText("B")
# 設定按鈕 B 的樣式
rb_b.setStyleSheet('''
    QRadioButton {
        color: #00f;
    }
    QRadioButton:hover {
        color:#f00;
    }
''')

Form.show()
sys.exit(app.exec_())


# 8.QRadioButton 樣式設定(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

rb_a = QtWidgets.QRadioButton(Form)
rb_a.setGeometry(30, 30, 100, 20)
rb_a.setText("A")
rb_a.setStyleSheet('''
    QRadioButton {
        color: #00f;
    }
    QRadioButton:hover {
        color:#f00;
    }
''')

rb_b = QtWidgets.QRadioButton(Form)
rb_b.setGeometry(30, 60, 100, 20)
rb_b.setText("B")
rb_b.setStyleSheet('''
    QRadioButton {
        color: #00f;
    }
    QRadioButton:hover {
        color:#f00;
    }
    QRadioButton:disabled {
        color:#ccc;
    }
''')
rb_b.setDisabled(True)   # 停用按鈕 B

Form.show()
sys.exit(app.exec_())


# 9.QRadioButton 點擊事件(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

rb_a = QtWidgets.QRadioButton(Form)
rb_a.setGeometry(30, 60, 100, 20)
rb_a.setText("A")

rb_b = QtWidgets.QRadioButton(Form)
rb_b.setGeometry(150, 60, 100, 20)
rb_b.setText("B")

def show():
    label.setText(str(group.checkedId()))   # 設定 label 文字為按鈕群組中勾選按鈕的 ID

group = QtWidgets.QButtonGroup(Form)
group.addButton(rb_a, 1)               # 添加 QRadioButton A，ID 設定為 1
group.addButton(rb_b, 2)               # 添加 QRadioButton B，ID 設定為 2
group.buttonClicked.connect(show)      # 綁定點擊事件

label = QtWidgets.QLabel(Form)
label.setGeometry(30, 30, 100, 20)

Form.show()
sys.exit(app.exec_())


# 10.QRadioButton 點擊事件(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show(rb):
    label.setText(rb.text() + ":" + str(rb.isChecked()))  # 取得按鈕狀態

rb_a = QtWidgets.QRadioButton(Form)
rb_a.setGeometry(30, 60, 100, 20)
rb_a.setText("A")
rb_a.toggled.connect(lambda: show(rb_a))  # 綁定函式

rb_b = QtWidgets.QRadioButton(Form)
rb_b.setGeometry(150, 60, 100, 20)
rb_b.setText("B")
rb_b.toggled.connect(lambda: show(rb_b))  # 綁定函式

group = QtWidgets.QButtonGroup(Form)
group.addButton(rb_a)
group.addButton(rb_b)

label = QtWidgets.QLabel(Form)
label.setGeometry(30, 30, 100, 20)

Form.show()
sys.exit(app.exec_())


# 11.QRadioButton 點擊事件(3)
from PyQt5 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)
        self.ui()

    def ui(self):
        rb_a = QtWidgets.QRadioButton(self)
        rb_a.setGeometry(30, 60, 100, 20)
        rb_a.setText("A")
        rb_a.toggled.connect(lambda: self.showMsg(rb_a))  # 綁定函式

        rb_b = QtWidgets.QRadioButton(self)
        rb_b.setGeometry(150, 60, 100, 20)
        rb_b.setText("B")
        rb_b.toggled.connect(lambda: self.showMsg(rb_b))  # 綁定函式

        group = QtWidgets.QButtonGroup(self)
        group.addButton(rb_a)
        group.addButton(rb_b)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(30, 30, 100, 20)

    def showMsg(self, rb):
        self.label.setText(rb.text() + ":" + str(rb.isChecked()))  # 取得按鈕狀態

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())