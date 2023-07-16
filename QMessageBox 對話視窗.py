# 1.QMessageBox 對話視窗
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 300)

def show():
    mbox = QtWidgets.QMessageBox(Form)       # 加入對話視窗
    mbox.information(Form, "info", "hello")  # 開啟資訊通知的對話視窗，標題 info，內容 hello

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText("彈出視窗")
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec_())


# 2.QMessageBox 的類型(1)
# 方法	                參數	            說明
# information()	parent, title, text	    資訊通知對話視窗。
# question()	parent, title, text	    二選一問題對話視窗。
# warning()	    parent, title, text	    警告視窗。
# critical()	parent, title, text	    關鍵警告視窗


# 3.QMessageBox 的類型(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show(n):
    mbox = QtWidgets.QMessageBox(Form)
    if n == 1:
      mbox.information(Form, "information", "information...")
    elif n == 2:
      mbox.question(Form, "question", "question?")
    elif n == 3:
      mbox.warning(Form, "warning", "warning!!!")
    elif n == 4:
      mbox.critical(Form, "critical", "critical!!!")

btn1 = QtWidgets.QPushButton(Form)
btn1.move(10, 10)
btn1.setText("information")
btn1.clicked.connect(lambda: show(1))

btn2 = QtWidgets.QPushButton(Form)
btn2.move(10, 40)
btn2.setText("question")
btn2.clicked.connect(lambda: show(2))

btn3 = QtWidgets.QPushButton(Form)
btn3.move(10, 70)
btn3.setText("warning")
btn3.clicked.connect(lambda: show(3))

btn4 = QtWidgets.QPushButton(Form)
btn4.move(10, 100)
btn4.setText("critical")
btn4.clicked.connect(lambda: show(4))

Form.show()
sys.exit(app.exec_())


# 4.自訂 QMessageBox 對話視窗(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show():
    mbox = QtWidgets.QMessageBox(Form)
    mbox.setText("hello")   # 通知文字
    mbox.exec()             # 執行

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText("open")
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec_())


# 5.自訂 QMessageBox 對話視窗(2)
#           圖示	        代號	說明
# QMessageBox.Information	1	    資訊。
# QMessageBox.Warning	    2	    警告。
# QMessageBox.Critical	    3	    重要警告。
# QMessageBox.Question	    4	    問題。


# 6.自訂 QMessageBox 對話視窗(3)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show():
    mbox = QtWidgets.QMessageBox(Form)
    mbox.setText("hello?")
    mbox.setIcon(4)          # 加入問號 icon
    # mbox.setIcon(QtWidgets.QMessageBox.Question)  # 效果等同這一段
    mbox.exec()

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText("open")
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec_())


# 7.自訂 QMessageBox 按鈕(1)
#       按鈕	                呈現文字	        對應 ButtonRole
# QMessageBox.Ok	            Ok	                AcceptRole
# QMessageBox.Open	            Open	            AcceptRole
# QMessageBox.Save	            Save	            AcceptRole
# QMessageBox.Cancel	        Save	            RejectRole
# QMessageBox.Close	            Close	            RejectRole
# QMessageBox.Discard	        Don't Save	        DestructiveRole
# QMessageBox.Apply	            Apply	            AcceptRole
# QMessageBox.Reset	            Reset	            ResetRole
# QMessageBox.RestoreDefaults	Restore Defaults	ResetRole
# QMessageBox.Help	            Help	            HelpRole
# QMessageBox.SaveAll	        Save All	        AcceptRole
# QMessageBox.Yes	            Yes	                YesRole
# QMessageBox.YesToAll	        Yes to All	        YesRole
# QMessageBox.No	            No	                NoRole
# QMessageBox.NoToAll	        No to All	        NoRole
# QMessageBox.Abort	            Abort	            RejectRole
# QMessageBox.Retry	            Retry	            AcceptRole
# QMessageBox.Ignore	        Ignore	            AcceptRole
# QMessageBox.NoButton		                        停用 Button


# 8.自訂 QMessageBox 按鈕(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show():
    mbox = QtWidgets.QMessageBox(Form)
    mbox.setText("hello")
    mbox.addButton(QtWidgets.QMessageBox.Ok)
    mbox.addButton(QtWidgets.QMessageBox.Open)
    mbox.addButton(QtWidgets.QMessageBox.Save)
    mbox.addButton(QtWidgets.QMessageBox.Cancel)
    mbox.exec()

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText("open")
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec_())


