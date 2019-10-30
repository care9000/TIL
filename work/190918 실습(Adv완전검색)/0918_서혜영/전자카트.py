import sys
sys.stdin = open('카트_input.txt')

def perm(n, k, cur_sum):
    global min_battery

    if cur_sum > min_battery: # 가지치기
        return

    if n == k: # 탈출하기
        cur_sum += data[A[-1]][0]
        if cur_sum < min_battery :
            min_battery = cur_sum

    else:
        for i in range(k, n):
            A[k], A[i] = A[i], A[k]
            perm(n, k+1, cur_sum + data[A[k-1]][A[k]])
            A[k], A[i] = A[i], A[k]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    A = [i for i in range(N)] # 순열만들기
    min_battery = 987654


    print(data)
    print(A)

    perm(N, 1, 0)

    print('#{} {}'.format(tc, min_battery))
