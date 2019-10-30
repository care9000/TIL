import sys
sys.stdin = open("단순2진암호_input.txt")

T = int(input())

number = [
       '0001101', '0011001', '0010011', '0111101', '0100011', '0110001',
       '0101111', '0111011', '0110111', '0001011'
        ]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = [input() for _ in range(N)]
    # print(N, M)
    # print(info)

    s_i = 0
    s_j = 0
    l_j = 0
    flag = 0
    code = ''

    for i in range(N): # 세로길이
        cnt = 0
        for j in range(M): # 가로길이
            if info[i][j] == '1':
                s_i = i
                s_j = j
                flag = 1
                for k in range(j, M):
                    if info[i][k] == '1':
                        l_j = k
                break

        if flag == 1:
            break

    for l in range(s_j, l_j+1):
        code += info[s_i][l]

    while len(code) != 56:
        code = '0' + code

    result = ''
    for i in range(len(code)//7):
        temp = ''
        for j in range(i*7, (i*7)+7):
            temp += code[j]
        if temp in number:
            idx = number.index(temp)
            result += str(idx)
    plus = 0
    total = 0
    # print(result)
    for i in range(0, len(result), 2):
        plus += int(result[i])
    a = plus * 3
    for i in range(1, len(result ), 2):
        a += int(result[i])
    # a += int(result[-1])
    if a % 10 == 0:
        for j in range(len(result)):
            total += int(result[j])

    print('#{} {}'.format(tc, total))