# 9.自訂 QMessageBox 按鈕(3)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show():
    mbox = QtWidgets.QMessageBox(Form)
    mbox.setText("hello")
    # 添加三顆按鈕
    mbox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
    # 設定預設按鈕
    mbox.setDefaultButton(QtWidgets.QMessageBox.Yes)
    mbox.exec()

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText("open")
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec_())


# 10.自訂 QMessageBox 按鈕(4)
#           ButtonRole	                    代碼	說明
# QMessageBox.ButtonRole.InvalidRole	    -1	    按鈕無效。
# QMessageBox.ButtonRole.AcceptRole	        0	    接受。
# QMessageBox.ButtonRole.RejectRole	        1	    拒絕。
# QMessageBox.ButtonRole.DestructiveRole	2	    破壞性更改。
# QMessageBox.ButtonRole.ActionRole	        3	    發生行為。
# QMessageBox.ButtonRole.HelpRole	        4	    請求幫助。
# QMessageBox.ButtonRole.YesRole	        5	    等同「是」。
# QMessageBox.ButtonRole.NoRole	            6	    等同「否」。
# QMessageBox.ButtonRole.ApplyRole	        7	    同意。
# QMessageBox.ButtonRole.ResetRole	        8	    設為預設值。


# 11.自訂 QMessageBox 按鈕(5)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show():
    mbox = QtWidgets.QMessageBox(Form)
    mbox.setText("hello")
    mbox.addButton("Apple", 3)
    mbox.addButton("Banana", 3)
    mbox.addButton("Orange", 3)
    mbox.exec()

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText("open")
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec_())


# 12.自訂 QMessageBox 按鈕(6)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show():
    mbox = QtWidgets.QMessageBox(Form)
    mbox.setText("hello")
    a = mbox.addButton("Apple",3)   # 前方多了變數 a
    b = mbox.addButton("Banana",3)  # 前方多了變數 b
    c = mbox.addButton("Orange",3)  # 前方多了變數 c
    mbox.setDefaultButton(b)        # 預先選取 b
    mbox.exec()

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText("open")
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec_())


# 13.QMessageBox 點擊事件(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show():
    mbox = QtWidgets.QMessageBox(Form)
    mbox.setText("hello")
    mbox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
    mbox.setDefaultButton(QtWidgets.QMessageBox.Yes)
    ret = mbox.exec()                      # 取得點擊的按鈕數字
    if ret == QtWidgets.QMessageBox.Yes:
        print(1)
    elif ret == QtWidgets.QMessageBox.No:
        print(2)
    elif ret == QtWidgets.QMessageBox.Cancel:
        print(3)

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText("open")
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec_())


# 14.QMessageBox 點擊事件(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show():
    mbox = QtWidgets.QMessageBox(Form)
    mbox.setText("hello")
    a = mbox.addButton("Apple",3)   # 前方多了變數 a，順序 0
    b = mbox.addButton("Banana",3)  # 前方多了變數 b，順序 1
    c = mbox.addButton("Orange",3)  # 前方多了變數 c，順序 2
    mbox.setDefaultButton(b)        # 預先選取 b
    ret = mbox.exec()
    print(ret)
    if ret == 0:
        print("Apple")
    if ret == 1:
        print("Banana")
    if ret == 2:
        print("Orange")

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText("open")
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec_())


# 15.QMessageBox 點擊事件(3)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show():
    mbox = QtWidgets.QMessageBox(Form)
    mbox.setText("hello")
    a = mbox.addButton("Apple",3)   # 前方多了變數 a
    b = mbox.addButton("Banana",3)  # 前方多了變數 b
    c = mbox.addButton("Orange",3)  # 前方多了變數 c
    mbox.setDefaultButton(b)        # 預先選取 b
    mbox.exec()
    text = mbox.clickedButton().text()   # 取得點擊的按鈕文字
    if text == "Apple":
        print("Apple")
    if text == "Banana":
        print("Banana")
    if text == "Orange":
        print("Orange")

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText("open")
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec_())


# 16.QMessageBox 點擊事件(4)
from PyQt5 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)
        self.ui()

    def ui(self):
        btn = QtWidgets.QPushButton(self)
        btn.move(10, 10)
        btn.setText("open")
        btn.clicked.connect(self.showBox)

    def showBox(self):
        mbox = QtWidgets.QMessageBox(self)
        mbox.setText("hello")
        a = mbox.addButton("Apple",3)
        b = mbox.addButton("Banana",3)
        c = mbox.addButton("Orange",3)
        mbox.setDefaultButton(b)
        mbox.exec()
        text = mbox.clickedButton().text()
        if text == "Apple":
            print("Apple")
        if text == "Banana":
            print("Banana")
        if text == "Orange":
            print("Orange")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())