import sys
sys.stdin = open('dump_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    min_num = 101
    max_num = 0

    for i in range(N):
        for idx, num in enumerate(data):
            if num > max_num:
                max_num = num
                max_num_idx = idx
            if num < min_num:
                min_num = num
                min_num_idx = idx

        max_num -= 1
        data[max_num_idx] = max_num
        min_num += 1
        data[min_num_idx] = min_num

    for num in data:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num


    result = max_num - min_num
    print('#{} {}'.format(tc, result))