A = [0, 5, 89, 6, 46, 25, 96, 11, 37, 7, 6]

n = len(A)
#
# for i in range(n-1):
#     minI = i
#     for j in range(i+1, n):
#         if A[j] < A[minI]:
#             minI = j
#
#     A[minI], A[i] = A[i], A[minI]
#
# print(A)

def reselectionsort(ary, s, e):
    if s == e:
        return
    else:
        mini = s
        for i in range(s+1, e):
            if ary[i] < ary[mini]:
                mini = i
        ary[s], ary[mini] = ary[mini], ary[s]
        return reselectionsort(ary, s+1, e)

reselectionsort(A, 0, n)

print(A)
