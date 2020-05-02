# B - 1%

X = int(input())
cur = 100

ans = 0
while cur < X:
    cur = int(cur * 1.01)
    ans += 1

print(ans)