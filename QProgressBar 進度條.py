# 1.QProgressBar 進度條
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

bar = QtWidgets.QProgressBar(Form)
bar.move(20,20)
bar.setRange(0, 100)    # 進度條範圍
bar.setValue(50)        # 進度條預設值

Form.show()
sys.exit(app.exec_())


# 2.QProgressBar 樣式設定
from PyQt5 import QtWidgets, QtCore
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

bar1 = QtWidgets.QProgressBar(Form)
bar1.move(20,20)
bar1.setRange(0, 100)
bar1.setValue(50)
bar1.setStyleSheet('''
    QProgressBar {
        border: 2px solid #000;
        border-radius: 5px;
        text-align:center;
        height: 50px;
        width:80px;
    }
    QProgressBar::chunk {
        background: #09c;
        width:1px;
    }
''')

bar2 = QtWidgets.QProgressBar(Form)
bar2.move(120,20)
bar2.setRange(0, 100)
bar2.setValue(50)
bar2.setStyleSheet('''
    QProgressBar {
        border: 2px solid #000;
        text-align:center;
        background:#aaa;
        color:#fff;
        height: 15px;
        border-radius: 8px;
        width:150px;
    }
    QProgressBar::chunk {
        background: #333;
        width:1px;
    }
''')

Form.show()
sys.exit(app.exec_())


# 3.QProgressBar 進度文字設定(1)
# 顯示格式	  說明
#   %p	    百分比
#   %v	    目前數值
#   %m	    總數值


# 4.QProgressBar 進度文字設定(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

style = '''
    QProgressBar {
        border: 2px solid #000;
        border-radius: 5px;
        text-align:center;
        height: 20px;
        width:200px;
    }
    QProgressBar::chunk {
        background: #09c;
        width:1px;
    }
'''

bar1 = QtWidgets.QProgressBar(Form)
bar1.move(20,20)
bar1.setRange(0, 200)
bar1.setValue(50)
bar1.setStyleSheet(style)
bar1.setFormat("%v / %m")

bar2 = QtWidgets.QProgressBar(Form)
bar2.move(20,60)
bar2.setRange(0, 200)
bar2.setValue(50)
bar2.setStyleSheet(style)
bar2.setFormat("%p%")

bar3 = QtWidgets.QProgressBar(Form)
bar3.move(20,100)
bar3.setRange(0, 200)
bar3.setValue(50)
bar3.setStyleSheet(style)
bar3.setFormat("%v")

Form.show()
sys.exit(app.exec_())


# 5.QProgressBar 常用方法(1)
# 方法	            參數	    說明
# setValue()	    int	    設定進度。
# setRange()	  min, max	設定進度範圍。
# setFormat()	   format	設定進度文字格式。
# reset()		            重設進度條數值。


# 6.QProgressBar 常用方法(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

style = '''
    QProgressBar {
        border: 2px solid #000;
        border-radius: 5px;
        text-align:center;
        height: 20px;
        width:200px;
    }
    QProgressBar::chunk {
        background: #09c;
        width:1px;
    }
'''

bar = QtWidgets.QProgressBar(Form)
bar.move(20,20)
bar.setRange(0, 0)       # 兩個數值設定相同
bar.setValue(50)
bar.setStyleSheet(style)

Form.show()
sys.exit(app.exec_())


# 7.點擊按鈕增加進度(1)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

style = '''
    QProgressBar {
        border: 2px solid #000;
        border-radius: 5px;
        text-align:center;
        height: 20px;
        width:200px;
    }
    QProgressBar::chunk {
        background: #09c;
        width:1px;
    }
'''

bar = QtWidgets.QProgressBar(Form)
bar.move(20,20)
bar.setRange(0, 200)
bar.setValue(0)
bar.setStyleSheet(style)

n = 0
def more():
    global n
    n = n + 10
    bar.setValue(n)      # 增加進度

def reset():
    global n
    n = 0
    bar.reset()          # 重設進度

btn1 = QtWidgets.QPushButton(Form)   # 增加進度按鈕
btn1.move(20,60)
btn1.setText("增加進度")
btn1.clicked.connect(more)

btn2 = QtWidgets.QPushButton(Form)   # 重設進度按鈕
btn2.move(110,60)
btn2.setText("重設")
btn2.clicked.connect(reset)


Form.show()
sys.exit(app.exec_())


# 8.點擊按鈕增加進度(2)
from PyQt5 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 200)
        self.n = 0
        self.ui()

    def ui(self):
        style = '''
            QProgressBar {
                border: 2px solid #000;
                border-radius: 5px;
                text-align:center;
                height: 20px;
                width:200px;
            }
            QProgressBar::chunk {
                background: #09c;
                width:1px;
            }
        '''

        self.bar = QtWidgets.QProgressBar(self)
        self.bar.move(20,20)
        self.bar.setRange(0, 200)
        self.bar.setValue(0)
        self.bar.setStyleSheet(style)

        self.btn1 = QtWidgets.QPushButton(self)   # 增加進度按鈕
        self.btn1.move(20,60)
        self.btn1.setText("增加進度")
        self.btn1.clicked.connect(self.more)

        self.btn2 = QtWidgets.QPushButton(self)   # 重設進度按鈕
        self.btn2.move(110,60)
        self.btn2.setText("重設")
        self.btn2.clicked.connect(self.reset)

    def showMsg(self):
        self.label.setText(str(self.slider.value()))

    def more(self):
        self.n = self.n + 10
        self.bar.setValue(self.n)      # 增加進度

    def reset(self):
        self.n = 0
        self.bar.reset()          # 重設進度

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())
