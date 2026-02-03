from database import database

class Tecnico:
    def __init__(self, nome, especialidade, id=None):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "especialidade": self.especialidade
        }
