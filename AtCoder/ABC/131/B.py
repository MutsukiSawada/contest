# B - Bite Eating

N, L = map(int, input().split())
ans = 0
mn = float('inf')
for i in range(1, N + 1):
    ans += L + i - 1
    if abs(L + i - 1) < abs(mn):
        mn = L + i - 1

print(ans - mn)
