from funcionário import *

class Gestor(Funcionário):
    def __init__(self, nome, numero):
        super().__init__(numero, nome)
