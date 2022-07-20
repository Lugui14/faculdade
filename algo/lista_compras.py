def semRepetidos(lista):
    novaLista = []
    for k in lista:
        if k not in novaLista:
            novaLista.append(k)

    return sorted(novaLista)
    

n = int(input())
listas = []

for i in range(n):
    lista = input().split(' ')
    listas.append(semRepetidos(lista))

for i in listas:
    for j in i:
        if j != i[-1]:
            print(j, end=" ")
        else:
            print(j)