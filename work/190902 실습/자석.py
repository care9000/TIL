import sys
sys.stdin = open('자석_input.txt')

T = 10

def move_N(i, j): # 아래로
    tx = i+1
    ty = j
    if -1 < tx < 100:
        # if tx == 99:
        #     table[tx][ty] = 0
        if table[tx][ty] == 2 or table[tx][ty] == 1:
            return
        elif table[tx][ty] == 0:
            table[i][j] = 0
            table[i+1][j] = 1
            move_N(tx, ty)


def move_S(i, j): # 위로
    tx = i-1
    ty = j
    if -1 < tx < 100:
        # if tx == 0:
        #     table[tx][ty] = 0
        if table[tx][ty] == 1 or table[tx][ty] == 2:
            return
        elif table[tx][ty] == 0:
            table[i][j] = 0
            table[tx][ty] = 2
            move_S(tx, ty)



for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if table[i][j] == 1: # 아래로
                move_N(i, j)

            elif table[i][j] == 2: # 위로
                move_S(i, j)


    cnt = 0
    for a in range(N):
        for b in range(N):
            if table[a][b] == 2:
                new_x = a - 1
                if -1 < new_x < 100:
                    if table[new_x][b] == 1:
                        cnt += 1

    print('#{} {}'.format(tc, cnt))
