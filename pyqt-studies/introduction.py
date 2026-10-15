import sys
from PyQt6 import QtWidgets, QtGui

def Window():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()

    window.setWindowTitle("PyQT6 Lesson 1")
    
    # Set Location for window
    window.setGeometry(100, 100, 500, 500)
    window.show()

    sys.exit(app.exec())

Window()