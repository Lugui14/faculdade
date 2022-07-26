n = int(input())
total = 0

for i in range(1, n+1):
    total += i

#se nao for par da bigode
if total % 2 != 0:
    print("NO")
else:
    print("YES")
    total /= 2

    loop = 1
    firsts = 1
    sum1 = 0
    sum2 = 0
    fset = []
    sset = []

    #1º set
    while sum1 != total:
        if loop % 2 != 0:
            sum1 += n
            fset.append(n)
            n -= 1
            loop += 1
            continue
        sum1 += firsts
        fset.append(firsts)
        firsts += 1
        loop += 1
        continue
    #2º set
    for i in range(firsts, n+1):
        sset.append(i)

    print(len(fset))
    print(*fset)
    print(len(sset))
    print(*sset)

