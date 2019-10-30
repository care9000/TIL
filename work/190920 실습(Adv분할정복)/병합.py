import sys
sys.stdin = open('병합_input.txt')
import time
st=time.time()

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    m = len(arr) // 2

    left = arr[0:m]
    right = arr[m:len(arr)]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(arr_l, arr_r):
    global cnt
    result = []
    i, j = 0, 0

    if arr_l[-1] > arr_r[-1]:
        cnt += 1

    while i < len(arr_l) or j < len(arr_r):
        if i < len(arr_l) and j < len(arr_r):
            if arr_l[i] <= arr_r[j]:
                result.append(arr_l[i])
                i += 1
            else:
                result.append(arr_r[j])
                j += 1

        elif i >= len(arr_l):
            result.append(arr_r[j])
            j += 1

        elif j >= len(arr_r):
            result.append(arr_l[i])
            i += 1

    return result

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))

    cnt = 0
    a = merge_sort(L)

    print('#{} {} {}'.format(tc, a[N//2], cnt))


print(time.time() - st)