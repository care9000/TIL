import sys
sys.stdin = open("sum_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    min_sum = 98498798798987989
    max_sum = 0


    for i in range(N-M+1):
        result_nums = []
        for pre in range(i, i+M):
            result_nums.append(nums[pre])
        result = sum(result_nums)

        if result < min_sum:
            min_sum = result
        if result > max_sum:
            max_sum = result
        prefix_result = max_sum - min_sum

    print('#{} {}'.format(tc, prefix_result))