# C - management

N = int(input())
A = [0] * N
for a in [*map(int, input().split())]: A[a - 1] += 1
print(*A, sep='\n')