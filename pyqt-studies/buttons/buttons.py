import sys
from PyQt6 import QtWidgets, QtGui

def Window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("PyQT6 Lesson 3")
    # Set Location for window
    window.setGeometry(100, 100, 500, 500)

    button = QtWidgets.QPushButton(window)
    button.setText("Save")
    button.move(190, 80)

    label = QtWidgets.QLabel(window)
    label.setText("Hello World")
    label.move(200, 30)

    window.show()

    sys.exit(app.exec())

Window()