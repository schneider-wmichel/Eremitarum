import json
from pathlib import Path

from dados.diario import Diario


PASTA_DIARIO = Path("diario")


def salvar_diario(diario):

    PASTA_DIARIO.mkdir(exist_ok=True)

    arquivo = PASTA_DIARIO / f"{diario.data}.json"

    with arquivo.open("w", encoding="utf-8") as f:
        json.dump(
            diario.para_dict(),
            f,
            ensure_ascii=False,
            indent=4
        )


def carregar_diario(data):

    arquivo = PASTA_DIARIO / f"{data}.json"

    if not arquivo.exists():
        return None

    with arquivo.open("r", encoding="utf-8") as f:
        dados = json.load(f)

    return Diario.de_dict(dados)