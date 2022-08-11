import functions
import ProductController
import SalesController

#função para gerenciar compras
def compras():
    opcao = functions.intinput("""
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

    #validar opcao
    if opcao == None or opcao < 0 or opcao > 3:
        print('Operação Invalida.')
        compras()
    if opcao == 0:
        print("Voltando...")
        return

    #executar opcao
    SalesController.execute(opcao)

#função para gerenciar produtos
def produtos():
    opcao = functions.intinput("""
\033[1;31m--------------------------------------------------------------------------
\033[1;97mO que você quer fazer?
0: Voltar
1: Gerar Relatório
2: Mostrar um produto
3: Cadastrar produto
4: Atualizar produto
5: Deletar Produto
\033[1;31m--------------------------------------------------------------------------
""")
    print("\033[1;97m")
    print("\n" * 50)

    #validar opcao
    if opcao == None or opcao < 0 or opcao > 5:
        print('Operação Invalida.')
        produtos()
    if opcao == 0:
        print("Voltando...")
        return
    #executar opcao
    ProductController.execute(opcao)

#array literal, usado para chamda de funções de forma dinâmica sem um monte de if
funcs = [None, compras, produtos]

#logo
print("""\033[1;31m
_   _ ______ _____  _____  ______ _      _______   __
| \ | |  ____|  __ \|  __ \|  ____| |    |_   _\ \ / /
|  \| | |__  | |__) | |  | | |__  | |      | |  \ V / 
| . ` |  __| |  _  /| |  | |  __| | |      | |   > <  
| |\  | |____| | \ \| |__| | |    | |____ _| |_ / . \ 
|_| \_|______|_|  \_\_____/|_|    |______|_____/_/ \_\                                                     
""")

#loop principal do programa
while True:
    #operação
    operacao = functions.intinput("""
\033[1;31m--------------------------------------------------------------------------
\033[1;97mO que você quer fazer?
0: Sair
1: Gerenciar Compras
2: Gerenciar Produtos
\033[1;31m--------------------------------------------------------------------------
""")
    print("\n" * 50)
    print("\033[1;97m")

    #validar operacao
    if operacao == None or operacao < 0 or operacao > 2:
        print("Operação Invalida.")
        continue

    if operacao == 0:
        print("Saindo...")
        break
    
    #chamada da função requerida de forma dinâmica
    funcs[operacao]()