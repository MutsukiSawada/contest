# C - Next Prime

X = int(input())

def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    i = 3
    while i <= x ** (1 / 2):
        if x % i == 0:
            return False
        i = i + 2
    return True

while True:
    if is_prime(X):
        break
    X += 1

print(X)
