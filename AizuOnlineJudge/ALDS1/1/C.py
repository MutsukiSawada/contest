def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    i = 3
    while i <= x ** (1 / 2):
        if x % i == 0:
            return False
        i += 2
    return True

N = int(input())
cnt = 0
for _ in range(N):
    x = int(input())
    if is_prime(x):
        cnt += 1

print(cnt)
