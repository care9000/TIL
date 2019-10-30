import sys
sys.stdin = open('p_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    datas = []
    cnt = 0

    for i in range(8):
        data = list(input())
        datas.append(data)
    # print(datas)

    for i in range(8):
        for j in range(8-N+1):
            result = []
            for k in range(j, j+N):
                result.append(datas[i][k])
            if result == result[::-1]:
                cnt += 1
            else:
                continue

    for i in range(8):
        for j in range(8-N+1):
            result = []
            for k in range(j, j+N):
                result.append(datas[k][i])
            if result == result[::-1]:
                cnt += 1
            else:
                continue

    print('#{} {}'.format(tc, cnt))


