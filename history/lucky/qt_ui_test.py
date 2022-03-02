




from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("登录")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        #     QStackedLayout()
        #     QStackedLayout(QWidget)
        #     QStackedLayout(QLayout)
        # 1. 创建一个布局管理对象
        sl = QStackedLayout()

        # 2. 把布局对象设置给需要布局的父控件  父布局
        self.setLayout(sl)

        # 3. 通过发布对象，管理一些子布局
        label1 = QLabel("标签一")
        label2 = QLabel("标签二")
        label3 = QLabel("标签三")
        label4 = QLabel("标签四")
        label1.setStyleSheet("background-color: cyan;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: red;")
        label4.setStyleSheet("background-color: orange;")

        label5 = QLabel("标签五")
        label6 = QLabel("标签六")
        label7 = QLabel("标签七")
        label5.setStyleSheet("background-color: pink;")
        label6.setStyleSheet("background-color: blue;")
        label7.setStyleSheet("background-color: cyan;")

        b_layout = QVBoxLayout()
        b_layout.addWidget(label5)
        b_layout.addWidget(label6)
        b_layout.addWidget(label7)

        sl.addWidget(label1)
        sl.addWidget(label2)
        sl.addWidget(label3)

        sl.insertWidget(0, label4)

        print(sl.currentIndex())  # 获取当前展示的索引值

        print(sl.widget(3))       # 获取标签索引值为3的控件
        print(sl.widget(3).text())# 获取标签索引值为3的控件的值

        # 切换显示的方法   显示索引值为2的控件
        # sl.setCurrentIndex(3)
        # 切换显示的方法   显示控件为label4的控件
        # sl.setCurrentWidget(label4)

        # 显示模式 所有空间均被显示 默认第一个看见  默认展示最前面 可以不用设置
        sl.setStackingMode(QStackedLayout.StackAll)
        # label1.hide()

        # timer = QTimer(self)
        # timer.timeout.connect(lambda: sl.setCurrentIndex((sl.currentIndex()+1) % sl.count()))
        # timer.start(1000)

        # 信号
        sl.currentChanged.connect(lambda val: print(val))




if __name__ == '__main__':

    # 1 创建一个应用程序对象
    app = QApplication(sys.argv)

    # 2.1  创建控件
    window = Window()
    # 2.3 展示控件
    window.show()
    # 3. 应用程序进入消息循环
    sys.exit(app.exec())






















































