n = input()
i = 0
v = 1
f = 0

for x in n:
    if i != 0 and x == n[i-1]:
        v += 1
    else:
        v = 1

    if f < v:
        f = v

    i += 1

print(f)