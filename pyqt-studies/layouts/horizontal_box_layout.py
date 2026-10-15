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
    
    # NOTE Once bosluk koyar sonra butonlari saga yaslar
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    # NOTE Once ilk butonu koyar sonra bosluk koyar sonra ikinci butonu koyar
    h_box.addWidget(okay)
    h_box.addStretch()
    h_box.addWidget(cancel)

    # NOTE Once butonlari sola yaslar sonra bosluk koyar
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    h_box.addStretch()

    # NOTE Yani aslinda stretch yatayda elementlerden geri kalan genislikte bir bosluk koyuyor gibi

    window.setLayout(h_box)

    window.show()

    sys.exit(app.exec())

Window()