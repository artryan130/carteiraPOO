import os
import json
from Usuario import Usuario

class SistemaFinanceiro:
    """
    Classe responsável por gerenciar o sistema financeiro, incluindo login de usuários
    e carregamento de categorias de ganhos e despesas.
    """

    # Categorias serão carregadas uma única vez como atributos de classe
    categorias_ganhos = []
    categorias_despesas = []

    def __init__(self):
        """
        Inicializa o sistema financeiro com o estado inicial.
        """
        self.usuario_atual: Usuario = None  # Usuário atualmente logado.

    def login(self, nome: str, senha: str) -> None:
        """
        Realiza o login do usuário, verificando se o arquivo JSON correspondente existe.

        :param nome: Nome do usuário.
        :param senha: Senha do usuário.
        """
        caminho: str = f"dados_clientes/{nome}_{senha}.json"  # Caminho do arquivo de dados do usuário.
        if os.path.exists(caminho):
            self.usuario_atual = Usuario(nome, senha)  # Cria um objeto Usuario para o usuário atual.
            print(f"Bem-vindo, {self.usuario_atual.nome}!")  # Saudação ao usuário logado.
        else:
            print("Usuário ou senha incorretos. Tente novamente.")  # Mensagem de erro.
            self.usuario_atual = None  # Reseta o usuário atual.

    @classmethod
    def carregar_categorias(cls) -> None:
        """
        Carrega categorias de ganhos e despesas a partir de um arquivo JSON.
        """
        caminho: str = "categorias.json"  # Caminho do arquivo de categorias.

        if not os.path.exists(caminho):
            print("Erro: O arquivo 'categorias.json' não foi encontrado.")
            return

        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                categorias = json.load(arquivo)  # Lê o JSON e converte em dicionário
                cls.categorias_ganhos = categorias.get("categorias_ganhos", [])  # Obtém categorias de ganhos
                cls.categorias_despesas = categorias.get("categorias_despesas", [])  # Obtém categorias de despesas
        except json.JSONDecodeError:
            print("Erro: O arquivo 'categorias.json' contém dados inválidos.")

# Carregar categorias automaticamente ao iniciar o sistema
SistemaFinanceiro.carregar_categorias()
