import sys
from PyQt6 import QtWidgets, QtGui

def Window():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()

    window.setWindowTitle("PyQT6 Lesson 2")

    label1 = QtWidgets.QLabel(window)
    label1.setText("Burası bir yazıdır")
    label1.move(200, 30)

    label2 = QtWidgets.QLabel(window)
    label2.setPixmap(QtGui.QPixmap("assets/images/example.png"))
    label2.move(80, 70)
    # Set Location for window
    window.setGeometry(100, 100, 500, 500)
    window.show()

    sys.exit(app.exec())

Window()