# 1.QLabel + QPixmap(1)
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

label = QtWidgets.QLabel(MainWindow)    # 放入 QLabel
label.setGeometry(0, 0, 300, 200)       # 設定 QLabel 尺寸和位置

qpixmap = QPixmap()                     # 建立 QPixmap 物件
qpixmap.load("mona.jpg")                # 讀取圖片
# 也可以寫成下面這樣
# qpixmap = QPixmap("mona.jpg")
label.setPixmap(qpixmap)                # 將 QPixmap 物件加入到 label 裡

MainWindow.show()
sys.exit(app.exec_())


# 2.QLabel + QPixmap(2)
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

label = QtWidgets.QLabel(MainWindow)
label.setGeometry(0, 0, 300, 200)

qpixmap = QPixmap()
qimg = QImage("mona.jpg")            # 讀取圖片
qpixmap = qpixmap.fromImage(qimg)    # 將圖片加入 QPixmap 物件中
label.setPixmap(qpixmap)             # 將 QPixmap 物件加入到 label 裡
MainWindow.show()
sys.exit(app.exec_())


# 3.QLabel + QPixmap(3)
# 一個 QLabel 裡只能存在一個 QPixmap 物件，因此如果要放入兩張圖片，需要使用兩個 QLabel。
# 如果要調整圖片位置，可使用 QLabel 的 move 方法進行調整。
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

label = QtWidgets.QLabel(MainWindow)  #  建立 QLabel
label.setGeometry(0, 0, 300, 200)
label2 = QtWidgets.QLabel(MainWindow) #  建立 QLabel
label2.setGeometry(0, 0, 300, 200)
label2.move(0, -50)                   # 調整位置

qpixmap = QPixmap()
qpixmap.load("mona.jpg")
img1 = qpixmap.scaled(300,50)    # 建立圖片 1
label.setPixmap(img1)            # 加入圖片 1
img2 = qpixmap.scaled(150,200)   # 建立圖片 2
label2.setPixmap(img2)           # 加入圖片 2
MainWindow.show()
sys.exit(app.exec_())


# 4.使用 QGraphicsView + QPixmap(1)
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
img = QPixmap("mona.jpg")                     # 加入圖片
scene.addPixmap(img)                          # 將圖片加入 scene
grview.setScene(scene)                        # 設定 QGraphicsView 的場景為 scene

MainWindow.show()
sys.exit(app.exec_())


# 5.使用 QGraphicsView + QPixmap(2)
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 300)

grview = QtWidgets.QGraphicsView(MainWindow)
gw = 300
gh = 300
grview.setGeometry(0, 0, gw, gh)      # QGraphicsView 的長寬改成變數
scene = QtWidgets.QGraphicsScene()
img = QPixmap("mona.jpg")
img_w = 120                           # 顯示圖片的寬度
img_h = 160                           # 顯示圖片的高度
img = img.scaled(img_w, img_h)        # 改變圖片尺寸
x = 20                                # 左上角 x 座標
y = 20                                # 左上角 y 座標
dx = int((gw - img_w) / 2) - x        # 修正公式
dy = int((gh - img_h) / 2) - y
scene.setSceneRect(dx, dy, img_w, img_h)
scene.addPixmap(img)
grview.setScene(scene)

MainWindow.show()
sys.exit(app.exec_())


# 6.使用 QGraphicsView + QPixmap(3)
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
