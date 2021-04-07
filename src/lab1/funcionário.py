from pessoa import *

class Funcionário(Pessoa):
    def __init__(self, nome, numero):
        super().__init__(nome)
        self.numero = str(numero)

    def obter_numero(self):
        print(self.numero)

