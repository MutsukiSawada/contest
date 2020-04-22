N = int(input())
pt_taro = 0
pt_hana = 0
for _ in range(N):
    taro, hanako = input().split()
    if taro < hanako:
        pt_hana += 3
    elif hanako < taro:
        pt_taro += 3
    elif taro == hanako:
         pt_taro += 1
         pt_hana += 1

print(pt_taro, pt_hana)