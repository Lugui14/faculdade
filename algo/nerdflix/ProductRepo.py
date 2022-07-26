#lista de produtos
produtos = {
    "1": {
      "codigo": "1",
      "nome": "Ilha do Medo",
      "tipo": 2,
      "preco": 15.00,
      "disponibilidade": True
    },
    "2": {
      "codigo": "2",
      "nome": "Ted 2",
      "tipo": 2,
      "preco": 10.00,
      "disponibilidade": False
    },
    "3": {
      "codigo": "3",
      "nome": "Stranger Things",
      "tipo": 1,
      "preco": 18.00,
      "disponibilidade": True
    },
    "4": {
      "codigo": "4",
      "nome": "Suits",
      "tipo": 1,
      "preco": 10.00,
      "disponibilidade": False
    },
    "5": {
      "codigo": "5",
      "nome": "As Fitas de Poughkeepsie",
      "tipo": 3,
      "preco": 20.00,
      "disponibilidade": True
    },
    "6": {
      "codigo": "6",
      "nome": "Take Your Pills",
      "tipo": 3,
      "preco": 12.00,
      "disponibilidade": False
    }
  }

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
      produtos[codigo]['disponibilidade'] = disponibilidade

    return produtos[codigo]

  #deleta um produto
  def delete(codigo: str):
    produtos.pop(codigo)