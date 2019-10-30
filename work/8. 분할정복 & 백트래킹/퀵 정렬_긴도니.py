def partition(A,l,r):
    p = A[l]
    i = l
    j = r

    while i < j:
        while A[i] <= p:
            i+=1
            if i == r:
                break
        while A[j] >= p:
            j-=1
            if j == l:
                break

        if i<j:
            A[i],A[j]=A[j],A[i]

    A[l],A[j] = A[j], A[l]

    return j

def quickSort(A,l,r):
    if l<r:
        s = partition(A,l,r)
        quickSort(A,l,s-1)
        quickSort(A,s+1,r)

# A=[11,45,23,81,28,34]
# A=[11,45,22,81,23,34,99,22,17,8]
A=[1,1,1,1,1,0,0,0,0,0]
quickSort(A,0,len(A)-1)

print(A)