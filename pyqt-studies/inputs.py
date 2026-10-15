import sys
from PyQt6 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_area = QtWidgets.QLineEdit()
        self.clearButton = QtWidgets.QPushButton("Temizle")
        self.writeButton = QtWidgets.QPushButton("Yazdır")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.text_area)
        v_box.addWidget(self.clearButton)
        v_box.addWidget(self.writeButton)
        v_box.addStretch()

        self.setLayout(v_box)

        self.clearButton.clicked.connect(self.click)
        self.writeButton.clicked.connect(self.click)

        self.show()

    def click(self):
        sender = self.sender()
        if sender.text() == "Temizle":
            self.text_area.clear()
        elif sender.text() == "Yazdır":
            print(self.text_area.text())
    
app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec())