while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for h in range(H):
        if h == 0:
            print('#' * W)
        elif h != 0 and h != H - 1:
            print('#', '.' * (W - 2), '#', sep='')
        elif h == H - 1:
            print('#' * W)
    print()