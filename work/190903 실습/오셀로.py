import sys
sys.stdin = open('오셀로_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = []
    for _ in range(M):
        data.append(list(map(int, input().split())))
    table = [[0] * (N+1) for _ in range(N+1)]
    C = N // 2
    # 2 백돌 놓기
    table[C][C] = 2
    table[C+1][C+1] = 2
    # 1 흑돌 놓기
    table[C][C+1] = 1
    table[C+1][C] =1
    # print(table)
    # print(data)

    dx = [0, 0, -1, 1, -1, 1, 1, -1]
    dy = [-1, 1, 0, 0, -1, 1, -1, 1]

    for i in range(M):
        color = data[i][2]
        x = data[i][0]
        y = data[i][1]
        table[y][x] = color
        print(1)
        [print(table[z]) for z in range(len(table))]
        print()
        for z in range(8):
            testx = x + dx[z]
            testy = y + dy[z]

            if 0 < testx < N+1 and 0 < testy < N+1:
                if table[testy][testx] != color:
                    # 상
                    if testx == x and testy == (y-1):
                        for j1 in range(1, y-1):
                            if table[j1][x] == color:
                                for j11 in range(j1, y):
                                    table[j11][x] = color
                    # 하
                    if testx == x and testy == (y+1):
                        for j2 in range(y+1, N+1):
                            if table[j2][x] == color:
                                for j22 in range(y+1, j2+1):
                                    table[j22][x] = color

                    # 좌
                    if testx == (x-1) and testy == y:
                        for j3 in range(1, x-1):
                            if table[y][j3] == color:
                                for j33 in range(j3, x):
                                    table[y][j33] = color
                    # 우
                    if testx == (x+1) and testy == y:
                        for j4 in range(x+1, N+1):
                            if table[y][j4] == color:
                                for j44 in range(x+1, j4+1):
                                    table[y][j44] = color

                    # 좌상
                    if testx == (x-1) and testy == (y-1):
                        for j5 in range(x-1, 0, -1):
                            if table[j5][j5] == color:
                                for j55 in range(j5, x):
                                    table[j55][j55] = color
                    # 우상
                    if testx == (x+1) and testy == (y-1):
                        t1 = testx + testy
                        for j6 in range(x+1, N+1):
                            if table[j6][t1-j6] == color:
                                for j66 in range(x+1, j6+1):
                                    table[j66][t1-j66] = color
                    # 우하
                    if testx == (x+1) and testy == (y+1):
                        for j7 in range(x+1, N+1):
                            if table[j7][j7] == color:
                                for j77 in range(x+1, j7+1):
                                    table[j77][j77] = color
                    # 좌하
                    if testx == (x-1) and testy == (y+1):
                        t2 = testx + testy
                        for j8 in range(1, x+1):
                            if table[j8][t2-j8] == color:
                                for j88 in range(j8, x, -1):
                                    table[j88][t2-j88] = color

    cnt_w = 0
    cnt_b = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            if table[a][b] == 1:
                cnt_b += 1
            elif table[a][b] == 2:
                cnt_w += 1

    print('#{} {} {}'.format(tc, cnt_b, cnt_w))