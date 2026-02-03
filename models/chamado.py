from database import database

class Chamado:
    def __init__(self, titulo, descricao, prioridade,
                 status="Aberto", tecnico_id=None, id=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        self.tecnico_id = tecnico_id

    def save(self):
        conn = database.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO chamados (titulo, descricao, prioridade, status, tecnico_id)
            VALUES (?, ?, ?, ?, ?)
        """, (self.titulo, self.descricao, self.prioridade,
              self.status, self.tecnico_id))
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "status": self.status,
            "tecnico_id": self.tecnico_id
        }
