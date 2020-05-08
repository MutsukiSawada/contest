# D - Gathering Children

S = [s for s in str(input())]

N = len(S)
cnt = 0
ans = [0] * N

for i in range(N - 1):
    if S[i] == 'R':
        cnt += 1
    if S[i] == 'R' and S[i + 1] == 'L':
        ans[i] += cnt // 2
        ans[i + 1] += cnt // 2
        if cnt % 2 != 0:
            ans[i] += 1
        cnt = 0

for i in reversed(range(1, N)):
    if S[i] == 'L':
        cnt += 1
    if S[i] == 'L' and S[i - 1] == 'R':
        ans[i] += cnt // 2
        ans[i - 1] += cnt // 2
        if cnt % 2 != 0:
            ans[i] += 1
        cnt = 0

print(*ans)
