import sys
sys.stdin = open('2D_array_input.txt')

T = 10
for tc in range(T):
    arr = [[0 for _ in range(100)] for _ in range(100)]
    N = int(input())
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    # print(arr)
    sum = 0
    max_sum = 0

    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        if sum > max_sum:
            max_sum = sum

    for j in range(100):
        sum = 0
        for i in range(100):
            sum += arr[i][j]
        if sum > max_sum:
            max_sum = sum

    for k in range(100):
        sum = 0
        sum += arr[k][k]
    if sum > max_sum:
        max_sum = sum


    print('#{} {}'.format(tc+1, max_sum))