from PyQt6.QtGui import QAction, QKeySequence

class FullApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.statusBar().showMessage("Готово")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&Файл")
        help_menu = menu_bar.addMenu("&Довідка")

        exit_action = QAction("Вихід", self)
        exit_action.setShortcut(QKeySequence("Ctrl+Q"))
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        about_action = QAction("Про програму", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

        toolbar = self.addToolBar("Main Toolbar")
        toolbar.addAction(exit_action)

    def show_about(self):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.about(self, "Про нас", "Це PyQt6 додаток v1.0")
