from ProductController import ProductController

#lista de produtos
produtos = {}

#looping principal do programa
while True:
    #operação
    print("--------------------------------------------------------------------------\n")
    opcao = input("O que você quer fazer?\n 0: Sair\n1: Mostrar lista de produtos,\n2: Mostrar um produto\n3: Cadastrar produto\n4: Atualizar produto\n5: Deletar Produto\n")
    print("--------------------------------------------------------------------------\n")
    
    if opcao.isnumeric():
        opcao = int(opcao)
    else:
        continue

    #validar operação
    if opcao < 0 or opcao > 5:
        print('Operação Invalida.')
        continue
    if opcao == 0:
        print("Saindo...")
        break
    
    #definir objeto para a classe controladora dos produtos
    productController = ProductController(produtos)
    produtos = productController.execute(opcao) 