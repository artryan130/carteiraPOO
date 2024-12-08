import os
import json
from Despesa import Despesa
from Ganho import Ganho
from datetime import datetime
import matplotlib.pyplot as plt
from typing import Union

class Usuario:
    def __init__(self, nome: str, senha: str):
        """
        Inicializa um objeto da classe Usuario.

        Args:
            nome (str): Nome do usuário.
            senha (str): Senha do usuário.
        """
        self._nome: str = nome
        self._senha: str = senha
        self.transacoes: list = []  # Lista de transações (Ganho ou Despesa)
        self.carregar_dados()

    @property
    def nome(self) -> str:
        """
        Retorna o nome do usuário.
        """
        return self._nome

    @property
    def senha(self) -> str:
        """
        Retorna a senha do usuário.
        """
        return self._senha
    
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        """
        Atualiza o nome do usuário.

        Args:
            novo_nome (str): Novo nome do usuário.
        """
        self.nome = novo_nome
    
    @senha.setter
    def senha(self, nova_senha: str) -> None:
        """
        Atualiza a senha do usuário.

        Args:
            nova_senha (str): Nova senha do usuário.
        """
        self._senha = nova_senha

    def adicionar_transacao(self, transacao) -> None:
        """
        Adiciona uma nova transação ao usuário.

        Args:
            transacao (Ganho ou Despesa): Transação a ser adicionada.
        """
        self.transacoes.append(transacao)
        self.salvar_dados()

    def calcular_saldo(self) -> float:
        """
        Calcula o saldo total do usuário.

        Returns:
            float: Saldo total considerando ganhos e despesas.
        """
        saldo: float = 0
        for transacao in self.transacoes:
            if isinstance(transacao, Ganho):
                saldo += transacao.valor
            elif isinstance(transacao, Despesa):
                saldo -= transacao.valor
        return saldo

    def salvar_dados(self) -> None:
        """
        Salva as transações do usuário em um arquivo JSON.
        """
        dados: dict = {
            'transacoes': [self._transacao_para_dict(t) for t in self.transacoes]
        }
        diretorio: str = 'dados_clientes'
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        with open(f"{diretorio}/{self.nome}_{self.senha}.json", 'w') as f:
            json.dump(dados, f, default=str)

    def carregar_dados(self) -> None:
        """
        Carrega as transações do usuário a partir de um arquivo JSON.
        """
        caminho: str = f"dados_clientes/{self.nome}_{self.senha}.json"
        if os.path.exists(caminho):
            with open(caminho, 'r') as f:
                dados = json.load(f)
                self.transacoes = [self._dict_para_transacao(t) for t in dados['transacoes']]

    def _transacao_para_dict(self, transacao) -> dict:
        """
        Converte uma transação para o formato de dicionário.

        Args:
            transacao (Ganho ou Despesa): Transação a ser convertida.

        Returns:
            dict: Representação da transação como dicionário.
        """
        return {
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'categoria': transacao.categoria,
            'data': transacao.data.isoformat()
        }

    def _dict_para_transacao(self, dados: dict) -> Union[Ganho, Despesa]:
        """
        Converte um dicionário em uma transação.

        Args:
            dados (dict): Dicionário contendo os dados da transação.

        Returns:
            Ganho ou Despesa: Objeto transação reconstruído.
        """
        classe = Ganho if dados['tipo'] == 'Ganho' else Despesa
        data = datetime.fromisoformat(dados['data'])
        return classe(dados['valor'], dados['categoria'], data)

    def gerar_grafico(self) -> None:
        """
        Gera gráficos de pizza mostrando a distribuição de ganhos e despesas por categoria.
        """
        categorias_despesas: dict = {}
        categorias_ganhos: dict = {}

        # Separar valores de despesas e ganhos por categoria
        for transacao in self.transacoes:
            if isinstance(transacao, Despesa):
                categorias_despesas[transacao.categoria] = categorias_despesas.get(transacao.categoria, 0) + transacao.valor
            elif isinstance(transacao, Ganho):  # Supondo que 'Ganho' seja a classe para receitas
                categorias_ganhos[transacao.categoria] = categorias_ganhos.get(transacao.categoria, 0) + transacao.valor

        def gerar_legenda(categorias: dict) -> list:
            """
            Gera legendas para os gráficos.

            Args:
                categorias (dict): Dicionário com categorias e valores.

            Returns:
                list: Lista de strings representando as legendas.
            """
            legendas: list = []
            for categoria, valor in categorias.items():
                legendas.append(f"{categoria}: R$ {valor:.2f}")
            return legendas

        # Plotar despesas
        if categorias_despesas:
            plt.figure(figsize=(12, 6))
            plt.subplot(1, 2, 1)
            valores = list(categorias_despesas.values())
            labels = list(categorias_despesas.keys())
            plt.pie(valores, labels=None, autopct='%1.1f%%')
            plt.title('Despesas por Categoria')
            legendas_despesas = gerar_legenda(categorias_despesas)
            plt.legend(legendas_despesas, title="Categorias", loc="best", bbox_to_anchor=(0.85, 0.5))
        else:
            print("Nenhuma despesa registrada para gerar gráfico.")

        # Plotar ganhos
        if categorias_ganhos:
            plt.subplot(1, 2, 2)
            valores = list(categorias_ganhos.values())
            labels = list(categorias_ganhos.keys())
            plt.pie(valores, labels=None, autopct='%1.1f%%')
            plt.title('Ganhos por Categoria')
            legendas_ganhos = gerar_legenda(categorias_ganhos)
            plt.legend(legendas_ganhos, title="Categorias", loc="best", bbox_to_anchor=(0.85, 0.5))
        else:
            print("Nenhum ganho registrado para gerar gráfico.")

        # Mostrar gráficos
        if categorias_despesas or categorias_ganhos:
            plt.tight_layout()
            plt.show()

    def mostrar_historico(self, data_inicial: datetime.date, data_final: datetime.date) -> None:
        """
        Exibe o histórico de transações em um período.

        Args:
            data_inicial (datetime.date): Data inicial do intervalo.
            data_final (datetime.date): Data final do intervalo.
        """
        historico: list = []
        for transacao in self.transacoes:
            if data_inicial <= transacao.data.date() <= data_final:
                historico.append(transacao.detalhes())
        if historico:
            for item in historico:
                print(item)
        else:
            print("Nenhuma transação no período especificado.")
