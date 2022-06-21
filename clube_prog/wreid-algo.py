i = int(input())
print(i, end=" ")
while True:
    if i == 1:
        print(i)
        break

    if i % 2 == 0:
        i //= 2
    else:
        i = (i*3) + 1

    print(i, end=" ")