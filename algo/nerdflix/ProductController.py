from ProductService import ProductService
import functions

def execute(opcao: int or None) -> None:
    #instancia objeto da classe de serviços
    productService = ProductService()

    #Mostrar Lista de produtos
    if opcao == 1:
        opcaoRelatorio = functions.intinput("\nEscolha uma opção:\n0- todos\n1- somente filmes\n2- somente séries\n3- somente documentários\n4- somente produtos a venda\n5- produtos indisponíveis.\n6- voltar\n")
        if opcaoRelatorio == None:
            print("\nErro... voltando")
            return
        #gerando tabela
        functions.tabelaprodutos(productService.getAll(opcaoRelatorio))
        return

    #Mostra um produto
    elif opcao == 2:
        codigo = input("Digite o codigo do produto que deseja pesquisar: (0- voltar)\n")
        #voltar
        if codigo == "0":
            return

        #pega produto
        produto = productService.getOne(codigo)
        if produto != None:
            if produto['tipo'] == 1:
                tipo = 'série'
            elif produto['tipo'] == 2:
                tipo = 'filme'
            else:
                tipo = 'documentário'

            #imprime produto
            print("Resultado: ")
            print(f"Nome: {produto['nome']}, Tipo: {tipo}, preço: R${produto['preco']}, Disponibilidade: {produto['disponibilidade']}")
        return

    #cadastra um produto novo
    elif opcao == 3:
        #coletando os dados e tratando-os
        cod = input("Digite o codigo do produto: (0- voltar)\n")
        if cod == "0":
            return
        nome = functions.strinput("Digite um nome para o produto: ")
        tipo = functions.intinput("Digite o tipo do produto: (1- série, 2-filme, 3-documentário) ")
        preco = functions.floatinput("Digite o preço do produto: ")
        disp = functions.intinput("O produto está disponível para venda? (1- disponível, 2- indisponível) ")

        #adicionando novo produto
        produto = productService.add(cod, nome, tipo, preco, disp)

        #mostrando novo produto
        if produto != None:
            print("\nProduto Cadastrado!")
            print(f"Nome: {produto['nome']}, Tipo: {produto['tipo']}, preço: R${produto['preco']}, Disponibilidade: {produto['disponibilidade']}")
        return
        
    #Atualizar um produto existente
    elif opcao == 4:
        #coletando os dados e tratamento de dados
        cod = input("Digite o codigo do produto que deseja atualizar: (0- voltar)\n")
        if cod == "0":
            return

        nome = functions.strinput("Digite um novo nome para o produto: (Clique enter caso não queira alterar nada) ")
        tipo = functions.intinput("Digite um novo tipo para o produto:\n(1-série, 2-filme, 3-documentário)\n(Clique enter caso não queira alterar nada) ")
        preco = functions.floatinput("Digite um novo preço para o produto: (Clique enter caso não queira alterar nada) ")
        disp = functions.intinput("Digite a nova disponibilidade do produto:\n(1- disponível, 2- indisponível)\n(Clique enter caso não queira alterar nada) ")

        #atualizando produto
        produto = productService.update(cod, nome, tipo, preco, disp)

        #mostrando produto atualizado
        if produto != None:
            print("\nProduto Atualizado!")
            print(f"Nome: {produto['nome']}, Tipo: {produto['tipo']}, preço: R${produto['preco']}, Disponibilidade: {produto['disponibilidade']}")
        return
    
    #Deletar produto
    else:
        #pegando codigo apra deletar
        cod = input("Digite o codigo do produto que deseja excluir: (0- voltar)\n")
        if cod == "0":
            return
        #deletando
        productService.delete(cod)
        return
    