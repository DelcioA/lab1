class Data:
    def __init__(self, ano, mes, dia):
        self.ano = int(ano)
        self.mes = int(mes)
        self.dia = int(dia)

    def obter_ano(self):
        return self.ano

    def obter_mes(self):
        return self.mes

    def obter_dia(self):
        return self.dia