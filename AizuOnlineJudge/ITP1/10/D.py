N = int(input())
X = [float(x) for x in input().split()]
Y = [float(y) for y in input().split()]

for p in range(1, 4):
    print(sum(map(lambda x, y: abs(x - y) ** p, X, Y)) ** (1 / p))
print(max(map(lambda x, y: abs(x - y), X, Y)))