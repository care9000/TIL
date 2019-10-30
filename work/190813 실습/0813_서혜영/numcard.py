import sys
sys.stdin = open("numcard_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = input()
    result_list = [0] * 10
    max_index = 0

    for i in nums:
        result_list[int(i)] += 1

    for i in range(10):
        if result_list[i] >= result_list[max_index]:
            max_value = result_list[i]
            max_index = i

    print('#{} {} {}'.format(tc, max_index, max_value))


