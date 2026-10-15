import sys

from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QTextEdit,
    QPushButton,
    QVBoxLayout
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.text_area = QTextEdit()
        self.clearButton = QPushButton("Temizle")

        v_box = QVBoxLayout()
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.clearButton)

        self.setWindowTitle("Yazı Alanı")

        self.setLayout(v_box)
        self.clearButton.clicked.connect(self.click)

        self.show()

    def click(self):

        self.text_area.clear()

app = QApplication(sys.argv)

window = Window()

sys.exit(app.exec())