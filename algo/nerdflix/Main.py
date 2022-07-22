from ProductService import ProductService

#lista de produtos
produtos = {}

#looping principal do programa
while True:
    #operação
    print("--------------------------------------------------------------------------\n")
    opcao = int(input("O que você quer fazer?\n 0: Sair\n1: Mostrar lista de produtos,\n2: Mostrar um produto\n3: Cadastrar produto\n4: Atualizar produto\n5: Deletar Produto\n"))
    print("--------------------------------------------------------------------------\n")

    #validar operação
    if opcao < 0 or opcao > 5:
        print('Operação Invalida.')
        continue
    if opcao == 0:
        print("Saindo...")
        break
    
    #definir objeto para a classe de produtos
    productObj = ProductService(produtos)
    #executar operação

    #lista os produtos
    if opcao == 1:
        for produto in produtos.values():
            if produto['tipo'] == 1: 
                tipo = "série"
            elif produto['tipo'] == 2:
                tipo = "filme"
            else:
                tipo = "documentário"

            print("-------------------------------------------------------------------------------------------------------------------------------------")
            print(f"Codigo: {produto['codigo']} | Nome: {produto['nome']} | Tipo: {tipo} | Preço: R${produto['preco']} | Disponível: {produto['vendivel']}")
            print("-------------------------------------------------------------------------------------------------------------------------------------")

    #cadastra um produto novo
    elif opcao == 3:
        resposta = "Cadastro Produto..."
        while type(resposta) != dict:
            print(resposta)
            codigo = input("Digite um código para o produto: ")
            nome = input("Digite um nome para o produto: ")
            tipo = int(input("Digite o tipo do produto: (1- serie, 2- filme, 3- documentário) "))
            preco = float(input("Digite o preço do produto: "))
            disponivel = int(input("Está disponível para a venda? (1- sim, 2- não) "))
            while disponivel != 1 and disponivel != 2:
                print("Digite um valor valido!")
                disponivel = int(input("Está disponível para a venda? (1- sim, 2- não) "))

            resposta = productObj.create(codigo, nome, tipo, preco, disponivel)

        produtos = productObj.readAll()
        print(f"Produto novo:\n {resposta}")