n = int(input())

for i in range(1, n+1):
    j = ((i*i) * ((i*i) -1))/2
    k = 4 * ((i-1) * (i-2))
    print(round(j-k))
