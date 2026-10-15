import sys

from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QCheckBox,
    QLabel,
    QPushButton,
    QVBoxLayout
)


class Window(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.checkbox = QCheckBox("Python'ı seviyor musunuz ?")
        self.text_area = QLabel("")
        self.button = QPushButton("Bana Tıkla")

        v_box = QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.button)

        self.setLayout(v_box)

        self.setWindowTitle("Check Box")

        self.button.clicked.connect(lambda : self.click(self.checkbox.isChecked(), self.text_area))

        self.show()

    def click(self, checkbox, text_area):
        if checkbox:
            text_area.setText("Python'ı seviyorsun çok güzel")
        else:
            text_area.setText("Niye Sevmiyorsun ? ")

app = QApplication(sys.argv)

window = Window()

sys.exit(app.exec())