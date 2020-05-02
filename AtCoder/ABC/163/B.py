# B - Homework

N, M = map(int, input().split())
A = [int(a) for a in input().split()]

for a in A: N -= a
print(N if N >= 0 else -1)