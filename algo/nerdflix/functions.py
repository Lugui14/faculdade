import pandas as pd

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
  elif val.isnumeric() == False:
    print("\nERROR: Valor invalido. (igualado a None)")
    return None
  return float(val)
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
    
  