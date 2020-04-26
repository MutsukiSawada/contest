N = int(input())
A = [int(a) for a in input().split()]

snt = 10 ** 9 + 1

def merge(A, left, mid, right):
    cnt = 0
    L = A[left:mid] + [snt]
    R = A[mid:right] + [snt]
    i = j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            cnt += len(L) - 1 - i
    return cnt

def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        v1 = merge_sort(A, left, mid)
        v2 = merge_sort(A, mid, right)
        v3 = merge(A, left, mid, right)
        return v1 + v2 + v3
    else:
        return 0

ans = merge_sort(A, 0, N)
print(ans)