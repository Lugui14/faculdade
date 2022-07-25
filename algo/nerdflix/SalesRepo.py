from datetime import datetime

#armazenamento de compras
compras = {}

class SalesRepo:

  #adicionar uma compra
  def add(cliente: str, codigosProdutos: list, precoTotal: float) -> dict:
    #cria dicionario de dados da compra
    compra = {"cliente": cliente, "produtos": codigoProduto, "total": precoTotal, "created_at": datetime.today().strftime('%d/%m/%Y')}
    #adiciona a compra ao armazenamento
    compras['cliente'] = compra
    return compra

  #retorna o dicionario de compras
  def getAll() -> dict:
    return compras
