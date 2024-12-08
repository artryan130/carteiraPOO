from datetime import datetime

class Transacao:
    """
    Classe que representa uma transação financeira genérica, contendo valor, categoria e data.
    """

    def __init__(self, valor: float, categoria: str, data: datetime = None):
        """
        Inicializa uma transação com valor, categoria e data.

        :param valor: Valor monetário da transação (deve ser positivo).
        :param categoria: Categoria da transação (ex.: alimentação, salário, etc.).
        :param data: Data da transação. Se não fornecida, assume o momento atual.
        """
        self.valor: float = valor  # Atribui o valor validado pelo setter.
        self.categoria: str = categoria  # Atribui a categoria validada pelo setter.
        self.data: datetime = data or datetime.now()  # Define a data, padrão para o momento atual.

    @property
    def valor(self) -> float:
        """
        Getter para o atributo 'valor'.
        
        :return: O valor da transação.
        """
        return self._valor

    @valor.setter
    def valor(self, novo_valor: float) -> None:
        """
        Setter para o atributo 'valor'. Valida se o valor é positivo e numérico.

        :param novo_valor: Novo valor para a transação.
        :raises ValueError: Se o valor não for um número positivo.
        """
        if isinstance(novo_valor, (int, float)) and novo_valor > 0:
            self._valor = novo_valor
        else:
            raise ValueError("O valor deve ser um número positivo")

    @property
    def categoria(self) -> str:
        """
        Getter para o atributo 'categoria'.
        
        :return: A categoria da transação.
        """
        return self._categoria

    @categoria.setter
    def categoria(self, nova_categoria: str) -> None:
        """
        Setter para o atributo 'categoria'. Define o valor fornecido sem validação adicional.

        :param nova_categoria: Nova categoria para a transação.
        """
        self._categoria = nova_categoria
