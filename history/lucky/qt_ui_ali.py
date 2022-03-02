from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        gl = QGridLayout()

        self.setLayout(gl)

        label1 = QLabel("标签一")
        label2 = QLabel("标签二")
        label3 = QLabel("标签三")
        label4 = QLabel("标签四")
        label1.setStyleSheet("background-color: cyan;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: red;")
        label4.setStyleSheet("background-color: orange;")

        # gl.addWidget(label1)
        # gl.addWidget(label2)
        # gl.addWidget(label3)

        gl.addWidget(label1, 0, 0)    # 添加到第0行0列
        gl.addWidget(label2, 0, 1)    # 添加到第0行1列
        # gl.addWidget(label3, 1, 0)  # 添加到第1行0列

        gl.addWidget(label3, 1, 0, 3, 3)  # 合并单元格 到开始1行0列 到 跨1行 2列

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

        # gl.addLayout(b_layout, 4, 0)
        gl.addLayout(b_layout, 4, 0, 1, 4)  # 合并单元格 到开始4行0列 到 跨1行 4列
        print(gl.getItemPosition(2))   # id为2 标签二 的位置信息

        # 限制最小的行高，最小的列宽
        # gl.setColumnMinimumWidth(0, 100)    #限制第0列 最小宽度为100
        # gl.setRowMinimumHeight(0, 100)      #限制第0行 最小宽度为100

        # 拉伸系数
        gl.setColumnStretch(0, 2)   # 第0列 拉伸系数为2
        gl.setColumnStretch(1, 1)   # 第1列 拉伸系数为1
        gl.setRowStretch(2, 1)      # 第1行 拉伸系数为1


        print(gl.spacing())            # 水平方向垂直方向默认值都是7
        print(gl.horizontalSpacing())  # 水平方向间距是7
        print(gl.verticalSpacing())    # 垂直方向间距是7

        gl.setVerticalSpacing(60)   # 设置垂直间距为60
        gl.setHorizontalSpacing(30)   # 设置水平间距为30
        gl.setSpacing(30)            # 设置垂直水平间距均为为30

        gl.setOriginCorner(Qt.BottomRightCorner)

        print(gl.rowCount())        # 获取总行数
        print(gl.columnCount())     # 获取总列数

        # 获取某一单元格尺寸大小
        print(gl.cellRect(0, 1))   # 0 行 1列
        print(gl.itemAtPosition(0, 1).widget().text())   # 0 行 1列



if __name__ == '__main__':

    # 1 创建一个应用程序对象
    app = QApplication(sys.argv)

    # 2.1  创建控件
    window = Window()
    # 2.3 展示控件
    window.show()
    # 3. 应用程序进入消息循环
    sys.exit(app.exec())
