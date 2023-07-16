# 1.安裝 Matplotlib 和 NumPy 函式庫
pip install matplotlib
pip install numpy


# 2.Matplotlib 顯示正弦波形
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (3,2), dpi = 150)
ax = plt.axes(xlim = (0, 2), ylim = (-2, 2))
line, = ax.plot([], [])
line.set_data([], [])
x = np.linspace(0, 2, 100)
y = np.sin(5 * np.pi * x)
line.set_data(x, y)

plt.show()


# 3.PyQt5 顯示 Matplotlib 圖表
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Qt5Agg")  # 使用 Qt5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# 建立正弦波繪圖函式
def sinWave(i=0):
    fig = plt.figure(figsize = (3,2), dpi = 100)
    ax = plt.axes(xlim = (0, 2), ylim = (-2, 2))
    line, = ax.plot([], [])
    line.set_data([], [])
    x = np.linspace(0, 2, 100)
    y = np.sin(5 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return fig

canvas = FigureCanvas(sinWave())  # 將圖表繪製在 FigureCanvas 裡

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(360, 240)

graphicview = QtWidgets.QGraphicsView(MainWindow)  # 建立顯示圖片元件
graphicview.setGeometry(0, 0, 360, 240)

graphicscene = QtWidgets.QGraphicsScene()   # 建立場景
graphicscene.setSceneRect(0, 0, 340, 220)
graphicscene.addWidget(canvas)              # 場景中放入圖表

graphicview.setScene(graphicscene)          # 元件中放入場景

MainWindow.show()
sys.exit(app.exec_())


# 4.PyQt5 顯示 Matplotlib 圖表動畫(1)
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
matplotlib.use("Qt5Agg")      # 表示使用 Qt5

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

def sinWave(i = 0):
    plt.close()     # 執行時先刪除已有的 plt
    fig = plt.figure(figsize = (3,2), dpi = 100)
    ax = plt.axes(xlim = (0, 2), ylim = (-2, 2))
    line, = ax.plot([], [])
    line.set_data([], [])
    x = np.linspace(0, 2, 100)
    y = np.sin(5 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return fig

canvas = FigureCanvas(sinWave())

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(360, 240)

graphicview = QtWidgets.QGraphicsView(MainWindow)
graphicview.setGeometry(0, 0, 360, 240)

graphicscene = QtWidgets.QGraphicsScene()
graphicscene.setSceneRect(0, 0, 340, 220)
graphicscene.addWidget(canvas)

graphicview.setScene(graphicscene)

dx = 0   # x 位移初始值

def count():
    global dx, canvas
    dx = dx + 5                         # 每次定時器執行位移 5
    canvas = FigureCanvas(sinWave(dx))  # 產生新的正弦波圖形
    graphicscene.clear()                # 清空場景
    graphicscene.addWidget(canvas)      # 場景放入圖形

timer = QTimer()                        # 加入定時器
timer.timeout.connect(count)            # 設定定時要執行的 function
timer.start(50)                         # 啟用定時器，設定間隔時間為 500 毫秒

MainWindow.show()
sys.exit(app.exec_())


# 5.PyQt5 顯示 Matplotlib 圖表動畫(2)
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(360, 240)
        self.t = 0
        self.ui()

    def ui(self):
        self.canvas = FigureCanvas(self.sinWave())

        self.graphicview = QtWidgets.QGraphicsView(self)
        self.graphicview.setGeometry(0, 0, 360, 240)

        self.graphicscene = QtWidgets.QGraphicsScene()
        self.graphicscene.setSceneRect(0, 0, 340, 220)
        self.graphicscene.addWidget(self.canvas)

        self.graphicview.setScene(self.graphicscene)

    def sinWave(self, i = 0):
        fig = plt.figure(figsize = (3,2), dpi = 100)
        ax = plt.axes(xlim = (0, 2), ylim = (-2, 2))
        line, = ax.plot([], [])
        line.set_data([], [])
        x = np.linspace(0, 2, 100)
        y = np.sin(5 * np.pi * (x - 0.01 * i))
        line.set_data(x, y)
        plt.close()
        return fig

    def count(self):
        self.t = self.t + 5
        self.canvas = FigureCanvas(self.sinWave(self.t))
        self.graphicscene.clear()
        self.graphicscene.addWidget(self.canvas)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()

    timer = QTimer()                    # 加入定時器
    timer.timeout.connect(Form.count)   # 設定定時要執行的 function
    timer.start(50)                     # 啟用定時器，設定間隔時間為 500 毫秒
    sys.exit(app.exec_())



















