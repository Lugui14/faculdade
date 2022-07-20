hi, mi, hf, mf = map(int, input().split())

H = hf - hi
M = mf - mi

if H <= 0 and M <= 0:
    H += 24

if M < 0:
    M += 60
    H -= 1
    

print(f"O JOGO DUROU {H} HORA(S) E {M} MINUTO(S)")