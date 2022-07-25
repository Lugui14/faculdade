from ProductService import ProductService
from SalesService import SalesService
import functions

def execute(opcao: int):
  productService = ProductService()
  salesService = SalesService()

  #relatorio de compras
  if opcao == 0:
    salesService.getAll()
    return

  #adiciona nova compras
  if opcao == 1:
    #recupera o login do cliente
    cliente = functions.strinput("\nDigite o login do cliente: (0- voltar) ")
    #valida login
    if cliente == "0":
      print("Voltando...")
      return
    if cliente == None:
      print("Login invalido. Voltando...")
      return

    produtos = []
    #adiciona os produtos à compra
    while True:
      #recupera o codigo do produto
      codigo = functions.strinput("\nDigite o codigo do produto: (0- voltar) ")
      if codigo == "0":
        print("Voltando...")
        return

      #valida produto
      produto = productService.getOne(codigo)
      if produto == None or produto['disponibilidade'] == False:
        print("Codigo de produto não encontrado ou produto indisponível para venda.")
        continue
      #confirma produto
      print(f"\nNome: {produto['nome']}, Preço: {produto['preco']}")
      confirmacao = functions.intinput("Confirmar produto? (1- sim, 2- não) ")
      if confirmacao == None or confirmacao != 1 and confirmacao != 2:
        print("Operação invalida, voltando uma etapa...")
        continue
      elif confirmacao != 1:
        continue
      #adiciona produto à compra
      produtos.append(codigo)
      #continuação da compra
      continuarCompra = functions.intinput("\nDeseja continuar a compra ou finaliza-la? (1- finalizar, 2- continuar) ")
      if continuarCompra == None or continuarCompra != 1 and continuarCompra != 2:
        print("Operação invalida, finalizando compra.")
        break
      elif continuarCompra == 2:
        continue
      else:
        print("Finalizando compra.")
        break
    salesService.add(cliente, produtos)
    return


  