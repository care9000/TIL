import sys
sys.stdin = open('색칠_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # N 행, M 열
    data = []
    paint = [[0] * M for _ in range(N)]
    for _ in range(K):
        data.append(list(map(int, input().split())))

    for i in range(K):
        info = data[i]
        color = info[-1]
        test = []
        for j in range(info[0], info[2]+1):
            for k in range(info[1], info[3]+1):
                test.append(paint[j][k])
        v = 0
        for t in test:
            v += 1
            if t > color:
                break
            elif v == len(test):
                for j in range(info[0], info[2] + 1):
                    for k in range(info[1], info[3] + 1):
                        paint[j][k] = color

    color_board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    color_cnt = [0] * 11

    for c in color_board:
        cnt = 0
        for x in range(N):
            for y in range(M):
                if paint[x][y] == c:
                    cnt += 1
        color_cnt[c] = cnt

    max_cnt = 0
    for w in color_cnt:
        if w > max_cnt:
            max_cnt = w

    print('#{} {}'.format(tc, max_cnt))


