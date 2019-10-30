import sys
sys.stdin = open('암호코드스캔_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = [input() for _ in range(N)]

    s_i = 0
    s_j = 0
    l_j = 0
    flag = 0

    for i in range(N):
        for j in range(M):
            if info[i][j] != '0':
                s_i = i
                s_j = j
                code = ''
                for k in range(j, M):
                    if info[i][k] == '0' and info[i][k-1] != '0':
                        l_j = k

                for l in range(s_j, l_j):
                    code += info[s_i][l]

                if len(code) != 0:
                    break
    print(code)