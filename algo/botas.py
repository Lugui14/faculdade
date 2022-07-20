while True:
  try:
    n = int(input())

    numeros = []
    pares = []
    total = 0
    for i in range(n):
      numero, par = map(str, input().split(' '))

      if numero in numeros:
        if pares[numeros.index(numero)] != par:
          total += 1
          pares.pop(numeros.index(numero))
          numeros.remove(numero)
          continue
        else:
          numeros.append(numero)
          pares.append(par)
      else: 
        numeros.append(numero)
        pares.append(par)
    print(total)
  except EOFError:
    break
