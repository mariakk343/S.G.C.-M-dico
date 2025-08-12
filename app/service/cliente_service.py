from datetime import datetime, date
from app.repository.cliente_repository import ClienteRepository
from app.models.cliente_model import ClienteModel

class ClienteService:
    def __init__(self):
        self.cliente_repository = ClienteRepository()
        
    def validate_date(self, date_str):
        try:
            data_nascimento = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Data inválida. Use o formato YYYY-MM-DD.")
        
        hoje = date.today()
        if data_nascimento > hoje:
            raise ValueError("A data de nascimento não pode ser no futuro.")

        idade = hoje.year - data_nascimento.year - (
            (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
        )
        if idade > 130:
            raise ValueError("Idade inválida. Por favor, verifique a data de nascimento.")

        return data_nascimento

    def validate_cliente(self, cliente: ClienteModel):
        if not cliente.get_nome() or not cliente.get_data_nascimento() or not cliente.get_telefone():
            raise ValueError("Nome, data de nascimento e telefone são obrigatórios.")
        if len(cliente.get_nome()) < 3:
            raise ValueError("O nome do cliente deve ter pelo menos 3 caracteres.")
        if cliente.get_nome().isdigit():
            raise ValueError("O nome do cliente não pode ser apenas numérico.")
        cliente.set_data_nascimento(self.validate_date(cliente.get_data_nascimento()))

    def get_all_clientes(self):
        return self.cliente_repository.get_all_clientes()
    
    def get_cliente_by_id(self, cliente_id):
        if cliente_id is None:
            raise ValueError("O ID do cliente não pode ser None.")
        return self.cliente_repository.get_cliente_by_id(cliente_id)
    
    def create_cliente(self, cliente: ClienteModel):
        if cliente.get_id() is not None:
            raise ValueError("Não é possível criar um cliente com ID já definido.")
        self.validate_cliente(cliente)
        self.cliente_repository.create_cliente(cliente)
        
    def update_cliente(self, cliente: ClienteModel):
        if cliente.get_id() is None:
            raise ValueError("O ID do cliente não pode ser None.")
        self.validate_cliente(cliente)
        self.cliente_repository.update_cliente(cliente)
        
    def delete_cliente(self, cliente_id):
        if cliente_id is None:
            raise ValueError("O ID do cliente não pode ser None.")
        atendimentos = self.cliente_repository.get_atendimentos_by_cliente_id(cliente_id)
        if atendimentos:
            raise ValueError("Não é possível excluir um cliente que possui atendimentos agendados.")
        self.cliente_repository.delete_cliente(cliente_id)
