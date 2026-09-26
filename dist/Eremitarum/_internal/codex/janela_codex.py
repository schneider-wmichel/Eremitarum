from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton
)

from codex.leitor import carregar_codex


class JanelaCodex(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Arquivos Codex")
        self.resize(700, 600)

        layout = QVBoxLayout()

        titulo = QLabel("Arquivos Codex")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold;")

        self.texto = QTextEdit()
        self.texto.setReadOnly(True)

        botao = QPushButton("Carregar Codex 001")
        botao.clicked.connect(self.carregar_primeiro_codex)

        layout.addWidget(titulo)
        layout.addWidget(self.texto)
        layout.addWidget(botao)

        self.setLayout(layout)

    def carregar_primeiro_codex(self):

        codex = carregar_codex(1)

        if codex is None:
            self.texto.setPlainText(
                "Codex 001 não encontrado."
            )
            return

        titulo = codex["titulo"]
        data = codex["data"]

        desenvolvimento = (
            codex["conteudo"]["desenvolvimento"]
        )

        registro = (
            codex["conteudo"]["registro_pessoal"]
        )

        texto = (
            f"{titulo}\n"
            f"Data: {data}\n\n"
            f"{desenvolvimento}\n\n"
            f"{registro['titulo']}\n\n"
            f"{registro['texto']}"
        )

        self.texto.setPlainText(texto)
