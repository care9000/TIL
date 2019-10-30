def printArr(n):
    for i in range(n):
        print(arr[i], end=' ')
    print()

def perm(n, k):
    if k == n:
        printArr(n)

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k] # 다시 제자리로 돌려놔야한다.

arr = [1, 2, 3]
perm(3, 0)