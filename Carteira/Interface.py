from abc import ABC, abstractmethod
from datetime import datetime

class Interface(ABC):
    """
    Classe abstrata que define a interface base para diferentes tipos de transações financeiras,
    como despesas e ganhos.
    """
    
    def __init__(self, valor: float, categoria: str, data: datetime = None):
        """
        Inicializa uma instância da interface com um valor, categoria e data.
        
        :param valor: Valor monetário da transação (ex.: despesa ou ganho).
        :param categoria: Categoria da transação (ex.: alimentação, salário, etc.).
        :param data: Data da transação. Se não fornecida, será definida como o momento atual.
        """
        self.valor: float = valor  # Valor monetário da transação.
        self.categoria: str = categoria  # Categoria da transação.
        self.data: datetime = data or datetime.now()  # Data da transação, padrão para o momento atual.

    @abstractmethod
    def detalhes(self) -> str:
        """
        Método abstrato que deve ser implementado pelas classes derivadas para descrever os detalhes da transação.
        
        :return: Uma string com os detalhes formatados da transação.
        """
        pass
