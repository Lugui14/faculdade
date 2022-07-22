from ProductService import ProductService

class ProductController:
    #define lista de produtos
    def __init__(self, produtos: dict):
        self.produtos = produtos
        self.productObj = ProductService(produtos)

    #executa controlador
    def execute(self, opcao: int):
        if opcao == 1:
            for produto in self.produtos.values():
                if produto['tipo'] == 1: 
                    tipo = "série"
                elif produto['tipo'] == 2:
                    tipo = "filme"
                else:
                    tipo = "documentário"

                print("---------------------------------------------------------------------------------------------------------------------")
                print(f"Codigo: {produto['codigo']} | Nome: {produto['nome']} | Tipo: {tipo} | Preço: R${produto['preco']} | Disponível: {produto['vendivel']}")
                print("---------------------------------------------------------------------------------------------------------------------")

        #Mostra um produto
        elif opcao == 2:
            produto = "Buscar Produto..."
            while type(produto) == str:
                print(produto)
                cod = input("Digite o codigo do produto para buscar: (0- voltar) ")
                if cod == "0":
                    return self.produtos

                produto = self.productObj.read(cod)
            
            print("Produto:")
            print(f"Codigo: {produto['codigo']} | Nome: {produto['nome']} | Tipo: {tipo} | Preço: R${produto['preco']} | Disponível: {produto['vendivel']}")
            

        #cadastra um produto novo
        elif opcao == 3:
            resposta = "Cadastro Produto..."
            while type(resposta) != dict:
                print(resposta)
                codigo = input("Digite um código para o produto: (0- voltar) ")
                if codigo == "0":
                    return self.produtos
                nome = input("Digite um nome para o produto: ")
                tipo = int(input("Digite o tipo do produto: (1- serie, 2- filme, 3- documentário) "))
                preco = float(input("Digite o preço do produto: "))
                disponivel = int(input("Está disponível para a venda? (1- sim, 2- não) "))
                while disponivel != 1 and disponivel != 2:
                    print("Digite um valor valido!")
                    disponivel = int(input("Está disponível para a venda? (1- sim, 2- não) "))

                resposta = self.productObj.create(codigo, nome, tipo, preco, disponivel)

            self.produtos = self.productObj.readAll()
            print(f"Produto novo:\n {resposta}")
        
        #Atualizar um produto existente
        elif opcao == 4:
            #codigo para alterar
            while True:
                cod = input("Digite o codigo do produto que deseja atualizar: (0- voltar) ")
                if cod not in self.produtos.keys():
                    print("Produto inexistente.")
                    continue
                if cod == "0":
                    return self.produtos

            opc = 0
            val = 0
            #opção para alterar 1 nome, 2 tipo, 3 preco, 4 vendivel
            while True:
                opc = int(input("O que você vai atualizar? (1- Nome, 2- Tipo, 3- Preço, 4- Disponibilidade)"))
                #alteração
                if opc == 1:
                    val = input("Digite um novo nome: ")
                    break
                elif opc == 2:
                    val = int(input("Digite um novo tipo: (1- serie, 2- filme, 3- documentario) "))
                    break
                elif opc == 3:
                    val = float(input("Digite um novo preço: "))
                    break
                elif opc == 4:
                    while True:
                        semival = int(input("Digite a disponibilidade (1- disponivel, 2- não disponivel) "))
                        if semival == 1:
                            val = True
                            break
                        elif semival == 2:
                            val = False
                            break
                        else:
                            print("Digite uma opção valida!")
                            continue 
                    break

                else:
                    print("Digite uma opção valida!")
                    continue

            produto = self.productObj.update(cod, opc, val)
            self.produtos = self.productObj.readAll()
            print(f"Produto atualizado!\n {produto}")

        else:
            while True:
                cod = input("Digite o codigo do produto a ser deletado: (0- voltar) ")
                if cod == "0":
                    return self.produtos
                
                if self.productObj.delete(cod) != str:
                    self.produtos = self.productObj.readALl()
                    print("Produto Deletado!")
                    break


        return self.produtos