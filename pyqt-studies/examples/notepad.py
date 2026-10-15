import sys
import os

from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
    QHBoxLayout,
    QMainWindow
)

from PyQt6.QtGui import QAction

class Notepad(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.text_area = QTextEdit()
        self.clearTextButton = QPushButton("Clear")
        self.openFileButton = QPushButton("Open")
        self.saveFileButton = QPushButton("Save")

        h_box = QHBoxLayout()
        h_box.addWidget(self.clearTextButton)
        h_box.addWidget(self.openFileButton)
        h_box.addWidget(self.saveFileButton)

        v_box = QVBoxLayout()
        v_box.addWidget(self.text_area)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("NotePad")

        self.clearTextButton.clicked.connect(self.clearText)
        self.openFileButton.clicked.connect(self.openFile)
        self.saveFileButton.clicked.connect(self.saveFile)

    def clearText(self):
        self.text_area.clear()

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, "Open File", ".")

        # NOTE getOpenFileName bir demet dondurur. Demetin ilk degeri secilen dosyanin adidir
        with open(filename[0], "r") as file:
            self.text_area.setText(file.read())

    def saveFile(self):
        filename = QFileDialog.getSaveFileName(self, "Save File", ".")

        with open(filename[0],"w") as file:
            file.write(self.text_area.toPlainText())

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.app = Notepad()
        self.setCentralWidget(self.app)
        self.create_menus()

    def create_menus(self):

        menubar = self.menuBar()

        fileMenu = menubar.addMenu("File")
        editMenu = menubar.addMenu("Edit")

        open_file = QAction("Open File", self)
        open_file.setShortcut("Ctrl+O")

        save_file = QAction("Save File",self)
        save_file.setShortcut("Ctrl+S")

        clear_file = QAction("Clear Text",self)
        clear_file.setShortcut("Ctrl+D")

        quit = QAction("Quit", self)
        quit.setShortcut("Ctrl+Q")

        fileMenu.addAction(open_file)
        fileMenu.addAction(save_file)
        fileMenu.addAction(clear_file)
        fileMenu.addAction(quit)

        search_and_edit = editMenu.addMenu("Search and Edit")
        search = QAction("Search", self)
        edit = QAction("Edit", self)
        search_and_edit.addAction(search)
        search_and_edit.addAction(edit)

        fileMenu.triggered.connect(self.response)

        self.setWindowTitle("Text Editor")
        self.show()

    def response(self, action):

        if action.text() == "Open File":
            self.app.openFile()
        elif action.text() == "Save File":
            self.app.saveFile()
        elif action.text() == "Clear Text":
            self.app.clearText()
        elif action.text() == "Quit":
            app.quit()

app = QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec())