from funcionário import *

class Vendedor(Funcionário):
    def __init__(self, nome, numero):
        super().__init__(nome, numero)
        self.faturas = []
        self.numero = str(numero)

    def obter_todas_faturas(self):
        return self.faturas

    def obter_faturas(self, inicio, fim):
        pass


