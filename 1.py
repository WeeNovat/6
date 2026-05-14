from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QLineEdit, 
                             QComboBox, QSlider, QProgressBar, QCheckBox)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мій PyQt6 Додаток")
        self.setMinimumSize(400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.label = QLabel("Вітаємо у формі!")
        main_layout.addWidget(self.label)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Введіть ваше ім'я...")
        main_layout.addWidget(self.input_field)

        h_layout = QHBoxLayout()
        
        self.combo = QComboBox()
        self.combo.addItems(["Варіант 1", "Варіант 2", "Варіант 3"])
        self.combo.setToolTip("Оберіть один з варіантів")
        h_layout.addWidget(self.combo)

        self.check = QCheckBox("Активувати")
        h_layout.addWidget(self.check)
        
        main_layout.addLayout(h_layout)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        main_layout.addWidget(self.slider)

        self.progress = QProgressBar()
        self.progress.setValue(25)
        main_layout.addWidget(self.progress)

        self.btn = QPushButton("Натисни мене")
        main_layout.addWidget(self.btn)
