import pytest
from .main import Database, CommandHandler, QueryHandler, AddProductCommand, UpdateProductPriceCommand, \
    GetProductByIdQuery


@pytest.fixture
def setup_database():
    # Inicializa o banco de dados e os handlers para os testes
    db = Database()
    command_handler = CommandHandler(db)
    query_handler = QueryHandler(db)
    return db, command_handler, query_handler


def test_add_product_command(setup_database):
    db, command_handler, query_handler = setup_database

    # Adiciona um produto
    command_handler.handle(AddProductCommand(1, "Notebook", 3500))

    # Verifica se o produto foi adicionado
    product = query_handler.handle(GetProductByIdQuery(1))
    assert product['name'] == "Notebook"
    assert product['price'] == 3500


def test_update_product_price_command(setup_database):
    db, command_handler, query_handler = setup_database

    # Adiciona um produto
    command_handler.handle(AddProductCommand(1, "Notebook", 3500))

    # Atualiza o preço do produto
    command_handler.handle(UpdateProductPriceCommand(1, 3000))

    # Verifica se o preço foi atualizado
    product = query_handler.handle(GetProductByIdQuery(1))
    assert product['price'] == 3000


def test_get_product_by_id_query_not_found(setup_database):
    db, command_handler, query_handler = setup_database

    # Tenta buscar um produto que não existe
    result = query_handler.handle(GetProductByIdQuery(999))
    assert result == "Produto não encontrado."
