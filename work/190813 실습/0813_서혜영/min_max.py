import sys
sys.stdin = open("minmax_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_num = 98543218795646
    max_num = 0


    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    result = max_num - min_num


    print('#{} {}'.format(tc, result))
