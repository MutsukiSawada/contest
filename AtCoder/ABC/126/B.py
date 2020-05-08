# B - YYMM or MMYY

month = [str(i).zfill(2) for i in range(1, 13)]
year = [str(i).zfill(2) for i in range(0, 100)]

S = str(input())
left = S[0] + S[1]
right = S[2] + S[3]

if left not in month and right not in month:
    print('NA')
else:
    if (left in month and left in year) and (right in month and right in year):
        print('AMBIGUOUS')
    else:
        if left in year and right in month:
            print('YYMM')
        else:
            print('MMYY')
