# C - Lower

N = int(input())
H = [int(h) for h in input().split()]
cnt = []
tmp = 0
for i in range(N - 1):
    if H[i + 1] <= H[i]:
        tmp += 1
    else:
        cnt.append(tmp)
        tmp = 0
else:
    cnt.append(tmp)

print(max(cnt))
