# C - Guess The Number

N, M = map(int, input().split())
num = [-1] * N
ans = True

for _ in range(M):
    s, c = map(int, input().split())
    if num[s - 1] != -1 and num[s - 1] != c:
        ans = False
        break
    num[s - 1] = c

if 1 < N and num[0] == 0:
    ans = False

if 1 < N and num[0] == -1:
    num[0] = 1

if N == 1 and num[0] == -1:
    num[0] = 0

for i in range(N):
    if num[i] == -1:
        num[i] = 0

print(''.join([str(n) for n in num]) if ans else -1)
