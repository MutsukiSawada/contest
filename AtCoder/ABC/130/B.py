# B - Bounding

N, X = map(int, input().split())
L = [int(l) for l in input().split()]
D = 0
cnt = 1
for i in range(N):
    D = D + L[i]
    if D <= X:
        cnt += 1

print(cnt)
