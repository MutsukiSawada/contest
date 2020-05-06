# A - Remaining Balls

S, T = map(str, input().split())
A, B = map(int, input().split())
U = str(input())
print(*((A - 1, B) if S == U else (A, B - 1)))
