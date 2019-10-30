import sys
sys.stdin = open('2D_array_input.txt')

T = 10
for tc in range(T):
    arr = [[0 for _ in range(100)] for _ in range(100)]
    N = int(input())
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    max_sum = 0

    for i in range(100):
        sum_1 = 0
        sum_2 = 0
        sum_3 = 0
        sum_4 = 0

        for j in range(100):
            sum_1 += arr[i][j]
            sum_2 += arr[j][i]
            sum_3 += arr[j][j]
            sum_4 += arr[j][99-j]


        if sum_1 > max_sum:
            max_sum = sum_1
        if sum_2 > max_sum:
            max_sum = sum_2
        if sum_3 > max_sum:
            max_sum = sum_3
        if sum_4 > max_sum:
            max_sum = sum_4
            # 인덴팅 유의, 굳이 j for문 안에 비교 조건문이 있을 필요가 없었음.

    print('#{} {}'.format(tc+1, max_sum))