from layouts import ClothFabricLayout
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QPushButton, QComboBox, QLabel, QVBoxLayout, QWidget, 
                               QLineEdit, QCalendarWidget, QCheckBox)

def create_register_clothes_window(window):
   
    clothes_type_layout = QVBoxLayout()
    clothes_type_label = QLabel('Informe o tipo da vestimenta')
    clothes_type_combobox = QComboBox()
    clothes_type_combobox.addItems(['camisa', 'calça', 'meia', 'bermuda', 'tenis', 'blusa', 'touca', 'cueca'])
    clothes_type_layout.addWidget(clothes_type_label)
    clothes_type_layout.addWidget(clothes_type_combobox)

    clothing_fabric_layout = QVBoxLayout()
    clothing_fabric_label = QLabel('Informe o(s) tecido(s) da roupa')
    clothing_fabric = ClothFabricLayout()
    clothing_fabric_layout.addWidget(clothing_fabric_label)
    clothing_fabric_layout.addLayout(clothing_fabric)

    color_layout = QVBoxLayout()
    clothes_color_label = QLabel('Informe a cor da vestimenta')
    clothes_color_line_edit = QLineEdit()
    color_layout.addWidget(clothes_color_label)
    color_layout.addWidget(clothes_color_line_edit)

    clothes_aquisition_date_layout = QVBoxLayout()
    clothes_aquisition_date_label = QLabel('Informe a data de aquisição da vestimenta')
    clothes_aquisition_date = QCalendarWidget()
    clothes_aquisition_date_layout.addWidget(clothes_aquisition_date_label)
    clothes_aquisition_date_layout.addWidget(clothes_aquisition_date)

    clothes_brand_layout = QVBoxLayout()
    clothes_brand_label = QLabel('Informe a marca da vestimenta')
    clothes_brand_combobox = QComboBox()
    clothes_brand_combobox.addItems(['Hering', 'Adidas', 'Puma'])
    clothes_brand_layout.addWidget(clothes_brand_label)
    clothes_brand_layout.addWidget(clothes_brand_combobox)

    clothes_in_use_indicator = QCheckBox("Vestimenta atualmente em uso?")

    register_clothes_button = QPushButton('Registrar vestimenta')
    
    register_clothes_button.setCheckable(True)
    register_clothes_button.clicked.connect(lambda: retrieve_values(window))

    layout = QVBoxLayout()
    layout.addLayout(clothes_type_layout)
    layout.addSpacing(30)
    layout.addLayout(clothing_fabric_layout)
    layout.addSpacing(30)
    layout.addLayout(color_layout)
    layout.addSpacing(30)
    layout.addLayout(clothes_aquisition_date_layout)
    layout.addSpacing(30)
    layout.addLayout(clothes_brand_layout)
    layout.addSpacing(30)
    layout.addWidget(clothes_in_use_indicator, alignment=Qt.AlignCenter)
    layout.addSpacing(30)
    layout.addWidget(register_clothes_button, alignment=Qt.AlignCenter)

    layout.setContentsMargins(20, 80, 20, 80)
    layout.setSpacing(0)

    widget = QWidget()
    widget.setLayout(layout)

    window.setCentralWidget(widget)

    window.clothes_type_combobox = clothes_type_combobox
    window.clothes_color_line_edit = clothes_color_line_edit
    window.clothes_aquisition_date = clothes_aquisition_date
    window.clothes_brand_combobox = clothes_brand_combobox
    window.clothes_in_use_indicator = clothes_in_use_indicator

def retrieve_values(window):

    clothes_type = window.clothes_type_combobox.currentText()
    clothes_color = window.clothes_color_line_edit.text()
    aquisition_date = window.clothes_aquisition_date.selectedDate().toString("dd/MM/yyyy")
    clothes_brand = window.clothes_brand_combobox.currentText()
    in_use = window.clothes_in_use_indicator.isChecked()

    # Exibindo os valores
    print(f"Tipo da vestimenta: {clothes_type}")
    print(f"Cor da vestimenta: {clothes_color}")
    print(f"Data de aquisição da vestimenta: {aquisition_date}")
    print(f"Marca da vestimenta: {clothes_brand}")
    print(f"Vestimenta em uso? {'Sim' if in_use else 'Não'}")