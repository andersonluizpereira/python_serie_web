# Simulando o banco de dados em memória
class Database:
    def __init__(self):
        self.products = {}


# Commands
class AddProductCommand:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class UpdateProductPriceCommand:
    def __init__(self, product_id, new_price):
        self.product_id = product_id
        self.new_price = new_price


class CommandHandler:
    def __init__(self, database):
        self.database = database

    def handle(self, command):
        if isinstance(command, AddProductCommand):
            self.database.products[command.product_id] = {
                'name': command.name,
                'price': command.price
            }
            print(f"Produto '{command.name}' adicionado com sucesso!")

        elif isinstance(command, UpdateProductPriceCommand):
            if command.product_id in self.database.products:
                self.database.products[command.product_id]['price'] = command.new_price
                print(f"Preço do produto atualizado para {command.new_price}!")
            else:
                print("Produto não encontrado para atualizar preço.")


# Queries
class GetProductByIdQuery:
    def __init__(self, product_id):
        self.product_id = product_id


class QueryHandler:
    def __init__(self, database):
        self.database = database

    def handle(self, query):
        if isinstance(query, GetProductByIdQuery):
            product = self.database.products.get(query.product_id, None)
            if product:
                return product
            else:
                return "Produto não encontrado."


# Exemplo de uso do CQRS
if __name__ == "__main__":
    # Criando banco de dados e handlers
    db = Database()
    command_handler = CommandHandler(db)
    query_handler = QueryHandler(db)

    # Executando comandos
    command_handler.handle(AddProductCommand(1, "Notebook", 3500))
    command_handler.handle(AddProductCommand(2, "Smartphone", 2000))
    command_handler.handle(UpdateProductPriceCommand(1, 3000))  # Atualizando preço

    # Executando consultas
    product = query_handler.handle(GetProductByIdQuery(1))
    print("Consulta Produto 1:", product)

    product = query_handler.handle(GetProductByIdQuery(3))  # Produto que não existe
    print("Consulta Produto 3:", product)
