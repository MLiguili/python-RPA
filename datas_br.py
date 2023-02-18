from datetime import datetime, timedelta
class Data_Br:

    def __init__(self):
        data_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def momento_cadastro(self):
        return datetime.today()

    def formata_data(self):
        data_formatada = self.momento_cadastro().strftime("%d/%m/%Y/ %H:%M")
        return data_formatada

    def tempo_cadastro(self) -> object:
        agora = datetime.today() + timedelta(days=15, minutes=20,seconds=30)
        return agora - self.tempo_cadastro()



