# B - 81

N = int(input())
ans = 'No'
for i in range(10):
    for j in range(10):
        if i * j == N:
            ans = 'Yes'

print(ans)
