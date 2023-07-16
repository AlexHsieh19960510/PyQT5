# 1.QComboBox 下拉選單
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 300)

box = QtWidgets.QComboBox(Form)   # 加入下拉選單
box.addItems(["A","B","C","D"])   # 加入四個選項
box.setGeometry(10,10,200,30)

Form.show()
sys.exit(app.exec_())


# 2.QComboBox 預設選項
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

box = QtWidgets.QComboBox(Form)
box.addItems(["A","B","C","D"])
box.setGeometry(10,10,200,30)
box.setCurrentIndex(1)     # 預先顯示第二個選項 ( 第一個為 0 )
box.setCurrentText("D")    # 如果選項文字為 D，則顯示 D

Form.show()
sys.exit(app.exec_())


# 3.QComboBox 添加、刪除選項
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

box = QtWidgets.QComboBox(Form)
box.addItems(["A","B","C","D"])
box.setGeometry(10,10,200,30)

box.addItem("apple")     # 在最後方添加 apple 選項
box.removeItem(2)        # 移除第三個選項 C
box.insertItem(0, "ok")  # 在最前方加入 ok 為第一個選項

Form.show()
sys.exit(app.exec_())


# 4.QComboBox 常用方法(1)
# 方法	                            參數	    說明
# addItem()	                        str	    從最後方增加單一個項目。
# addItems()	                    list	以串列方式增加多個項目。
# insertItem()	                index, str	從指定位置添加項目。
# insertItems()	                index, list	以串列的方式，在指定位置添加多個項目。
# removeItem()	                    index	移除指定項目。
# setDisabled()	                    bool	設定是否禁用，預設 False。
# currentIndexChanged.connect()	    fn	    選項改變時要執行的函式。
# currentText()		                        選擇項目的文字。
# currentIndex()		                    選擇項目的索引值。
# setItemIcon()	                index, icon	設定指定選項的 icon，icon 使用 QtGui.QIcon(圖片路徑)。


# 5.QComboBox 常用方法(2)
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

box = QtWidgets.QComboBox(Form)
box.addItems(["A","B","C","D"])
box.setGeometry(10,10,200,30)
box.setItemIcon(0, QtGui.QIcon("icon.png"))
box.setItemIcon(1, QtGui.QIcon("mona.jpg"))
box.setItemIcon(2, QtGui.QIcon("orange.jpg"))
box.setItemIcon(3, QtGui.QIcon("ok.png"))

Form.show()
sys.exit(app.exec_())


# 6.顯示 QComboBox 選擇項目(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(10,10,200,30)


def show():
    text = box.currentText()
    num = box.currentIndex()
    label.setText(f"{num}:{text}")

box = QtWidgets.QComboBox(Form)
box.addItems(["A","B","C","D"])
box.setGeometry(10,50,200,30)
box.currentIndexChanged.connect(show)

Form.show()
sys.exit(app.exec_())


# 7.顯示 QComboBox 選擇項目(2)
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
        self.label.setGeometry(10,10,200,30)

        self.box = QtWidgets.QComboBox(self)
        self.box.addItems(["A","B","C","D"])
        self.box.setGeometry(10,50,200,30)
        self.box.currentIndexChanged.connect(self.showMsg)

    def showMsg(self):
        text = self.box.currentText()
        num = self.box.currentIndex()
        self.label.setText(f"{num}:{text}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())
