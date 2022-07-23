#lista de produtos
produtos = {}

#Repositorio de produtos
class ProductRepo:

  #lista todos os produtos
  def getAll():
    return produtos

  #busca um produto
  def getOne(codigo: str):
    return produtos[codigo]

  #cadastra um produto
  def add(produto: dict):
    produtos[produto['codigo']] = produto

  #atualiza um produto
  def update(codigo: str, nome: str, tipo: int, preco: float, disponibilidade: bool):
    if nome != None:
      produtos[codigo]['nome'] = nome
    if tipo != None:
      produtos[codigo]['tipo'] = tipo
    if preco != None:
      produtos[codigo]['preco'] = preco
    if disponibilidade != None:
      produtos[codigo]['vendivel'] = disponibilidade

    return produtos[codigo]

  #deleta um produto
  def delete(codigo: str):
    produtos.pop(codigo)