n = int(input())

if n < 4 and n != 1:
    print("NO SOLUTION")
else:
    for x in range(1, n+1):
        if x % 2 == 0:
            print(x, end=" ")

    for x in range(1, n+1):
        if x % 2 != 0:
            print(x, end=" ")


