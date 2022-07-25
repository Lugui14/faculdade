import ProductController
import SalesController

#logo
print("""\033[1;31m
        _   _ ______ _____  _____  ______ _      _______   __
        | \ | |  ____|  __ \|  __ \|  ____| |    |_   _\ \ / /
        |  \| | |__  | |__) | |  | | |__  | |      | |  \ V / 
        | . ` |  __| |  _  /| |  | |  __| | |      | |   > <  
        | |\  | |____| | \ \| |__| | |    | |____ _| |_ / . \ 
        |_| \_|______|_|  \_\_____/|_|    |______|_____/_/ \_\                                                     
    """)


#looping principal do programa
while True:
    #operação
    print("\033[1;31m--------------------------------------------------------------------------\n")
    operacao = input("\033[1;97mO que você quer fazer?\n0: Sair\n1: Gerenciar Compras,\n2: Gerenciar Produtos\n")
    print("\x1b[2J")
    print("\033[1;31m--------------------------------------------------------------------------\n")
    print("\033[1;97m")

    #validar digito
    if operacao.isnumeric():
        operacao = int(operacao)
    else:
        continue
    #validar operação
    if operacao < 0 or operacao > 2:
        print('Operação Invalida.')
        continue
    if operacao == 0:
        print("Saindo...")
        break
    
    #gerenciar compras
    if operacao == 1:
        while True:
            opcao = input("\033[1;97m\n\nO que você quer fazer?\n0: Voltar\n1: Cadastrar Compra,\n2: Gerar Relatório\n\n\n")
            print("\x1b[2J")

            #validar digito
            if opcao.isnumeric():
                opcao = int(opcao)
            else:
                continue

            #validar opcao
            if opcao < 0 or opcao > 2:
                print('Operação Invalida.')
                continue
            if opcao == 0:
                print("Voltando...")
                break

            #executar opcao
            SalesController.execute(opcao)
    #gerenciar produtos:
    elif operacao == 2:
        while True:
            opcao = input("\033[1;97m\n\nO que você quer fazer?\n0: Voltar\n1: Gerar Relatório,\n2: Mostrar um produto\n3: Cadastrar produto\n4: Atualizar produto\n5: Deletar Produto\n\n\n")
            print("\x1b[2J")

            #validar digito
            if opcao.isnumeric():
                opcao = int(opcao)
            else:
                continue

            #validar opcao
            if opcao < 0 or opcao > 5:
                print('Operação Invalida.')
                continue
            if opcao == 0:
                print("Voltando...")
                break
            #executar opcao
            ProductController.execute(opcao)