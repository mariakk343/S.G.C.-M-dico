from app.database.connection import get_db
from app.models.cliente_model import ClienteModel

class ClienteRepository:
    def get_all_clientes(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT id, nome, telefone, data_nascimento FROM cliente")
        rows = cursor.fetchall()
        return [
            ClienteModel(id=row[0], nome=row[1], telefone=row[2], data_nascimento=row[3]) for row in rows
        ]
    
    def get_cliente_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT id, nome, telefone, data_nascimento FROM cliente WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return ClienteModel(id=row[0], nome=row[1], telefone=row[2], data_nascimento=row[3])
        return None
    
    def create_cliente(self, cliente):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO cliente (nome, telefone, data_nascimento) VALUES (?, ?, ?)",
            (cliente.get_nome(), cliente.get_telefone(), cliente.get_data_nascimento())
        )
        connection.commit()

    def update_cliente(self, cliente):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE cliente SET nome = ?, telefone = ?, data_nascimento = ? WHERE id = ?",
            (cliente.get_nome(), cliente.get_telefone(), cliente.get_data_nascimento(), cliente.get_id())
        )
        connection.commit()
        
    def delete_cliente(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM cliente WHERE id = ?", (id,))
        connection.commit()
        
    def get_atendimentos_by_cliente_id(self, cliente_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM atendimento WHERE cliente_id = ?", (cliente_id,))
        return cursor.fetchall()
