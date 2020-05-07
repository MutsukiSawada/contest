# B - TAKOYAKI FESTIVAL 2019

N = int(input())
D = [int(d) for d in input().split()]
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        ans += D[i] * D[j]

print(ans)
