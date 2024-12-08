from Interface import Interface

class Despesa(Interface):
    """
    Classe que representa uma despesa, herdando de uma interface genérica.
    """
    # Atributos esperados:
    # valor: float - valor monetário da despesa.
    # data: datetime - data em que a despesa foi realizada.
    # categoria: str - categoria da despesa (ex.: alimentação, transporte, etc.).
    
    def detalhes(self) -> str:
        """
        Retorna os detalhes da despesa formatados em uma string.
        
        :return: Uma string contendo o valor, data e categoria da despesa.
        """
        return f"Despesa de R${self.valor} em {self.data.strftime('%d/%m/%Y')} na categoria {self.categoria}"
