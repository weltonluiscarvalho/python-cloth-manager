from PySide6.QtWidgets import (QPushButton, QComboBox, QVBoxLayout, QHBoxLayout, QSpinBox)

class ClothFabricLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        
        self.add_clothing_fabric()
        self.setContentsMargins(0, 0, 0, 0)

    def add_clothing_fabric(self):
        for i in range(self.count()):
            widget = self.itemAt(i).widget()

            if isinstance(widget, QPushButton):
                self.removeWidget(widget)

        clothing_fabric_combobox = QComboBox()
        clothing_fabric_combobox.addItems(['algodão', 'poliester', 'seda'])

        clothing_fabric_percentage = QSpinBox()
        clothing_fabric_percentage.setMinimum(1)
        clothing_fabric_percentage.setMaximum(100)

        clothing_fabric_layout = QHBoxLayout()
        clothing_fabric_layout.addWidget(clothing_fabric_combobox)
        clothing_fabric_layout.addWidget(clothing_fabric_percentage)
        clothing_fabric_layout.setSpacing(10)
        self.addLayout(clothing_fabric_layout)

        add_fabric_button = QPushButton('adicionar')
        add_fabric_button.clicked.connect(self.add_clothing_fabric)
        self.addWidget(add_fabric_button)