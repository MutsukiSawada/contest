# C - Build Stairs

N = int(input())
H = [int(h) for h in input().split()]
ans = 'Yes'
for i in range(1, N):
    if H[i - 1] <= H[i] - 1:
        H[i] -=1
    if H[i] < H[i - 1]:
        print('No')
        break
else:
    print('Yes')
