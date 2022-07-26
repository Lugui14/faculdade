from datetime import datetime

#armazenamento de compras
compras = {
  "Pedro": {
    "cliente": "Pedro",
    "produtos": ["1", "5"],
    "total": 35.00,
    "created_at": datetime.today().strftime('%d/%m/%Y')
    },
    "Sergio": {
    "cliente": "Sergio",
    "produtos": ["3"],
    "total": 18.00,
    "created_at": datetime.today().strftime('%d/%m/%Y')
    },
}

class SalesRepo:

  #adicionar uma compra
  def add(cliente: str, codigosProdutos: list, precoTotal: float) -> dict:
    #cria dicionario de dados da compra
    compra = {"cliente": cliente, "produtos": codigosProdutos, "total": precoTotal, "created_at": datetime.today().strftime('%d/%m/%Y')}
    #adiciona a compra ao armazenamento
    compras['cliente'] = compra
    return compra

  #retorna o dicionario de compras
  def getAll() -> dict:
    return compras
