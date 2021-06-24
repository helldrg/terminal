# -*- coding: cp1252 -*-
# on june
# - change baudrate
# - comport
# - logger action
# - simple graphic
# + background animate
# - animate color
# - animate add blur
# + resize main form: position components
# + button hover change image background
# + min size window +++++++++++++++++++++++++++
# + change size main window on 550, 250
# + change size plain text edit on 430, 175
# - view objgraph module for debug
# - view image
# - view to much image
# - load image scroll
# - Ищем уязвимости в Python-коде с помощью open source инструмента Bandit
# - визуализация алгоритмов
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