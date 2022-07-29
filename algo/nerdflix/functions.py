import pandas as pd
from ClientsRepo import ClientsRepo

#tratamento string
def strinput(text: str) -> str or None:
  val = input(text)
  if val == '':
    return None
  return val
#tratamento inteiro
def intinput(text: str) -> int or None:
  val = input(text)
  if val == '':
    return None
  elif val.isnumeric() == False:
    print("\nERROR: Valor invalido. (igualado a None)")
    return None
  return int(val)
#tratamento float
def floatinput(text: str) -> float or None:
  val = input(text)
  if val == '':
    return None
  
  val = val.replace(',', '.')

  try:
    nval = float(val)
  except:
    print("\nERRO: Valor invalido. (retornado None)")
    nval = None

  return nval
#cria tabela com produtos
def tabelaprodutos(produtos: dict):
  colunas = "Nome Tipo Preço Disp".split(' ')
  linhas = []
  dados = []

  if produtos == {}:
    return

  for produto in produtos.values():
    #adiciona linha
    linhas.append(produto['codigo'])
    #formata o tipo
    if produto['tipo'] == 1:
      tipo = 'Série'
    elif produto['tipo'] == 2:
      tipo = 'Filme'
    else:
      tipo = 'Documentário'
    #adiciona dado
    dados.append([produto['nome'], tipo, produto['preco'], produto['disponibilidade']])
  #cria tabela
  tabela = pd.DataFrame(data=dados, index=linhas, columns=colunas)
  print(tabela)
  return
#cria tabela de compras
def tabelacompras(compras: dict):
  colunas = "Cliente Total Data".split(' ')
  linhas = []
  linha = 1
  dados = []

  if compras == {}:
    return

  for compra in compras.values():
    #adiciona linha
    linhas.append(linha)
    linha += 1
    #adiciona dados das compras
    dados.append([compra['cliente'], round(compra['total'], 2), compra['created_at']])
    
  #cria tabela
  tabela = pd.DataFrame(data=dados, index=linhas, columns=colunas)
  print(tabela)
  return
#cria tabela de clientes
def tabelaclientes():
  clientsRepo = ClientsRepo
  clientes = clientsRepo.getAll()

  colunas = "Cliente Compras".split(' ')
  linhas = []
  linha = 1
  dados = []

  for cliente in clientes.keys():
    #adiciona linha
    linhas.append(linha)
    linha += 1

    #adiciona dados das compras
    dados.append([cliente, clientes[cliente]])
    
  #cria tabela
  tabela = pd.DataFrame(data=dados, index=linhas, columns=colunas)
  print(tabela)
  return