# C - Alchemist

N = int(input())
V = sorted([int(v) for v in input().split()])
while len(V) != 1:
    v1 = V.pop(0)
    v2 = V.pop(0)
    V = [(v1 + v2) / 2] + V

print(V[0])
