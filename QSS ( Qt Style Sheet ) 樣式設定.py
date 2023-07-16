# 1.QSS
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(10,10,150,100)
label.setText("HELLO")
label.setStyleSheet('''
        font-size:30px;
        color:red;
    ''')

Form.show()
sys.exit(app.exec_())


# 2.常用樣式設定
#   樣式	            說明
# font-size	        文字大小，單位 px。
# color	            文字顏色，可使用顏色名稱或色碼，例如 #f00 為紅色。
# font-family	    字體。
# font-weight	    字體粗細，可設定 normal、bold。
# font-style	    文字樣式，可設定 normal、italic、oblique。
# spacing	        文字間距，不用單位。
# text-align	    文字對齊方式，可設定 left、center、right。
# height	        元件高度，單位 px。
# width	            元件寬度，單位 px。
# margin	        元件外邊距，單位 px。
# padding	        元件內邊距，單位 px。
# opacity	        透明度，範圍 0～255，0 為透明。
# background	    背景色或背景圖，可使用顏色名稱或色碼，例如 #f00 為紅色。
# background-color	背景色，可使用顏色名稱或色碼，例如 #f00 為紅色。
# border	        邊框，有三個值分別是 ( 粗細、樣式、顏色 )。
# border-width	    邊框寬度，單位 px。
# border-style	    邊框樣式，可設定 solid、dashed、dotted。
# border-color	    邊框顏色，可使用顏色名稱或色碼，例如 #f00 為紅色。
# border-radius	    邊框是否圓角，圓角半徑單位 px。

#       寫法	                說明
# padding:1px	            上下左右都 1px。
# padding:1px 2px	        上下 1px，左右 2px。
# padding:1px 2px 3px	    上 1px，左右 2px，下 3px。
# padding:1px 2px 3px 4px	上 1px，右 2px，下 3px，左 4px。

#       樣式	            說明
# padding-top	    元件上方內邊距，單位 px。
# padding-right	    元件右側內邊距，單位 px。
# padding-bottom	元件下方內邊距，單位 px。
# padding-left	    元件左側內邊距，單位 px。


# 3.偽狀態設定(1)
# 偽狀態	        說明
# :hover	    滑鼠移上去。
# :active	    發生行為 ( 通常可能是點擊 )。
# :focus	    成為焦點 ( 通常是點擊之後 )。
# :checked	    被勾選。
# :disabled	    停用狀態。
# :enabled	    啟用狀態。
# :selected	    被選取。


# 4.偽狀態設定(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

btn = QtWidgets.QPushButton(Form)
btn.setGeometry(10,10,150,100)
btn.setText("HELLO")
btn.setStyleSheet('''
    QPushButton{
        border:1px solid #000;
        background:#fff;
    }
    QPushButton:hover{
        border:5px solid #000;
        background:#ff0;
    }
''')

Form.show()
sys.exit(app.exec_())


# 5.子控制項設定(1)
# 子控制項	        說明
# ::chunk	    進度條進度。
# ::item	    列表選擇框項目。
# ::groove	    滑桿底線。
# ::handle	    滑桿拉霸。
# ::sub-page	滑桿調整線。


# 6.子控制項設定(2)
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

slider = QtWidgets.QSlider(Form)
slider.setGeometry(20,20,200,30)
slider.setOrientation(1)
slider.setStyleSheet('''
    QSlider {
        border-radius: 10px;
    }
    QSlider::groove:horizontal {
        height: 5px;
        background: #000;
    }
    QSlider::handle:horizontal{
        background: #f00;
        width: 16px;
        height: 16px;
        margin:-6px 0;
        border-radius:8px;
    }
    QSlider::sub-page:horizontal{
        background:#f90;
    }
''')

Form.show()
sys.exit(app.exec_())


# 7.注意事項
# 雖然使用 QSS 可以很方便的修改樣式，但仍然有些小細節需要注意，例如 QPushButton，一旦設定了「邊框」，則必須要一併設定背景色和點擊樣式，不然其他樣式就會被清空。
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("oxxo.studio")
Form.resize(300, 200)

btn = QtWidgets.QPushButton(Form)
btn.setGeometry(10,10,150,100)
btn.setText("HELLO")
btn.setStyleSheet("border:1px solid #000")

Form.show()
sys.exit(app.exec_())








