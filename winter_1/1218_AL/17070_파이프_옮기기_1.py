import sys
sys.stdin = open('17070_파이프_옮기기_1.txt')

from collections import deque

def Moving_pipe(x, y, pipe_type):
    global cnt
    if pipe_type == 1:
        for move in range(2):
            x_tem = x + pipe_1_x[move]
            y_tem = y + pipe_1_y[move]
            if -1 < x_tem < N and -1 < y_tem < N and house_map[x_tem][y_tem] == 0:
                if move == 1:
                    if house_map[x_tem - 1][y_tem] == 0 and house_map[x_tem][y_tem - 1] == 0:
                        if x_tem == N - 1 and y_tem == N - 1:
                            cnt += 1
                        else:
                            Moving_pipe(x_tem, y_tem, move + 1)

                else:
                    if x_tem == N - 1 and y_tem == N - 1:
                        cnt += 1
                    else:
                        Moving_pipe(x_tem, y_tem, move + 1)
    elif pipe_type == 2:
        for move in range(3):
            x_tem = x + pipe_2_x[move]
            y_tem = y + pipe_2_y[move]
            if -1 < x_tem < N and -1 < y_tem < N and house_map[x_tem][y_tem] == 0:
                if move == 1:
                    if house_map[x_tem - 1][y_tem] == 0 and house_map[x_tem][y_tem - 1] == 0:
                        if x_tem == N - 1 and y_tem == N - 1:
                            cnt += 1
                        else:
                            Moving_pipe(x_tem, y_tem, move + 1)
                else:
                    if x_tem == N - 1 and y_tem == N - 1:
                        cnt += 1
                    else:
                        Moving_pipe(x_tem, y_tem, move + 1)

    else:
        for move in range(2):
            x_tem = x + pipe_3_x[move]
            y_tem = y + pipe_3_y[move]
            if -1 < x_tem < N and -1 < y_tem < N and house_map[x_tem][y_tem] == 0:
                if move == 0:
                    if house_map[x_tem - 1][y_tem] == 0 and house_map[x_tem][y_tem - 1] == 0:
                        if x_tem == N - 1 and y_tem == N - 1:
                            cnt += 1
                        else:
                            Moving_pipe(x_tem, y_tem, move + 2)
                else:
                    if x_tem == N - 1 and y_tem == N - 1:
                        cnt += 1
                    else:
                        Moving_pipe(x_tem, y_tem, move + 2)


def ispass(x, y):
    if -1 < x < N and -1 < y < N and house_map[x][y] == 0:
        return True
    return False




# 가로 파이프 다음거
pipe_1_x = [0, 1]
pipe_1_y = [1, 1]

# 세로 파이프 다음거
pipe_3_x = [1, 1]
pipe_3_y = [1, 0]

# 대각선 파이프 다음거
pipe_2_x = [0, 1, 1]
pipe_2_y = [1, 1, 0]


N = int(input())
house_map = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
if house_map[-1][-1] == 0:
    print(0)
else:
    Moving_pipe(0, 1, 1)
    print(cnt)




