import sys
sys.stdin = open('최소_input.txt')

def perm(n, k, cur_sum):
    global min

    if cur_sum >= min:
        return

    if n == k:
        min = cur_sum
        return

    else:
        for i in range(k, n):
            A[k], A[i] = A[i], A[k]
            perm(n, k+1, cur_sum + data[k][A[k]])
            A[k], A[i] = A[i], A[k]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    A = [i for i in range(N)]
    min = 9999999

    perm(N, 0, 0)

    print('#{} {}'.format(tc, min))