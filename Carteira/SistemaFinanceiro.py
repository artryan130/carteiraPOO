import os
from Usuario import Usuario
import json

class SistemaFinanceiro:
    """
    Classe responsável por gerenciar o sistema financeiro, incluindo login de usuários
    e carregamento de categorias de ganhos e despesas.
    """

    def __init__(self):
        """
        Inicializa o sistema financeiro com o estado inicial.
        """
        self.usuario_atual: Usuario = None  # Usuário atualmente logado.
        self.categorias_ganhos: list[str] = []  # Lista de categorias de ganhos.
        self.categorias_despesas: list[str] = []  # Lista de categorias de despesas.

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

    def carregar_categorias(self) -> None:
        """
        Carrega categorias de ganhos e despesas a partir de um arquivo JSON.
        """
        caminho: str = "categorias.json"  # Caminho do arquivo de categorias.
        if os.path.exists(caminho):
            with open(caminho, "r", encoding="utf-8") as arquivo:
                categorias: dict = json.load(arquivo)  # Lê o conteúdo do arquivo JSON.
                self.categorias_ganhos = categorias.get("categorias_ganhos", [])  # Obtém categorias de ganhos.
                self.categorias_despesas = categorias.get("categorias_despesas", [])  # Obtém categorias de despesas.
        else:
            print("Arquivo de categorias não encontrado. Verifique se 'categorias.json' existe.")  # Mensagem de erro.
