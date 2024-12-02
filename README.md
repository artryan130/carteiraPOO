# Sistema Financeiro

Um sistema financeiro desenvolvido em Python, com foco em controle de ganhos e despesas. O sistema utiliza JSON para persistência de dados e Matplotlib para geração de gráficos.

## Funcionalidades

- **Cadastro e Login de Usuários**: Os dados são armazenados em arquivos JSON, permitindo acesso seguro e individualizado.
- **Gerenciamento de Transações**: Adicione ganhos e despesas, categorizando-os de forma organizada.
- **Cálculo de Saldo**: Visualize o saldo atual com base nas transações cadastradas.
- **Histórico de Transações**: Filtre e exiba transações por período.
- **Gráficos**: Geração de gráficos para análise de ganhos e despesas por categoria.

## Estrutura do Projeto

O projeto é estruturado com classes e organização modular, cada módulo tem sua função específica:

- `Transacao`: Classe base abstrata que representa uma transação financeira.
- `Ganho`: Representa um ganho financeiro, herdando da classe `Transacao`.
- `Despesa`: Representa uma despesa financeira, herdando da classe `Transacao`.
- `Usuario`: Gerencia os dados de um usuário, incluindo suas transações.
- `SistemaFinanceiro`: Controla a lógica principal do sistema, como login, cadastro e acesso ao usuário atual.

## Como Usar

### Pré-requisitos

- Python 3.x instalado.

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://https://github.com/artryan130/CampoMinadoPOO

2. Navegue até o diretório do projeto:
   ```bash
   cd JogoCampoMinadoPOO

3. Execute o jogo:
   ```bash
   python main.py


## Funcionalidades do Sistema

### Menu Principal

- **[1] Adicionar Ganho**: Registra um ganho financeiro, escolhendo uma categoria e valor.
- **[2] Adicionar Despesa**: Registra uma despesa financeira, escolhendo uma categoria e valor.
- **[3] Mostrar Saldo**: Calcula e exibe o saldo atual do usuário.
- **[4] Mostrar Histórico**: Filtra e exibe as transações em um intervalo de datas.
- **[5] Gerar Gráfico**: Exibe gráficos de ganhos e despesas por categoria.
- **[6] Sair**: Fecha o sistema.

### Cadastro e Login

- Para cadastrar, insira um nome e uma senha. O sistema verifica se o usuário já existe.
- Faça login com o nome e senha cadastrados para acessar suas transações.

### Gráficos

Os gráficos mostram a distribuição percentual de ganhos e despesas por categoria. São gerados automaticamente com base nas transações cadastradas.

## Estrutura de Arquivos

- **Transacao**: Classe abstrata para representar uma transação.
- **Ganho e Despesa**: Subclasses que implementam transações específicas.
- **Usuario**: Gerencia dados e transações de um usuário.
- **SistemaFinanceiro**: Controla a lógica principal do sistema.
- **main.py**: Ponto de entrada do programa.

## Imagens do Sistema

### Gráfico de Categorias

*Imagem ilustrativa de um gráfico de categorias gerado pelo sistema.*

### Histórico de Transações

*Imagem ilustrativa do histórico de transações filtrado por data.*

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório.
