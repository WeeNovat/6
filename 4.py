from PyQt6.QtCore import pyqtSignal

class InputComponent(QWidget):
    data_submitted = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.edit = QLineEdit()
        self.btn = QPushButton("Відправити")
        self.btn.clicked.connect(self.emit_signal)
        layout.addWidget(self.edit)
        layout.addWidget(self.btn)

    def emit_signal(self):
        self.data_submitted.emit(self.edit.text())

class DisplayComponent(QWidget):
    def update_label(self, text):
        self.label.setText(f"Отримано: {text}")
