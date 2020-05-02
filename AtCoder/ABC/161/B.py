# B - Popular Vote

N, M = map(int, input().split())
A = [int(a) for a in input().split()]
P = [1 for a in A if a >= sum(A) * 1 / (4 * M)]

print('Yes' if len(P) >= M else 'No')