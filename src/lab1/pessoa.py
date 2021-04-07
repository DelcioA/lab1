import abc

class Pessoa(abc.ABC):
    def __init__(self, nome):
        self.nome = nome

    def obter_nome(self):
        return self.nome
