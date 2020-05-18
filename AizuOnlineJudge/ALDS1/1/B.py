def gcd(x, y):
    if x < y:
        x, y = y, x
    
    while 0 < y:
        x, y = y, x % y

    return x

X, Y = map(int, input().split())
print(gcd(X, Y))
