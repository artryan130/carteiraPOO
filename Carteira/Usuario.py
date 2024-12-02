import os
import json
from Despesa import Despesa
from Ganho import Ganho
from datetime import datetime
import matplotlib.pyplot as plt

class Usuario:
    def __init__(self, nome, senha):
        self._nome = nome
        self._senha = senha
        self.transacoes = []
        self.carregar_dados()

    @property
    def nome(self):
        return self._nome

    @property
    def senha(self):
        return self._senha

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
        self.salvar_dados()

    def calcular_saldo(self):
        saldo = 0
        for transacao in self.transacoes:
            if isinstance(transacao, Ganho):
                saldo += transacao.valor
            elif isinstance(transacao, Despesa):
                saldo -= transacao.valor
        return saldo

    def salvar_dados(self):
        dados = {
            'transacoes': [self._transacao_para_dict(t) for t in self.transacoes]
        }
        diretorio = 'dados_clientes'
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        with open(f"{diretorio}/{self.nome}_{self.senha}.json", 'w') as f:
            json.dump(dados, f, default=str)

    def carregar_dados(self):
        caminho = f"dados_clientes/{self.nome}_{self.senha}.json"
        if os.path.exists(caminho):
            with open(caminho, 'r') as f:
                dados = json.load(f)
                self.transacoes = [self._dict_para_transacao(t) for t in dados['transacoes']]

    def _transacao_para_dict(self, transacao):
        return {
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'categoria': transacao.categoria,
            'data': transacao.data.isoformat()
        }

    def _dict_para_transacao(self, dados):
        classe = Ganho if dados['tipo'] == 'Ganho' else Despesa
        data = datetime.fromisoformat(dados['data'])
        return classe(dados['valor'], dados['categoria'], data)

    def gerar_grafico(self):
        categorias_despesas = {}
        categorias_ganhos = {}

        # Separar valores de despesas e ganhos por categoria
        for transacao in self.transacoes:
            if isinstance(transacao, Despesa):
                categorias_despesas[transacao.categoria] = categorias_despesas.get(transacao.categoria, 0) + transacao.valor
            elif isinstance(transacao, Ganho):  # Supondo que 'Ganho' seja a classe para receitas
                categorias_ganhos[transacao.categoria] = categorias_ganhos.get(transacao.categoria, 0) + transacao.valor

        # Plotar despesas
        if categorias_despesas:
            plt.figure(figsize=(10, 5))
            plt.subplot(1, 2, 1)
            plt.pie(categorias_despesas.values(), labels=categorias_despesas.keys(), autopct='%1.1f%%')
            plt.title('Despesas por Categoria')
        else:
            print("Nenhuma despesa registrada para gerar gráfico.")

        # Plotar ganhos
        if categorias_ganhos:
            plt.subplot(1, 2, 2)
            plt.pie(categorias_ganhos.values(), labels=categorias_ganhos.keys(), autopct='%1.1f%%')
            plt.title('Ganhos por Categoria')
        else:
            print("Nenhum ganho registrado para gerar gráfico.")

        # Mostrar gráficos
        if categorias_despesas or categorias_ganhos:
            plt.tight_layout()
            plt.show()

    def mostrar_historico(self, data_inicial, data_final):
        historico = []
        for transacao in self.transacoes:
            if data_inicial <= transacao.data.date() <= data_final:
                historico.append(transacao.detalhes())
        if historico:
            for item in historico:
                print(item)
        else:
            print("Nenhuma transação no período especificado.")