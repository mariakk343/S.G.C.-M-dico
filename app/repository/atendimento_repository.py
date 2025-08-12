from app.database.connection import get_db
from app.models.atendimento_model import AtendimentoModel

class AtendimentoRepository:
    
    def get_all_atendimentos(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT a.id, a.data, a.hora, a.motivo, a.cliente_id, c.nome
            FROM atendimento a
            JOIN cliente c ON a.cliente_id = c.id
        """)
        rows = cursor.fetchall()
        atendimentos = []
        for row in rows:
            atendimento = AtendimentoModel(
                id=row[0],
                data=row[1],
                hora=row[2],
                motivo=row[3],
                cliente_id=row[4]
            )
            atendimento.cliente_nome = row[5]
            atendimentos.append(atendimento)
        return atendimentos
    
    def get_atendimento_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT a.id, a.data, a.hora, a.motivo, a.cliente_id, c.nome
            FROM atendimento a
            JOIN cliente c ON a.cliente_id = c.id
            WHERE a.id = ?
        """, (id,))
        row = cursor.fetchone()
        if row:
            atendimento = AtendimentoModel(
                id=row[0],
                data=row[1],
                hora=row[2],
                motivo=row[3],
                cliente_id=row[4]
            )
            atendimento.cliente_nome = row[5]
            return atendimento
        return None
        
    def create_atendimento(self, atendimento):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO atendimento (data, hora, motivo, cliente_id)
            VALUES (?, ?, ?, ?)
        """, (
            atendimento.get_data(),
            atendimento.get_hora(),
            atendimento.get_motivo(),
            atendimento.get_cliente_id()
        ))
        connection.commit()
        
    def update_atendimento(self, atendimento):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE atendimento
            SET data = ?, hora = ?, motivo = ?, cliente_id = ?
            WHERE id = ?
        """, (
            atendimento.get_data(),
            atendimento.get_hora(),
            atendimento.get_motivo(),
            atendimento.get_cliente_id(),
            atendimento.get_id()
        ))
        connection.commit()
        
    def delete_atendimento(self, atendimento_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM atendimento WHERE id = ?", (atendimento_id,))
        connection.commit()
