A =[3, 2, 4, 6, 9, 1, 8, 7, 5]

l = 0
r = len(A) - 1

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

quickSort(A, l, r)

print(A)
print(A)