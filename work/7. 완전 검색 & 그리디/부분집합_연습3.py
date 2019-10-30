data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

N = 10
A = [0 for _ in range(N)]

def printSet(n):
    for i in range(n):
        if A[i] == 1:
            print('%d' % data[i], end=' ')
    print()

def powerset(n, k, cur_sum):
    if cur_sum > 10:
        return

    else:
        if n == k:
            if cur_sum == 10:
                printSet(n)

        else:
            A[k] = 1
            powerset(n, k+1, cur_sum + data[k])
            A[k] = 0
            powerset(n, k+1, cur_sum)

powerset(N, 0, 0)