# 1.QThread(1)
from PyQt5 import QtWidgets
import sys, time

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label_a = QtWidgets.QLabel(Form)      # 第一個 QLabel
label_a.setGeometry(10, 10, 100, 30)

label_b = QtWidgets.QLabel(Form)      # 第二個 QLabel
label_b.setGeometry(10, 50, 100, 30)

def a():
    for i in range(0,5):
        label_a.setText(str(i))      # 每次迴圈執行時設定文字
        print("A:",i)
        time.sleep(0.5)              # 等待 0.5 秒

def b():
    for i in range(0,50,10):
        label_b.setText(str(i))      # 每次迴圈執行時設定文字
        print("B:",i)
        time.sleep(0.5)              # 等待 0.5 秒

a()          # 執行 a()
b()          # 執行 a()

Form.show()  # 顯示主視窗
sys.exit(app.exec_())


# 2.QThread(2)
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
import sys, time

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label_a = QtWidgets.QLabel(Form)
label_a.setGeometry(10, 10, 100, 30)

label_b = QtWidgets.QLabel(Form)
label_b.setGeometry(10, 50, 100, 30)

def a():
    for i in range(0,5):
        label_a.setText(str(i))
        print("A:",i)
        time.sleep(0.5)

def b():
    for i in range(0,50,10):
        label_b.setText(str(i))
        print("B:",i)
        time.sleep(0.5)

thread_a = QThread()   # 建立 Thread()
thread_a.run = a       # 設定該執行緒執行 a()
thread_a.start()       # 啟動執行緒

thread_b = QThread()   # 建立 Thread()
thread_b.run = b       # 設定該執行緒執行 b()
thread_b.start()       # 啟動執行緒

Form.show()
sys.exit(app.exec_())


# 3.QThread 常用方法(1)
# 方法	    參數	    說明
# start()		    啟動執行緒。
# wait()		    等待該執行緒結束。
# sleep()	sec	    等待該執行緒幾秒。


# 4.QThread 常用方法(2)
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
import sys, time

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label_a = QtWidgets.QLabel(Form)
label_a.setGeometry(10, 10, 100, 30)

label_b = QtWidgets.QLabel(Form)
label_b.setGeometry(10, 50, 100, 30)

def a():
    for i in range(0,5):
        label_a.setText(str(i))
        print("A:",i)
        time.sleep(0.5)

def b():
    thread_a.wait()             # 使用 wait
    for i in range(0,50,10):
        label_b.setText(str(i))
        print("B:",i)
        time.sleep(0.5)

thread_a = QThread()   # 建立 Thread()
thread_a.run = a       # 設定該執行緒執行 a()
thread_a.start()       # 啟動執行緒

thread_b = QThread()   # 建立 Thread()
thread_b.run = b       # 設定該執行緒執行 b()
thread_b.start()       # 啟動執行緒

Form.show()
sys.exit(app.exec_())


# 5.QThread 常用方法(3)
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
import sys, time

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label_a = QtWidgets.QLabel(Form)
label_a.setGeometry(10, 10, 100, 30)

label_b = QtWidgets.QLabel(Form)
label_b.setGeometry(10, 50, 100, 30)

def a():
    for i in range(0,5):
        label_a.setText(str(i))
        print("A:",i)
        time.sleep(0.5)

def b():
    thread_a.sleep(1)             # 使用 sleep
    for i in range(0,50,10):
        label_b.setText(str(i))
        print("B:",i)
        time.sleep(0.5)

thread_a = QThread()   # 建立 Thread()
thread_a.run = a       # 設定該執行緒執行 a()
thread_a.start()       # 啟動執行緒

thread_b = QThread()   # 建立 Thread()
thread_b.run = b       # 設定該執行緒執行 b()
thread_b.start()       # 啟動執行緒

Form.show()
sys.exit(app.exec_())


# 6.QThread 搭配 threading Event(1)
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
import sys, time, threading

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label_a = QtWidgets.QLabel(Form)
label_a.setGeometry(10, 10, 100, 30)

label_b = QtWidgets.QLabel(Form)
label_b.setGeometry(10, 50, 100, 30)

event = threading.Event()    # 建立事件

def a():
    event.wait()             # 等待事件被觸發
    for i in range(0,5):
        label_a.setText(str(i))
        print("A:",i)
        time.sleep(0.5)

def b():
    for i in range(0,50,10):
        if i > 20:
            event.set()      # 觸發事件
        label_b.setText(str(i))
        print("B:",i)
        time.sleep(0.5)

thread_a = QThread()
thread_a.run = a
thread_a.start()

thread_b = QThread()
thread_b.run = b
thread_b.start()

Form.show()
sys.exit(app.exec_())


# 7.QThread 搭配 threading Event(2)
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
import sys, time, threading

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)
        self.event = threading.Event()
        self.ui()
        self.run()

    def ui(self):
        self.label_a = QtWidgets.QLabel(self)
        self.label_a.setGeometry(10, 10, 100, 30)

        self.label_b = QtWidgets.QLabel(self)
        self.label_b.setGeometry(10, 50, 100, 30)

    def a(self):
        self.event.wait()             # 等待事件被觸發
        for i in range(0,5):
            self.label_a.setText(str(i))
            print("A:",i)
            time.sleep(0.5)

    def b(self):
        for i in range(0,50,10):
            if i > 20:
                self.event.set()      # 觸發事件
            self.label_b.setText(str(i))
            print("B:",i)
            time.sleep(0.5)

    def run(self):
        self.thread_a = QThread()
        self.thread_a.run = self.a
        self.thread_a.start()

        self.thread_b = QThread()
        self.thread_b.run = self.b
        self.thread_b.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())


# 8.使用 threading + PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
import sys, time, threading

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label_a = QtWidgets.QLabel(Form)
label_a.setGeometry(10, 10, 100, 30)

label_b = QtWidgets.QLabel(Form)
label_b.setGeometry(10, 50, 100, 30)

def a():
    for i in range(1,6):
        label_a.setText(str(i))
        print("A:",i)
        time.sleep(0.5)

def b():
    for i in range(10,60,10):
        label_b.setText(str(i))
        print("B:",i)
        time.sleep(0.5)

thread_a = threading.Thread(target=a)   # 建立執行緒，執行 a 函式
thread_b = threading.Thread(target=b)   # 建立執行緒，執行 b 函式

thread_a.start()   # 啟動執行緒
thread_b.start()   # 啟動執行緒

Form.show()
sys.exit(app.exec_())





















