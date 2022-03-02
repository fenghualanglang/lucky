# coding:utf-8
# 州的先生
# https://zmister.com
# PyQt5界面美化

import sys
import qtawesome
from PyQt5.Qt import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtWebEngineWidgets import QWebEngineView



class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(1640,900)
        # self.setFixedSize(960,700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_layout.setContentsMargins(0, 0, 0, 0)  # 设置主网格布局层的margin边距
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_layout.setContentsMargins(0,0,0,0) # 设置左侧网格布局层的margin边距
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格
        # ----self.left_widget.setStyleSheet('''QPushButton{border:none;color:white;}''') # 设置左侧部件的样式
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.left_close = QtWidgets.QPushButton("") # 关闭按钮
        self.left_close.clicked.connect(self.close) # 绑定窗口关闭槽
        self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小
        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')

        self.left_visit = QtWidgets.QPushButton("") # 空白按钮
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')

        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.left_mini.clicked.connect(self.showMinimized) # 绑定窗口最小化槽
        self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_label_1 = QtWidgets.QPushButton("国家相关")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("历史相关")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.music',color='white'),"最佳动态")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy',color='white'),"路线动画")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.film',color='white'), "中国市县")  # https://fontawesome.com/v5.15/icons?d=gallery&p=2&q=download&m=free
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.home',color='white'), "地点查绘")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.download',color='white'), "历史查询")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.heart',color='white'), "历史疆域")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment',color='white'),"反馈建议")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star',color='white'),"关注我们")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question',color='white'),"遇到问题")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1,1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0,1,3)
        self.left_layout.addWidget(self.left_button_2, 3, 0,1,3)
        self.left_layout.addWidget(self.left_button_3, 4, 0,1,3)
        self.left_layout.addWidget(self.left_label_2, 5, 0,1,3)
        self.left_layout.addWidget(self.left_button_4, 6, 0,1,3)
        self.left_layout.addWidget(self.left_button_5, 7, 0,1,3)
        self.left_layout.addWidget(self.left_button_6, 8, 0,1,3)
        self.left_layout.addWidget(self.left_label_3, 9, 0,1,3)
        self.left_layout.addWidget(self.left_button_7, 10, 0,1,3)
        self.left_layout.addWidget(self.left_button_8, 11, 0,1,3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        # ----self.left_layout.setAlignment(QtCore.Qt.AlignTop) # 设置左侧网格布局层按顶部排列

        # -------主函数--------------------------------------------------------------------------------
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2) # 左侧部件在第0行第0列，占8行3列
        self.setCentralWidget(self.main_widget) # 设置窗口主部件
        self.setWindowOpacity(0.9) # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框

        self.left_button_2.pressed.connect(self.left_button_2_ui)
        self.left_button_3.pressed.connect(self.left_button_3_ui)


    def left_button_2_ui(self):
        print("在线FM 被点击啦...")
        self.right_widget_2 = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget_2.setObjectName('right_widget')
        self.right_layout_2 = QtWidgets.QGridLayout()
        #---- self.right_layout.setContentsMargins(50,0,0,0) # 设置外边框 距离
        self.right_widget_2.setLayout(self.right_layout_2) # 设置右侧部件布局为网格
        self.right_widget_2.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')
        self.right_bar_widget_2 = QtWidgets.QWidget() # 右侧顶部搜索框部件
        self.right_bar_layout_2 = QtWidgets.QGridLayout() # 右侧顶部搜索框网格布局
        self.right_bar_widget_2.setLayout(self.right_bar_layout_2)
        self.search_icon_2 = QtWidgets.QLabel(chr(0xf002) + ' '+'搜索  ')
        self.search_icon_2.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input_2 = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input_2.setPlaceholderText("输入歌手、歌曲或用户，回车进行搜索")
        self.right_bar_widget_search_input_2.setStyleSheet("QLineEdit{border:1px solid gray;width:300px;border-radius:10px;padding:2px 4px;}")
        self.right_bar_layout_2.addWidget(self.search_icon_2,0,0,1,1)
        self.right_bar_layout_2.addWidget(self.right_bar_widget_search_input_2, 0, 1, 1, 8)
        self.right_bar_layout_2.setAlignment(QtCore.Qt.AlignLeft) # 布局内的部件左对齐
        self.right_bar_layout_2.setSpacing(0) # 设置布局内部件间隙为0    设置内边框距离
        self.right_layout_2.addWidget(self.right_bar_widget_2,0, 0, 1, 9)
        self.main_layout.addWidget(self.right_widget_2, 0, 2, 12, 10) # 右侧部件在第0行第3列，占8行9列

    def left_button_3_ui(self):
        print("热门MV 被点击啦...")
        self.right_widget_3 = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget_3.setObjectName('right_widget')
        self.right_layout_3 = QtWidgets.QGridLayout()
        self.right_widget_3.setLayout(self.right_layout_3) # 设置右侧部件布局为网格
        self.right_widget_3.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')


        self.right_bar_widget_3 = QtWidgets.QWidget()        # 右侧顶部搜索框部件
        self.right_bar_layout_3 = QtWidgets.QGridLayout()    # 右侧顶部搜索框网格布局
        self.right_bar_widget_3.setLayout(self.right_bar_layout_3)
        # self.search_icon_3 = QtWidgets.QLabel('  ' + chr(0xf019))
        self.search_icon_3 = QtWidgets.QPushButton('  ' + chr(0xf019) + ' ' + '下载  ')
        self.search_icon_3.setFont(qtawesome.font('fa', 16))   # "http://www.fontawesome.com.cn/"
        self.search_icon_3.setStyleSheet('background-color: rgb(192, 192, 192);border-radius:10px;padding:6px 4px;')

        self.right_bar_widget_search_input_3 = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input_3.setPlaceholderText("输入JSON API 进行KML下载")
        self.right_bar_widget_search_input_3.setStyleSheet("QLineEdit{border:1px solid gray;width:600px;border-radius:10px;padding:6px 4px;}")
        self.right_bar_layout_3.addWidget(self.search_icon_3, 0, 10, 1, 12)
        self.right_bar_layout_3.addWidget(self.right_bar_widget_search_input_3, 0, 1, 1, 8)
        self.right_bar_layout_3.setAlignment(QtCore.Qt.AlignLeft) # 布局内的部件左对齐
        self.right_bar_layout_3.setSpacing(0) # 设置布局内部件间隙为0    设置内边框距离
        self.right_layout_3.addWidget(self.right_bar_widget_3, 0, 0, 1, 2)

        # 创建
        self.right_browser_widget_3 = QtWidgets.QWidget()                           # 右侧顶部搜索框部件
        self.right_browser_layout_3 = QtWidgets.QGridLayout()                       # 右侧顶部搜索框网格布局
        self.right_browser_widget_3.setLayout(self.right_browser_layout_3)          # 右侧顶部搜索框网格布局

        self.browser = QWebEngineView()  # 设置浏览器
        self.browser.setUrl(QUrl('http://datav.aliyun.com/portal/school/atlas/area_selector'))  # 指定打开界面的 URL


        self.right_browser_layout_3.addWidget(self.browser, 0, 0, 1, 1)
        self.right_layout_3.addWidget(self.right_browser_widget_3, 2, 0, 9, 9)

        self.main_layout.addWidget(self.right_widget_3, 0, 2, 12, 10) # 右侧部件在第0行第3列，占8行9列

        self.search_icon_3.clicked.connect(self.left_button_3_ui_search_icon_3_cilck)


    def left_button_3_ui_search_icon_3_cilck(self):

        print("left_button_3_ui_search_icon_3_cilck  被点击啦")
        link = self.right_bar_widget_search_input_3.text()
        print(link)

        pass


    # 重写三个方法使我们的Example窗口支持拖动,上面参数window就是拖动对象
    def mousePressEvent(self, event): # 鼠标长按事件
        if event.button() == QtCore.Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent): # 鼠标移动事件
        if QtCore.Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent): # 鼠标释放事件
        self.m_drag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def paintEvent(self, ev): # 重绘窗口边框线条
        painter = QtGui.QPainter(self)
        painter.begin(self)
        gradient = QtGui.QLinearGradient(QtCore.QRectF(self.rect()).topLeft(), QtCore.QRectF(self.rect()).bottomLeft())
        # gradient.setColorAt(0.0, QtCore.Qt.black)
        gradient.setColorAt(0.5, QtCore.Qt.darkGray)
        # gradient.setColorAt(0.7, QtCore.Qt.)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(gradient)
        painter.setPen(QtCore.Qt.transparent)
        painter.drawRoundedRect(self.rect(), 10.0, 10.0)
        painter.end()

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()