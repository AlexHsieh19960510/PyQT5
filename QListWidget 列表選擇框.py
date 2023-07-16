# 1.QListWidget 和 QListView 的差異
from PyQt5 import QtWidgets, QtCore
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

# 使用 QListView
listview = QtWidgets.QListView(Form)
listview.setGeometry(10,10,120,100)
model = QtCore.QStringListModel()
model.setStringList(["A","B","C","D"])  # 使用 QtCore.QStringListModel() 建立選單
listview.setModel(model)

# 使用 QListWidget
listwidget = QtWidgets.QListWidget(Form)
listwidget.setGeometry(140,10,120,100)
listwidget.addItems(["A","B","C","D"])  # 使用 addItems 建立選單

Form.show()
sys.exit(app.exec_())


# 2.加入 QListWidget 列表選擇框
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

listwidget = QtWidgets.QListWidget(Form)  # 建立列表選擇框元件
listwidget.addItems(["A","B","C","D"])    # 建立選單
listwidget.setGeometry(10,10,120,100)    # 設定位置

Form.show()
sys.exit(app.exec_())


# 3.QListWidget 刪除選項
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

listwidget = QtWidgets.QListWidget(Form)
listwidget.addItems(["A","B","C","D"])
listwidget.setGeometry(10,10,120,100)
item = listwidget.takeItem(1)       # 取得第二個項目，也就是 B
listwidget.removeItemWidget(item)   # 移除第二個項目

Form.show()
sys.exit(app.exec_())


# 4.QListWidget 添加選項
from PyQt5 import QtWidgets, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def create_item(text, img):
    item = QtWidgets.QListWidgetItem()      # 建立清單項目
    item.setText(text)                      # 項目文字
    item.setIcon(QtGui.QIcon(img))          # 項目圖片
    return item                             # 返回清單項目

listwidget = QtWidgets.QListWidget(Form)
listwidget.addItems(["A","B","C","D"])
listwidget.setGeometry(10,10,120,120)
listwidget.addItem("X")                         # 添加純文字項目
listwidget.addItem(create_item("", "icon.png")) # 添加使用函式創造的選項

listwidget.insertItem(0, "Y")                          # 添加純文字項目
listwidget.insertItem(0, create_item("", "mona.jpg"))  # 添加使用函式創造的選項

Form.show()
sys.exit(app.exec_())


# 5.QListWidget 修改選項
from PyQt5 import QtWidgets, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

listwidget = QtWidgets.QListWidget(Form)
listwidget.addItems(["A","B","C","D"])
listwidget.setGeometry(10,10,120,100)
item = listwidget.item(1)                # 取得第二個項目 ( 第一個為 0 )
item.setText("ok")                       # 設定文字為 ok
item.setIcon(QtGui.QIcon("icon.png"))    # 設定 icon

Form.show()
sys.exit(app.exec_())


# 6.QListWidget 樣式設定
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

def show():
    print(listwidget.currentItem().text(), listwidget.currentIndex().row())

def create_item(text):
    item = QtWidgets.QListWidgetItem(listwidget)
    item.setText(text)
    item.setIcon(QtGui.QIcon("icon.png"))
    return item

listwidget = QtWidgets.QListWidget(Form)
listwidget.addItems(["A","B","C","D"])
listwidget.setGeometry(10,10,200,50)
listwidget.addItem(create_item(""))
listwidget.setFlow(QtWidgets.QListView.LeftToRight)  # 改成水平顯示
listwidget.setStyleSheet('''
    QListWidget{
        color:#00f;
    }
    QListWidget::item{
        width:30px;
    }
    QListWidget::item:selected{
        color:#f00;
        background:#000;
    }
''')

Form.show()
sys.exit(app.exec_())


# 7.QListWidget 常用方法
# 方法	                    參數	    說明
# item()	                index	取得指定的項目。
# addItem()	                str	    增加單一個項目。
# addItems()	            list	以串列方式增加多個項目。
# takeItem()	            index	取得並移除指定項目。
# removeItemWidget()	    item	移除指定項目。
# clear()		                    清空所有項目。
# setFlow()	                type	設定排列方式，預設 QtWidgets.QListView.TopToBottom 從上而下，QtWidgets.QListView.LeftToRight 從左到右。
# setDisabled()	            bool	設定是否禁用，預設 False。
# clicked.connect()	        fn	    點擊項目時時要執行的函式。
# text()		                    取得輸入框內容。
# currentItem().text()		        點擊項目的文字。
# currentIndex().row()		        點擊項目的列數 ( 垂直 )。
# currentIndex().column()		    點擊項目的欄數 ( 水平 )。

# 方法	            參數	            說明
# setText()	        str	            設定項目的文字內容。
# setIcon() 	QtGui.QIcon(path)	設定項目的圖片。
# setSelected()	    bool	        設定是否選取，預設 False。
# text()		                    項目的文字內容。


# 8.顯示 QListWidget 選擇項目(1)
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(10,10,120,30)

def show():
    text = listwidget.currentItem().text()  # 取得項目文字
    num = listwidget.currentIndex().row()   # 取得項目編號
    label.setText(f"{num}:{text}")          # 顯示文字

listwidget = QtWidgets.QListWidget(Form)
listwidget.addItems(["A","B","C","D"])
listwidget.setGeometry(10,50,120,50)
listwidget.setFlow(QtWidgets.QListView.LeftToRight)
listwidget.setStyleSheet('''
    QListWidget::item{
        font-size:20px;
    }
    QListWidget::item:selected{
        color:#f00;
        background:#000;
    }
''')
listwidget.clicked.connect(show)         # 點擊項目時執行函式

Form.show()
sys.exit(app.exec_())


# 9.顯示 QListWidget 選擇項目(2)
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
        self.label.setGeometry(10,10,120,30)
        self.listwidget = QtWidgets.QListWidget(self)
        self.listwidget.addItems(["A","B","C","D"])
        self.listwidget.setGeometry(10,50,120,50)
        self.listwidget.setFlow(QtWidgets.QListView.LeftToRight)
        self.listwidget.setStyleSheet('''
            QListWidget::item{
                font-size:20px;
            }
            QListWidget::item:selected{
                color:#f00;
                background:#000;
            }
        ''')
        self.listwidget.clicked.connect(self.showMsg)         # 點擊項目時執行函式

    def showMsg(self):
        text = self.listwidget.currentItem().text()  # 取得項目文字
        num = self.listwidget.currentIndex().row()   # 取得項目編號
        self.label.setText(f"{num}:{text}")          # 顯示文字

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())
