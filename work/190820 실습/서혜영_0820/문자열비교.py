import sys
sys.stdin = open('문자열_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    n1 = len(str1)
    n2 = len(str2)

    cnt = 0

    for i in range(n2-n1+1):
        str_cnt = 0

        if str1[0] == str2[i]:
            for j in range(n1):
                if str1[j] == str2[i+j]:
                    str_cnt += 1
            if str_cnt == n1:
                cnt += 1
                break

    print('#{} {}'.format(tc, cnt))
