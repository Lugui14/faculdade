from ProductService import ProductService
from SalesRepo import SalesRepo
import functions

class SalesService:

  def __init__(self):
    self.productService = ProductService()
    self.salesRepo = SalesRepo()

  #adiciona nova compra
  def add(self, cliente: str, codigosProdutos: list):
    #validando dados
    if cliente == None or codigoProduto == None:
      print("\nVocê precisa digitar o login do cliente e os codigos dos produtos.")
      return

    #registrando total da compra
    total = 0
    produtos = {}
    for produto in codigosProdutos:
      produto = self.productService.getOne(produto)
      produtos[produto['codigo']] = produto
      total += produto['preco']
    
    #adiciona compra ao repositorio
    compra = self.salesRepo.add(cliente, codigosProdutos, total)

    #relatorio da compra
    functions.tabelaprodutos(produtos)
    print(f"TOTAL DA COMPRA: R${total:.2f}")
    return
    
  #relatório de compras
  def getAll():
    #gera tabela com relatório das compras
    functions.tabelacompras(self.productService.getAll())
    return