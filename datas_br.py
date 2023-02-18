from datetime import datetime


class DataBr:

    def __init__(self):
        self.momento_cadastro()

    def __str__(self):
        return self.formata_data()

    @staticmethod
    def momento_cadastro():
        return datetime.today()

    def formata_data(self):
        data_formatada = self.momento_cadastro().strftime("%d/%m/%Y/ %H:%M")
        return data_formatada
