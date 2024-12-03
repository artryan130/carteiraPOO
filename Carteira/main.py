import os
from datetime import datetime
from SistemaFinanceiro import SistemaFinanceiro
from Usuario import Usuario
from Ganho import Ganho
from Despesa import Despesa

if __name__ == "__main__":

    sistema = SistemaFinanceiro()

print("Bem-vindo ao Sistema Financeiro!")

while True:
    opcao = input("Escolha uma opção: [1] Login, [2] Cadastro, [3] Sair: ")

    if opcao == "1":
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        sistema.login(nome, senha)
        if sistema.usuario_atual:
            print(f"Login bem-sucedido! Bem-vindo, {nome}.")
            break
        else:
            print("Login falhou. Tente novamente.")

    elif opcao == "2":
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")

        # Caminho da pasta onde os arquivos são armazenados
        pasta_dados = "dados_clientes"
        if not os.path.exists(pasta_dados):
            os.makedirs(pasta_dados)  # Garante que a pasta exista

        # Valida se já existe um arquivo com o nome do usuário
        arquivos_existentes = os.listdir(pasta_dados)
        if any(arquivo.startswith(f"{nome}_") for arquivo in arquivos_existentes):
            print("Usuário já existe. Por favor, escolha outro nome ou faça login.")
        else:
            # Cria o novo usuário
            sistema.usuario_atual = Usuario(nome, senha)
            sistema.usuario_atual.salvar_dados()  # Salva os dados iniciais do usuário
            print(f"Usuário {nome} cadastrado com sucesso!")
    
    elif opcao == "3":
        print("Saindo do sistema. Até mais!")
        exit()
    
    else:
        print("Opção inválida. Tente novamente.")

while True:
    print("\nMenu Principal")
    print("[1] Adicionar Ganho")
    print("[2] Adicionar Despesa")
    print("[3] Mostrar Saldo")
    print("[4] Mostrar Histórico")
    print("[5] Gerar Gráfico")
    print("[6] Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":  # Adicionar ganho
        print("Escolha a categoria do ganho:")
        for idx, categoria in enumerate(SistemaFinanceiro.categorias_ganhos, start=1):
            print(f"[{idx}] {categoria}")
        
        try:
            opcao_categoria = int(input("Digite o número da categoria: "))
            if 1 <= opcao_categoria <= len(SistemaFinanceiro.categorias_ganhos):
                categoria = SistemaFinanceiro.categorias_ganhos[opcao_categoria - 1]
                
                try:
                    valor = float(input("Digite o valor do ganho: "))
                    if valor > 0:
                        transacao = Ganho(valor, categoria)
                        sistema.usuario_atual.adicionar_transacao(transacao)
                        print("Ganho adicionado com sucesso!")
                    else:
                        print("O valor do ganho deve ser maior que zero.")
                except ValueError:
                    print("O valor deve ser um número válido.")
            else:
                print("Categoria inválida. Tente novamente.")
        except ValueError:
            print("Opção inválida. Digite um número correspondente à categoria.")

    elif escolha == "2":  # Adicionar despesa
        print("Escolha a categoria da despesa:")
        for idx, categoria in enumerate(SistemaFinanceiro.categorias_despesas, start=1):
            print(f"[{idx}] {categoria}")
        
        try:
            opcao_categoria = int(input("Digite o número da categoria: "))
            if 1 <= opcao_categoria <= len(SistemaFinanceiro.categorias_despesas):
                categoria = SistemaFinanceiro.categorias_despesas[opcao_categoria - 1]
                
                try:
                    valor = float(input("Digite o valor da despesa: "))
                    if valor > 0:
                        transacao = Despesa(valor, categoria)
                        sistema.usuario_atual.adicionar_transacao(transacao)
                        print("Despesa adicionada com sucesso!")
                    else:
                        print("O valor da despesa deve ser maior que zero.")
                except ValueError:
                    print("O valor deve ser um número válido.")
            else:
                print("Categoria inválida. Tente novamente.")
        except ValueError:
            print("Opção inválida. Digite um número correspondente à categoria.")

    elif escolha == "3":
        saldo = sistema.usuario_atual.calcular_saldo()
        print(f"Seu saldo atual é: R${saldo:.2f}")

    elif escolha == "4":
        try:
            data_inicio = input("Digite a data inicial (AAAA-MM-DD): ")
            data_fim = input("Digite a data final (AAAA-MM-DD): ")
            data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
            data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date()
            sistema.usuario_atual.mostrar_historico(data_inicio, data_fim)
        except ValueError:
            print("Formato de data inválido. Use AAAA-MM-DD.")

    elif escolha == "5":
        sistema.usuario_atual.gerar_grafico()

    elif escolha == "6":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
