import sys

from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QRadioButton,
    QLabel,
    QPushButton,
    QVBoxLayout
)


class Window(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.radio_text = QLabel("Hangi dili daha çok seviyorsun ?")
        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")
        self.php = QRadioButton("Php")
        self.text_area = QLabel("")
        self.sendButton = QPushButton("Gönder")

        v_box = QVBoxLayout()

        v_box.addWidget(self.radio_text)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addStretch()
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.sendButton)

        self.setLayout(v_box)

        self.sendButton.clicked.connect(lambda : self.click(self.python.isChecked(), self.java.isChecked(), self.php.isChecked(), self.text_area))

        self.setWindowTitle("Radio Button")

        self.show()

    def click(self, python, java, php, text_area):
        if python:
            text_area.setText("Python")
        if php:
            text_area.setText("Php")
        if java:
            text_area.setText("Java")


app = QApplication(sys.argv)

window = Window()

sys.exit(app.exec())