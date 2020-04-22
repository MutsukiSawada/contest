while True:
    X = [int(x) for x in input()]
    if sum(X) == 0:
        break
    else:
        print(sum(X))