import ProductController

#looping principal do programa
while True:
    #operação
    print("--------------------------------------------------------------------------\n")
    opcao = input("O que você quer fazer?\n0: Sair\n1: Gerar Relatório,\n2: Mostrar um produto\n3: Cadastrar produto\n4: Atualizar produto\n5: Deletar Produto\n")
    print("--------------------------------------------------------------------------\n")
    
    #validar digito
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

    ProductController.execute(opcao)