import sys
from screens import create_register_clothes_window as crt
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget)


def initial_window(window):
    layout = QVBoxLayout()
    widget = QWidget()

    register_clothes_button = QPushButton('Registrar uma nova vestimenta')
    register_clothes_button.setFixedWidth(200)
    register_clothes_button.setFixedHeight(50)

    register_clothes_button.setCheckable(True)
    register_clothes_button.clicked.connect(window.register_clothes)

    layout.addWidget(register_clothes_button, alignment=Qt.AlignCenter)

    widget.setLayout(layout)

    window.setCentralWidget(widget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Gerenciador de vestimenta')
        self.setFixedSize(QSize(400, 700))

    def register_clothes(self):
        # create_register_clothes_window(self)
        crt(self)
        print('clothes registered!')


app = QApplication(sys.argv)

window = MainWindow()
initial_window(window)
window.show()

app.exec()