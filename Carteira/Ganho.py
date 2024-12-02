from Transacao import Transacao

class Ganho(Transacao):
    def detalhes(self):
        return f"Ganho de R${self.valor} em {self.data.strftime('%d/%m/%Y')} na categoria {self.categoria}"