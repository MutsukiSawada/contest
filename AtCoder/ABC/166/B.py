# B - Trick or Treat

N, K = map(int, input().split())
ls = []
for _ in range(K):
    d = int(input())
    A = [int(a) for a in input().split()]
    ls += A

print(N - len(set(ls)))
