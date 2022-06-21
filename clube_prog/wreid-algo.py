i = int(input())

while True:
    if i == 1:
        print(i)
        break
    else: print(i, end=" ")

    if i % 2 == 0:
        i //= 2
    else:
        i = (i*3) + 1