n = int(input())

todas = []
for i in range(n):
    stri = input().split(" ")
    stri.sort(key=len, reverse=True)
    todas.append(stri)
    
for i in todas:
    print(' '.join(i))