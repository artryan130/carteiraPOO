from Transacao import Transacao

class Despesa(Transacao):
    def detalhes(self):
        return f"Despesa de R${self.valor} em {self.data.strftime('%d/%m/%Y')} na categoria {self.categoria}"