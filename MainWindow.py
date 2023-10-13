from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Password Generator")

        self.setMinimumSize(500, 300)

        central_widget = CentralWidget(self)
        self.setCentralWidget(central_widget)