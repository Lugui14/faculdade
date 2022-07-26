#dicionario de clientes
clientes = {
 "Sergio": 1,
 "Pedro": 1
}

class ClientsRepo:

  def getAll():
    return clientes

  def addCompra(nomeCliente: str):
    if nomeCliente in clientes.keys():
      clientes[nomeCliente] += 1
      return
    cliente[nomeCliente] = 0
    clientes[nomeCliente] += 1
    return
    