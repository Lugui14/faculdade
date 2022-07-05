n = int(input())
list = list(map(int, input().split(" ")))
moves = 0

for index, value in enumerate(list):
    if index == 0:
        continue

    if value < list[index-1]:
        moves += list[index-1] - value
        list[index] = value + (list[index-1] - value)

print(moves)