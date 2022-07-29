from ProductService import ProductService
from SalesRepo import SalesRepo
from ClientsRepo import ClientsRepo
import functions

class SalesService:

  def __init__(self):
    self.productService = ProductService()
    self.salesRepo = SalesRepo
    self.clientsRepo = ClientsRepo

  #adiciona nova compra
  def add(self, cliente: str, codigosProdutos: list):
    #validando dados
    if cliente == None or codigosProdutos == None:
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
    self.clientsRepo.addCompra(cliente)

    #relatorio da compra
    functions.tabelaprodutos(produtos)
    print(f"#\t\tTOTAL DA COMPRA: R${total:.2f}")
    return
    
  #relatório de compras
  def getAll(self):
    #gera tabela com relatório das compras
    functions.tabelacompras(self.salesRepo.getAll())
    return