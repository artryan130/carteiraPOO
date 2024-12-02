from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
    def __init__(self, valor, categoria, data=None):
        self.valor = valor
        self.categoria = categoria
        self.data = data or datetime.now()

    @abstractmethod
    def detalhes(self):
        pass

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        if isinstance(novo_valor, (int, float)) and novo_valor > 0:
            self._valor = novo_valor
        else:
            raise ValueError("O valor deve ser um número positivo")

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, nova_categoria):
        self._categoria = nova_categoria