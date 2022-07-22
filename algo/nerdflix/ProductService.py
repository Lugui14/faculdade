#CRUD de serviços
class ProductService:

    def __init__(self, listaDeProdutos: dict):
        self.listaDeProdutos = listaDeProdutos

    #Todos os produtos
    def readAll(self) -> dict:
        return self.listaDeProdutos

    #Busca um produto
    def read(self, codigo: str) -> dict or str:
        if codigo in self.listaDeProdutos.keys():
            return self.listaDeProdutos[codigo]
        return "Produto não cadastrado."

    #Criar produto
    def create(self, codigo: str, nome: str, tipo: int, preco: float, vendivel: bool) -> dict or str:
        #Regras de negócio
        if preco <= 0:
            return "Digite um preço valido."
        if tipo < 1 or tipo > 3:
            return "Digite um tipo valido!"
        if codigo in self.listaDeProdutos.keys():
            return "Codigo de produto ja existente."
        #formatar preco    
        novoPreco = round(preco, 2)

        product = {'codigo': codigo, 'nome': nome, 'tipo': tipo, 'preco': novoPreco, 'vendivel': vendivel}
        self.listaDeProdutos[codigo] = product
        return product

    #Atualizar produto
    def update(self, codigo: str, opcao: int, val) -> dict or str:
        #Regras de negócio
        if codigo not in self.listaDeProdutos.keys():
            return "Produto não cadastrado."
        
        if opcao == 1 and type(val) == str:
            self.listaDeProdutos[codigo][nome] = val
            return self.listaDeProdutos[codigo]
        elif opcao == 2 and type(val) == int:
            self.listaDeProdutos[codigo][tipo] = val
            return self.listaDeProdutos[codigo]
        elif opcao == 3 and type(val) == float:
            self.listaDeProdutos[codigo][preco] = val
            return self.listaDeProdutos[codigo]
        elif opcao == 4 and type(val) == bool:
            self.listaDeProdutos[codigo][vendivel] = val
            return self.listaDeProdutos[codigo]
        else:
            return "Digite uma opção valida com a tipagem correta."

    #Deleta um produto
    def delete(self, codigo: str):
        #Regras de negócio
        if codigo not in self.listaDeProdutos.keys():
            return "Produto não cadastrado."

        self.listaDeProdutos.pop(codigo)