# A - Poor

A, B, C = map(int, input().split())
ans = 'No'
if A == B and A != C:
    ans = 'Yes'
if A == C and A != B:
    ans = 'Yes'
if B == C and A != B:
    ans = 'Yes'
print(ans)