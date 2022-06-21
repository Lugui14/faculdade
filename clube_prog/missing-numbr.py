i = int(input())
list = list(map(int, input().split(" ")))
list.sort()

for x in range(1, i):
    if x != list[x-1]:
        print(x)
        break