# CQRS Example with Python and SQLite

Este é um exemplo simples de uma aplicação CQRS (Command Query Responsibility Segregation) usando Python. O código simula um banco de dados em memória e implementa comandos para adicionar e atualizar produtos, além de consultas para recuperar informações de produtos.

## Estrutura do Projeto


### 1. `main.py`

Este arquivo contém a implementação dos comandos (commands) e consultas (queries) no padrão CQRS. Simula um banco de dados em memória que armazena produtos com informações como nome e preço.

### 2. `test_main.py`

Este arquivo contém testes de unidade escritos com o framework `pytest`, que validam o comportamento dos comandos e consultas no código.

---

## Requisitos

- **Python 3.x** 
- **pytest** para rodar os testes unitários.

### Instalação do `pytest`

Caso o `pytest` não esteja instalado, você pode instalá-lo executando o seguinte comando no terminal:

```bash
pip install pytest
```
# Como executar o código
### Clone ou baixe o repositório para o seu ambiente local.

Navegue até o diretório do projeto:
cd cqrs_app

```bash
cd cqrs_lite
```

Execute o script principal cqrs.py para ver a simulação de adição, atualização e consulta de produtos:

```bash
python main.py
```
# Como executar os testes
Os testes foram escritos utilizando o framework pytest para validar o comportamento do código CQRS.

Para rodar todos os testes de unidade, basta executar o comando:
```bash
pytest test_main.py
```

# Estrutura CQRS Implementada
## Comandos (Commands):

#### AddProductCommand: Adiciona um novo produto ao sistema.

#### UpdateProductPriceCommand: Atualiza o preço de um produto existente.

## Consultas (Queries):
#### GetProductByIdQuery: Consulta os detalhes de um produto com base em seu ID. Handlers:

#### CommandHandler: Responsável por executar comandos. QueryHandler: Responsável por executar consultas.
