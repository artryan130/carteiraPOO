import os
from Usuario import Usuario

class SistemaFinanceiro:

    categorias_ganhos = ["Salário", "Freelance", "Investimentos", "Presente", "Outros"]
    categorias_despesas = ["Alimentação", "Lazer", "Educação", "Transporte", "Saúde"]

    def __init__(self):
        self.usuario_atual = None

    def login(self, nome, senha):
        caminho = f"dados_clientes/{nome}_{senha}.json"
        if os.path.exists(caminho):
            self.usuario_atual = Usuario(nome, senha)
            print(f"Bem-vindo, {self.usuario_atual.nome}!")
        else:
            print("Usuário ou senha incorretos. Tente novamente.")
            self.usuario_atual = None