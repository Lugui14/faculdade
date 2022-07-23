import ProductController

#looping principal do programa
while True:
    #operação

    print("""\033[1;31m
        _   _ ______ _____  _____  ______ _      _______   __
        | \ | |  ____|  __ \|  __ \|  ____| |    |_   _\ \ / /
        |  \| | |__  | |__) | |  | | |__  | |      | |  \ V / 
        | . ` |  __| |  _  /| |  | |  __| | |      | |   > <  
        | |\  | |____| | \ \| |__| | |    | |____ _| |_ / . \ 
        |_| \_|______|_|  \_\_____/|_|    |______|_____/_/ \_\                                                     
    """)

    print("\033[1;31m--------------------------------------------------------------------------\n")
    opcao = input("\033[1;97mO que você quer fazer?\n0: Sair\n1: Gerar Relatório,\n2: Mostrar um produto\n3: Cadastrar produto\n4: Atualizar produto\n5: Deletar Produto\n")
    print("\x1b[2J")
    print("\033[1;31m--------------------------------------------------------------------------\n")
    print("\033[1;97m")
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