x, y = map(int, input().split())
while x != 0 or y != 0:
    print(x, y) if x < y else print(y, x)
    x, y = map(int, input().split())