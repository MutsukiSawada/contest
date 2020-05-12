# D - Preparing Boxes

N = int(input())
A = [int(a) for a in input().split()]

ans = [0] * N
for i in reversed(range(1, N + 1)):
    x = 0
    for j in range(i, N + 1, i):
        x += ans[j - 1]
    if x % 2 != A[i - 1]:
        ans[i - 1] = 1

print(ans.count(1))
print(*[i for i in range(1, N + 1) if ans[i - 1] == 1])
