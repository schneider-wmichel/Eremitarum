import json
from pathlib import Path


PASTA_CODEX = Path(__file__).parent

def carregar_codex(numero):
	nome_arquivo = f"{numero:03d}_genese_do_eremitarum.json"
	caminho = PASTA_CODEX / nome_arquivo

	if not caminho.exists():
		return None

	with open(caminho, "r", encoding="utf-8") as arquivo:
		return json.load(arquivo)


