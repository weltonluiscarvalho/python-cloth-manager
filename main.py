import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Cloth Manager')
        self.setFixedHeight(500)
        self.setFixedWidth(400)

        layout = QVBoxLayout()
        widget = QWidget()

        register_cloth_button = QPushButton('register cloth')
        register_cloth_button.setFixedWidth(100)
        register_cloth_button.setFixedHeight(50)

        register_cloth_button.setCheckable(True)
        register_cloth_button.clicked.connect(self.register_cloth)

        layout.addWidget(register_cloth_button)

        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def register_cloth(self):
        print('cloth registered!')

    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()