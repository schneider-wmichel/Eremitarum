class Diario:

    def __init__(self, data, titulo="", texto="", tags=None):
        self.data = data
        self.titulo = titulo
        self.texto = texto
        self.tags = tags or []

    def para_dict(self):
        return {
            "data": self.data,
            "titulo": self.titulo,
            "texto": self.texto,
            "tags": self.tags
        }

    @classmethod
    def de_dict(cls, dados):
        return cls(
            dados["data"],
            dados["titulo"],
            dados["texto"],
            dados["tags"]
        )