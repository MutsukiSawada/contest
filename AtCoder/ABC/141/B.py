# B - Tap Dance

S = str(input())
ans = 'Yes'
for i in range(1, len(S) + 1):
    if i % 2 != 0 and S[i - 1] == 'L':
        ans = 'No'
    if i % 2 == 0 and S[i - 1] == 'R':
        ans = 'No'

print(ans)
