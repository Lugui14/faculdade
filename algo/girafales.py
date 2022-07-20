while True:
    turma = int(input())
    if turma == 0:
        break

    falsos = 0
    alunos = []
    assinaturasV = []

    for i in range(turma):
        aluno, assin = map(str, input().split())
        alunos.append(aluno)
        assinaturasV.append(assin)
    
    vieram = int(input())
    for i in range(vieram):
        aluno, assin = map(str, input().split())
        erros = 0

        for index, j in enumerate(assinaturasV[alunos.index(aluno)]):
            if j != assin[index]:
                erros += 1
        if erros > 1:
            falsos += 1
    print(falsos)
        