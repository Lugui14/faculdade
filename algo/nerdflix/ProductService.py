from ProductRepo import ProductRepo

#Regras de negócio dos produtos
class ProductService:
    def __init__(self):
        self.repo = ProductRepo

    #Pega todos os produtos
    def getAll(self) -> dict:
        produtos = self.repo.getAll()
        return produtos

    #Busca um produto
    def getOne(self, codigo: str) -> dict or str:
        if codigo not in self.repo.getAll().keys():
            print("Produto não cadastrado.")
            return
        return self.repo.getOne(codigo)

    #Criar produto
    def add(self, codigo: str, nome: str, tipo: int, preco: float, vendivel: int) -> dict or None:
        #Validação dos dados
        if preco == None or preco <= 0:
            print("\nDigite um preço valido.")
            return 
        if tipo == None or tipo < 1 or tipo > 3:
            print("\nDigite um tipo valido!")
            return
        if codigo == None or codigo in self.repo.getAll().keys():
            print("\nCodigo de produto já existente ou é invalido.")
            return 
        if vendivel == None or vendivel != 1 and vendivel != 2:
            print("\nDigite um valor valido para disponibilidade de venda.")
            return
        if nome == None or len(nome) < 1:
            print("\nNome invalido.")
            return

        #formatar preco    
        novoPreco = round(preco, 2)
        #formatar disponibilidade
        if vendivel == 1:
            dispo = True
        else:
            dispo = False

        produto = {'codigo': codigo, 'nome': nome, 'tipo': tipo, 'preco': novoPreco, 'disponibilidade': dispo}
        self.repo.add(produto)
        return produto

    #Atualizar produto
    def update(self, codigo: str, nome: str or None, tipo: int or None, preco: float or None, vendivel: int or None) -> dict or None:
        #Validando dados
        if type(tipo) == str or type(preco) == str or type(vendivel) == str:
            print("\nErro na tipagem dos dados.")
            return
        if codigo not in self.repo.getAll().keys():
            print("\nProduto não cadastrado.")
            return
        if tipo != None:
            if tipo < 1 or tipo > 3:
                print("\nDigite um tipo valido.")
                return
        if preco != None:
            if preco <= 0:
                print("\nDigite um preço valido.")
                return
        if vendivel != None:
            if vendivel != 1 and vendivel != 2:
                print("\nDigite um valor valido para disponibilidade de venda.")
                return
        
        #formatar preco    
        novoPreco = round(preco, 2)
        #formatar disponibilidade
        if vendivel == 1:
            dispo = True
        else:
            dispo = False

        produto = self.repo.update(codigo, nome, tipo, preco, dispo)
        return produto
        
    #Deleta um produto
    def delete(self, codigo: str):
        #Regras de negócio
        if codigo not in self.repo.getAll().keys():
            print("Produto não cadastrado.")
            return 
        self.repo.delete(codigo)