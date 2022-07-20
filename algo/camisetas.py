indexG = 0
while True:
    n = int(input())
    if n == 0:
        break

    vermelhas = [[], [], []]
    brancas = [[], [], []]

    if indexG != 0:
        print()
    for i in range(n):
        nome = input()
        cor, tamanho = map(str, input().split())

        if cor == 'vermelho':
            if tamanho == 'P':
                vermelhas[0].append(nome)
            elif tamanho == 'M':
                vermelhas[1].append(nome)
            else:
                vermelhas[2].append(nome)

        else:
            if tamanho == 'P':
                brancas[0].append(nome)
            elif tamanho == 'M':
                brancas[1].append(nome)
            else:
                brancas[2].append(nome)

    for index, i in enumerate(brancas):
        if index == 0:
            for val in sorted(i):
                print(f"branco P {val}")
        elif index == 1:
            for val in sorted(i):
                print(f"branco M {val}")
        else:
            for val in sorted(i):
                print(f"branco G {val}")
        

    for index, i in enumerate(vermelhas):
        if index == 0:
            for val in sorted(i):
                print(f"vermelho P {val}")
        elif index == 1:
            for val in sorted(i):
                print(f"vermelho M {val}")
        else:
            for val in sorted(i):
                print(f"vermelho G {val}")
    indexG += 1