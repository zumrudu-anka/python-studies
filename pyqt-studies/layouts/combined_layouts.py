import sys
from PyQt6 import QtWidgets, QtGui

def Window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("PyQT6 Lesson 4")
    # Set Location for window
    window.setGeometry(100, 100, 500, 500)

    okay = QtWidgets.QPushButton("Ok")
    cancel = QtWidgets.QPushButton("Cancel")

    h_box = QtWidgets.QHBoxLayout()

    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)


    window.setLayout(v_box)

    window.show()

    sys.exit(app.exec())

Window()