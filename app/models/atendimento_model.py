class AtendimentoModel:
    def __init__(self, id, data, hora, motivo, cliente_id):
        self.__id = id
        self.__data = data
        self.__hora = hora
        self.__motivo = motivo
        self.__cliente_id = cliente_id
        
    def get_id(self):
        return self.__id
    
    def get_data(self):
        return self.__data
    
    def get_hora(self):
        return self.__hora
    
    def get_motivo(self):
        return self.__motivo
    
    def get_cliente_id(self):
        return self.__cliente_id
    
    def set_id(self, id):
        self.__id = id
        
    def set_data(self, data):
        self.__data = data
        
    def set_hora(self, hora):
        self.__hora = hora
    
    def set_motivo(self, motivo):
        self.__motivo = motivo
    
    def set_cliente_id(self, cliente_id):
        self.__cliente_id = cliente_id