from Interface import Interface

class Ganho(Interface):
    """
    Classe que representa um ganho, herdando de uma interface genérica.
    """
    # Atributos esperados:
    # valor: float - valor monetário do ganho.
    # data: datetime - data em que o ganho foi recebido.
    # categoria: str - categoria do ganho (ex.: salário, bônus, etc.).
    
    def detalhes(self) -> str:
        """
        Retorna os detalhes do ganho formatados em uma string.
        
        :return: Uma string contendo o valor, data e categoria do ganho.
        """
        return f"Ganho de R${self.valor} em {self.data.strftime('%d/%m/%Y')} na categoria {self.categoria}"
