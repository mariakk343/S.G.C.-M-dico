class ClienteModel:
    def __init__(self, id, nome, telefone, data_nascimento):
        self.__id = id
        self.__nome = nome
        self.__telefone = telefone
        self.__data_nascimento = data_nascimento
        
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_data_nascimento(self):
        return self.__data_nascimento
    
    def get_telefone(self):
        return self.__telefone
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
    
    def set_telefone(self, telefone):
        self.__telefone = telefone
    
    