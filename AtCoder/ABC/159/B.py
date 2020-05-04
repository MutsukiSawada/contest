# B - String Palindrome

S = input()

ans = 'No'
N = len(S)
left = S[:(N - 1) // 2]
right = S[((N + 3) // 2) - 1:]
if left == right:
    if left == left[::-1] and right == right[::-1]:
        ans = 'Yes'

print(ans)