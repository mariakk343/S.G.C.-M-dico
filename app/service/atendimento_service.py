from datetime import datetime, date
from app.repository.atendimento_repository import AtendimentoRepository
from app.models.atendimento_model import AtendimentoModel
from app.repository.cliente_repository import ClienteRepository

class AtendimentoService:
    def __init__(self):
        self.atendimento_repository = AtendimentoRepository()
        self.cliente_repository = ClienteRepository()

    def get_all_atendimentos(self):
        return self.atendimento_repository.get_all_atendimentos()
    
    def get_atendimento_by_id(self, atendimento_id):
        if atendimento_id is None:
            raise ValueError("O ID do atendimento não pode ser None.")
        return self.atendimento_repository.get_atendimento_by_id(atendimento_id)
    
    def create_atendimento(self, atendimento: AtendimentoModel):
        if atendimento.get_id() is not None:
            raise ValueError("Não é possível criar um atendimento com ID já definido.")
        if not atendimento.get_data() or not atendimento.get_motivo():
            raise ValueError("Data e motivo do atendimento são obrigatórios.")
        if len(atendimento.get_motivo()) < 3:
            raise ValueError("O motivo deve ter pelo menos 3 caracteres.")
        if not self.cliente_repository.get_cliente_by_id(atendimento.get_cliente_id()):
            raise ValueError("O cliente informado não existe.")
        atendimento.set_data(self.validar_data_atendimento(atendimento.get_data()))
        self.atendimento_repository.create_atendimento(atendimento)
        
    def update_atendimento(self, atendimento: AtendimentoModel):
        if atendimento.get_id() is None:
            raise ValueError("O ID do atendimento não pode ser None.")
        if not atendimento.get_data() or not atendimento.get_motivo():
            raise ValueError("Data e motivo do atendimento são obrigatórios.")
        if len(atendimento.get_motivo()) < 3:
            raise ValueError("O motivo deve ter pelo menos 3 caracteres.")
        if not self.cliente_repository.get_cliente_by_id(atendimento.get_cliente_id()):
            raise ValueError("O cliente informado não existe.")

        atendimento.set_data(self.validar_data_atendimento(atendimento.get_data()))

        self.atendimento_repository.update_atendimento(atendimento)
        
    def delete_atendimento(self, atendimento_id):
        if atendimento_id is None:
            raise ValueError("O ID do atendimento não pode ser None.")
        self.atendimento_repository.delete_atendimento(atendimento_id)
        
    def validar_data_atendimento(self, data_atendimento):
        if isinstance(data_atendimento, str):
            try:
                data_atendimento = datetime.strptime(data_atendimento, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Esse formato de data não é permitido, use o formato YYYY-MM-DD.")
        if not isinstance(data_atendimento, date):
            raise ValueError("A data do atendimento deve ser um objeto date válido.")
        hoje = date.today()
        if data_atendimento < hoje:
            raise ValueError("Não é possível marcar atendimentos para dias que já se passaram.")
        return data_atendimento
