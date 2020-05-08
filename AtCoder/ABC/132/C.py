# C - Divide the Problems

N = int(input())
D = sorted([int(d) for d in input().split()])

print(D[N // 2] - D[N // 2 - 1])
