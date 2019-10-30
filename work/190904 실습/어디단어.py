import sys
sys.stdin = open('단어_input.txt')


def start1(x, y): #가로용
    flag = 0
    if y == 0:
        flag = 1
        return flag
    elif puzzle[x][y-1] == 0:
        flag = 1
        return flag
    return flag


def start2(x, y): # 세로용
    flag = 0
    if puzzle[x-1][y] == 0:
        flag = 1
        return flag
    elif x == 0:
        flag = 1
        return flag
    return flag


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # 1 이 단어 들어가는 곳

    k_cnt = 0
    # 가로 탐색
    for i in range(N):
        for j in range(N-K+1):
            cnt1 = 0
            if puzzle[i][j] == 1 and start1(i, j) == 1:

                for k in range(j, N):

                    if puzzle[i][k] == 1:
                        cnt1 += 1
                    elif puzzle[i][k] == 0:
                        if cnt1 != K:
                            cnt1 = 0
                            break
                        else:
                            break

            if cnt1 == K:
                k_cnt += 1

    # 세로 탐색
    # for i in range(N):
    #     for j in range(N-K+1):
            cnt2 = 0
            if puzzle[j][i] == 1 and start2(j, i) == 1:
                for k in range(j, N):
                    if puzzle[k][i] == 1:
                        cnt2 += 1
                    elif puzzle[k][i] == 0:
                        if cnt2 != K:
                            cnt2 = 0
                            break
                        else:
                            break

            if cnt2 == K:
                k_cnt += 1

    print('#{} {}'.format(tc, k_cnt))