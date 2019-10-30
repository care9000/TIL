import sys
sys.stdin = open('퀵_input.txt')

def quickSort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quickSort(arr, l, s-1)
        quickSort(arr, s+1, r)



def partition(arr, l, r):
    p = arr[l]
    i = l
    j = r

    while i < j:
        while arr[i] <= p:
            i += 1
            if i == r:
                break
        while arr[j] >= p:
            j -= 1
            if j == l:
                break

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]

    return j

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n = N//2
    A = list(map(int, input().split()))

    l = 0
    r = len(A) - 1

    quickSort(A, l, r)

    print('#{} {}'.format(tc, A[n]))
