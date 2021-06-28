# -*- coding: cp1252 -*-
# on jule 20
# - change baudrate
# - comport
# - add logger in two state 1. apend; 2. create new   high
# - simple graphic
# - animate color                                     high
# - animate add blur
# - view objgraph module for debug
# - view image
# - view to much image
# - load image scroll
# - finding vulnerability in the program using open source tool Bandit
# - visualization algorithm
# https://code-explained.com/lesson/simplified_hash_search
from PyQt5 import QtWidgets
from main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    #QtCore.QTimer.singleShot(0, MainWindow.close) # <---
    sys.exit(app.exec_())