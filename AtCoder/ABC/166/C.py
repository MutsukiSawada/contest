# C - Peaks

N, M = map(int, input().split())
H = [int(h) for h in input().split()]

mapping = [[] for _ in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    mapping[i - 1].append(j - 1)
    mapping[j - 1].append(i - 1)

cnt = 0
for i in range(N):
    ls = mapping[i]
    for j in ls:
        if H[i] <= H[j]:
            break
    else:
        cnt += 1

print(cnt)
