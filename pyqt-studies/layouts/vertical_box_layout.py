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

    v_box = QtWidgets.QVBoxLayout()

    # NOTE Once bosluk koyar sonra butonlari asagi yaslar
    v_box.addStretch()
    v_box.addWidget(okay)
    v_box.addWidget(cancel)

    # NOTE Once ilk butonu koyar sonra bosluk koyar sonra ikinci butonu koyar
    v_box.addWidget(okay)
    v_box.addStretch()
    v_box.addWidget(cancel)

    # NOTE Once butonlari yukari yaslar sonra bosluk koyar
    v_box.addWidget(okay)
    v_box.addWidget(cancel)
    v_box.addStretch()

    # NOTE Yani aslinda stretch burada dikeyde elementlerden geri kalan genislikte bir bosluk koyuyor gibi
    window.setLayout(v_box)

    window.show()

    sys.exit(app.exec())

Window()