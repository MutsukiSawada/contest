# C - Slimes

N = int(input())
S = str(input())

ans = ''
for i in range(N - 1):
    if S[i] != S[i + 1]:
        ans += S[i]
else:
    ans += S[N - 1]

print(len(ans))
