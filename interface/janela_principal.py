from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QDateEdit,
    QLineEdit,
    QTextEdit,
)

from PySide6.QtCore import QDate

from dados.diario import Diario
from dados.armazenamento import salvar_diario
from codex.janela_codex import JanelaCodex


class JanelaPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eremitarum")
        self.resize(600, 500)

        self.label_data = QLabel(
            "Qual é a data do diário?"
        )

        self.data = QDateEdit()
        self.data.setCalendarPopup(True)
        self.data.setDate(QDate.currentDate())

        self.botao_continuar = QPushButton(
            "Continuar"
        )

        self.botao_codex = QPushButton(
            "Arquivos Codex"
        )

        self.label_titulo = QLabel("Título")

        self.titulo = QLineEdit()

        self.label_texto = QLabel("Diário")

        self.texto = QTextEdit()

        self.botao_salvar = QPushButton(
            "Salvar"
        )

        layout = QVBoxLayout()

        layout.addWidget(self.label_data)
        layout.addWidget(self.data)
        layout.addWidget(self.botao_continuar)
        layout.addWidget(self.botao_codex)

        layout.addWidget(self.label_titulo)
        layout.addWidget(self.titulo)

        layout.addWidget(self.label_texto)
        layout.addWidget(self.texto)

        layout.addWidget(self.botao_salvar)

        self.setLayout(layout)

        self.botao_continuar.clicked.connect(
            self.continuar
        )

        self.botao_codex.clicked.connect(
            self.abrir_codex
        )

        self.botao_salvar.clicked.connect(
            self.salvar
        )

        self.janela_codex = None

    def continuar(self):

        data_escolhida = self.data.date()

        data_formatada = data_escolhida.toString(
            "dd/MM/yyyy"
        )

        data_arquivo = data_escolhida.toString(
            "yyyy-MM-dd"
        )

        entrada = Diario(
            data_arquivo
        )

        salvar_diario(entrada)

        print("Entrada criada!")
        print("Data:", data_formatada)

    def abrir_codex(self):

        self.janela_codex = JanelaCodex()
        self.janela_codex.show()

    def salvar(self):

        data_arquivo = self.data.date().toString(
            "yyyy-MM-dd"
        )

        entrada = Diario(
            data_arquivo,
            self.titulo.text(),
            self.texto.toPlainText()
        )

        salvar_diario(entrada)

        print("Diário salvo!")
