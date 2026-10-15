import sys
import sqlite3
from PyQt6 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.create_db_connection()
        self.init_ui()

    def create_db_connection(self):
        self.db_connection = sqlite3.connect("database.db")
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute("CREATE TABLE IF NOT EXISTS USER (username TEXT, password TEXT)")
        
        self.db_connection.commit()

    def init_ui(self):
        self.usernameInput = QtWidgets.QLineEdit()
        self.usernameInput.setPlaceholderText("Username")
        self.passwordInput = QtWidgets.QLineEdit()
        self.passwordInput.setPlaceholderText("Password")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.loginButton = QtWidgets.QPushButton("Login")
        self.registerButton = QtWidgets.QPushButton("Register")
        self.text_area = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.usernameInput)
        v_box.addWidget(self.passwordInput)
        v_box.addWidget(self.text_area)
        v_box.addStretch()
        v_box.addWidget(self.loginButton)
        v_box.addWidget(self.registerButton)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("User Login")
        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.register)

        self.show()

    def login(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        
        self.db_cursor.execute("Select * From USER Where username = ? and password = ?", (username, password))
        data = self.db_cursor.fetchall()

        if len(data) == 0:
            self.text_area.setText("Böyle bir kullanıcı yok!\nLütfen tekrar deneyin")
        else:
            self.text_area.setText(f"Hoşgeldiniz {username}")
        

    def register(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()

        self.db_cursor.execute("Insert Into USER Values (?, ?)", (username, password))
        self.db_connection.commit()

        self.usernameInput.setText("")
        self.passwordInput.setText("")
        self.text_area.setText(f"{username} Başarıyla oluşturuldu!")


app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec())