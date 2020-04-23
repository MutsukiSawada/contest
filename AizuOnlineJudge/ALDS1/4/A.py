N = int(input())
S = [int(s) for s in input().split()]
Q = int(input())
T = [int(t) for t in input().split()]

cnt = 0
for t in T:
    if t in S:
        cnt += 1

print(cnt)