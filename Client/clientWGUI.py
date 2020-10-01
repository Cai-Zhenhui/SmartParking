# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys
from ui import Ui_Form


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    root=QtWidgets.QWidget()#创建一个根容器
    window=Ui_Form()
    window.setupUi(root)#将自己设计的ui加载到根容器中

    root.show()
    sys.exit(app.exec())#运行
    pass
