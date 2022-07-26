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
    operacao = input("""
\033[1;31m--------------------------------------------------------------------------
\033[1;97mO que você quer fazer?
0: Sair
1: Gerenciar Compras
2: Gerenciar Produtos
\033[1;31m--------------------------------------------------------------------------
""")
    print("\n" * 50)
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
            opcao = input("""
\033[1;31m--------------------------------------------------------------------------
\033[1;97mO que você quer fazer?
0: Voltar
1: Cadastrar Compra
2: Gerar Relatório de Compras
3: Gerar Relatório de Clientes
\033[1;31m--------------------------------------------------------------------------
""")
            print("\033[1;97m")
            print("\n" * 50)

            #validar digito
            if opcao.isnumeric():
                opcao = int(opcao)
            else:
                continue

            #validar opcao
            if opcao < 0 or opcao > 3:
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
            opcao = input("""
\033[1;31m--------------------------------------------------------------------------
\033[1;97mO que você quer fazer?
0: Voltar
1: Gerar Relatório,
2: Mostrar um produto
3: Cadastrar produto
4: Atualizar produto
5: Deletar Produto
\033[1;31m--------------------------------------------------------------------------
""")
            print("\033[1;97m")
            print("\n" * 50)

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