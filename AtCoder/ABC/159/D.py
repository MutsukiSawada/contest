N = int(input())
A = [int(a) for a in input().split()]
cnt = {}
total = 0

for a in A:
    if a not in cnt:
        cnt[a] = 0
    cnt[a] += 1

for i in cnt.values():
    total += i * (i - 1) // 2

for a in A:
    print(total - (cnt[a] - 1))
