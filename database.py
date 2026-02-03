from models.tarefa import database, Database

class Tarefa:
    def __init__(self, titulo, concluido = False, id = None):
        self.titulo = titulo
        self.concluido = concluido
        self.id = id 
        self.db = database # Usa a instância já existente

    def save(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        # Correção do SQL abaixo:
        cursor.execute('INSERT INTO tarefas (titulo, concluido) VALUES (?, ?)', (self.titulo, self.concluido))
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'concluido': self.concluido
        }

    @classmethod
    def find_all(cls):
        conn = database.get_connection() # Correção do nome da função
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tarefas')
        registros = cursor.fetchall()
        conn.close()

        return [cls(titulo=r[1], concluido=r[2], id=r[0]) for r in registros]