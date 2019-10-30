import sys
sys.stdin = open('2자리 소수_input.txt')

def calc(t):
    if t in real:
        real_check[real.index(t)] = 1

def comb(n, r, q):

    test = 0

    if r == 0:
        test += int(T[0]) * 10
        test += int(T[1])
        calc(test)

    elif n < r:
        return

    else:
        T[r-1] = c[n-1]
        comb(n-1, r-1, q)
        comb(n-1, r, q)

T = int(input())

real = [11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]


for tc in range(1, T+1):
    a, b = input().split()
    arr = [i for i in range(int(a), int(b) + 1)]
    # print(arr)
    t_cnt = 0

    for i in range(len(arr)):
        c = list(str(arr[i]))
        n = len(c)
        T = [0] * 2
        real_check = [0] * 21
        comb(n, 2, 2)
        t_cnt += sum(real_check)

    print('#{} {}'.format(tc, t_cnt))


