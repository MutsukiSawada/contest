# C - Rally

N = int(input())
X = [int(x) for x in input().split()]
total = float('inf')
for p in range(101):
    tmp = 0
    for x in X:
        tmp += (x - p) ** 2
    total = min(total, tmp)
print(total)