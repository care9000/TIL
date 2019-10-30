import sys
sys.stdin = open('글자수_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    result = {}

    for i in str1:
        cnt1 = 0
        for j in str2:
            if i == j:
                cnt1 += 1
            result[i] = cnt1
        max_value = 0
        for value in result.values():
            if value > max_value:
                max_value = value

    print('#{} {}'.format(tc, max_value))