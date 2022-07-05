def funcaoMuitoBraba(a, b):
        if b != 0:
            return (a / b)
        return -1

n = int(input())
sN = int(input())

response = funcaoMuitoBraba(n, sN)

print(response)