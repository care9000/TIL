import sys
sys.stdin = open('이진수2_input.txt')

T = int(input())

for tc in range(1, T+1):
    nums = input()

    temp = nums
    temp_s = nums
    cnt = 0
    result = ''
    while temp_s[2] != 0:
        cnt += 1

        if cnt > 13:
            result = 'overflow'

        if temp_s[2] == '0' and temp_s[0] == '1':
            break

        else:
            temp = float(temp) * 2
            temp_s = str(temp)
            result += temp_s[0]
            if temp > 1:
                temp = temp - 1
                temp_s = str(temp)

    print('#{} {}'.format(tc, result))