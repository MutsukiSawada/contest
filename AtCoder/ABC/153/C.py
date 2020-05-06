# C - Fennec vs Monster

N, K = map(int, input().split())
H = sorted([int(h) for h in input().split()])
H = H[:N - K]
print(sum(H) if K < N else 0)
