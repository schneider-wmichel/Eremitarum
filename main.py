import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class Eremita(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eremita")
        self.resize(940, 540)


app = QApplication(sys.argv)

janela = Eremita()
janela.show()

sys.exit(app.exec())