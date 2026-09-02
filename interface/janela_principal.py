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
from dados.armazenamento import salvar_diario, carregar_diario


class JanelaPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eremitarum")
        self.resize(600, 500)

        self.label_data = QLabel("Qual é a data do diário?")

        self.data = QDateEdit()
        self.data.setCalendarPopup(True)
        self.data.setDate(QDate.currentDate())

        self.botao_continuar = QPushButton("Continuar")

        self.label_titulo = QLabel("Título")

        self.titulo = QLineEdit()

        self.label_texto = QLabel("Diário")

        self.texto = QTextEdit()

        self.botao_salvar = QPushButton("Salvar")

        layout = QVBoxLayout()

        layout.addWidget(self.label_data)
        layout.addWidget(self.data)
        layout.addWidget(self.botao_continuar)

        layout.addWidget(self.label_titulo)
        layout.addWidget(self.titulo)

        layout.addWidget(self.label_texto)
        layout.addWidget(self.texto)

        layout.addWidget(self.botao_salvar)

        self.setLayout(layout)

        self.botao_continuar.clicked.connect(self.continuar)
        self.botao_salvar.clicked.connect(self.salvar)


    def continuar(self):

        data_escolhida = self.data.date()

        data_formatada = data_escolhida.toString("dd/MM/yyyy")

        data_arquivo = data_escolhida.toString("yyyy-MM-dd")

        entrada = carregar_diario(data_arquivo)

        if entrada is None:

            entrada = Diario(
                data_arquivo
            )

            salvar_diario(entrada)

            print("Novo diário criado!")

        else:

            print("Diário existente carregado!")

        self.titulo.setText(entrada.titulo)
        self.texto.setPlainText(entrada.texto)

        self.entrada_atual = entrada

        print("Data:", data_formatada)


    def salvar(self):

        if not hasattr(self, "entrada_atual"):
            print("Nenhum diário foi selecionado.")
            return

        self.entrada_atual.titulo = self.titulo.text()

        self.entrada_atual.texto = self.texto.toPlainText()

        salvar_diario(self.entrada_atual)

        print("Diário salvo!")