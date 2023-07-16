# 1.QGraphicsView 顯示圖片
from PyQt5 import QtWidgets, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 300)

grview = QtWidgets.QGraphicsView(Form)  # 加入 QGraphicsView
grview.setGeometry(20, 20, 260, 200)    # 設定 QGraphicsView 位置與大小
scene = QtWidgets.QGraphicsScene()      # 加入 QGraphicsScene
scene.setSceneRect(0, 0, 300, 400)      # 設定 QGraphicsScene 位置與大小
img = QtGui.QPixmap("mona.jpg")         # 加入圖片
scene.addPixmap(img)                    # 將圖片加入 scene
grview.setScene(scene)                  # 設定 QGraphicsView 的場景為 scene

Form.show()
sys.exit(app.exec_())


# 2.改變圖片尺寸
from PyQt5 import QtWidgets, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 300)                    # 視窗大小

grview = QtWidgets.QGraphicsView(Form)
grview.setGeometry(20, 20, 260, 200)     # QGraphicsView 位置 (20, 20) 和大小 260x200
scene = QtWidgets.QGraphicsScene()
scene.setSceneRect(0, 0, 120, 160)       # QGraphicsScene 相對位置 (20, 20) 和大小 120x160
img = QtGui.QPixmap("mona.jpg")
img = img.scaled(120,160)                # 調整圖片大小為 120x160
scene.addPixmap(img)
grview.setScene(scene)

Form.show()
sys.exit(app.exec_())


# 3.設定圖片位置(1)
from PyQt5 import QtWidgets, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 300)

grview = QtWidgets.QGraphicsView(Form)
gw = 260
gh = 200
grview.setGeometry(20, 20, gw, gh)    # QGraphicsView 的長寬改成變數
scene = QtWidgets.QGraphicsScene()
img = QtGui.QPixmap("mona.jpg")
img_w = 120                           # 顯示圖片的寬度
img_h = 160                           # 顯示圖片的高度
img = img.scaled(img_w, img_h)
x = 20                                # 左上角 x 座標
y = 20                                # 左上角 y 座標
dx = int((gw - img_w) / 2) - x        # 修正公式
dy = int((gh - img_h) / 2) - y
scene.setSceneRect(dx, dy, img_w, img_h)
scene.addPixmap(img)
grview.setScene(scene)

Form.show()
sys.exit(app.exec_())


# 4.設定圖片位置(2)
from PyQt5 import QtWidgets, QtGui
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("oxxo.studio")
        self.resize(300, 300)
        self.ui()

    def ui(self):
        grview = QtWidgets.QGraphicsView(self)
        gw = 260
        gh = 200
        grview.setGeometry(20, 20, gw, gh)    # QGraphicsView 的長寬改成變數
        scene = QtWidgets.QGraphicsScene()
        img = QtGui.QPixmap("mona.jpg")
        img_w = 120                           # 顯示圖片的寬度
        img_h = 160                           # 顯示圖片的高度
        img = img.scaled(img_w, img_h)
        x = 20                                # 左上角 x 座標
        y = 20                                # 左上角 y 座標
        dx = int((gw - img_w) / 2) - x        # 修正公式
        dy = int((gh - img_h) / 2) - y
        scene.setSceneRect(dx, dy, img_w, img_h)
        scene.addPixmap(img)
        grview.setScene(scene)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
sys.exit(app.exec_())


# 5.顯示多張圖片
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 300)

grview = QtWidgets.QGraphicsView(MainWindow)  # 加入 QGraphicsView
grview.setGeometry(0, 0, 300, 300)            # 設定 QGraphicsView 位置與大小
scene = QtWidgets.QGraphicsScene()            # 加入 QGraphicsScene
scene.setSceneRect(0, 0, 200, 200)            # 設定 QGraphicsScene 位置與大小
img = QPixmap("mona.jpg")                     # 建立圖片
img1 = img.scaled(200,50)                     # 建立不同尺寸圖片
qitem1 = QtWidgets.QGraphicsPixmapItem(img1)  # 設定 QItem，內容是 img1
img2 = img.scaled(100,150)                    # 建立不同尺寸圖片
qitem2 = QtWidgets.QGraphicsPixmapItem(img2)  # 設定 QItem，內容是 img2
scene.addItem(qitem1)                         # 場景中加入 QItem
scene.addItem(qitem2)                         # 場景中加入 QItem
grview.setScene(scene)                        # 設定 QGraphicsView 的場景為 scene

MainWindow.show()
sys.exit(app.exec_())
