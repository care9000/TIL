import sys
sys.stdin =open('섬의 개수.txt')


def dfs(i, j):
    visited[i][j] = 1
    for k in range(8):
        i_test = i + i_move[k]
        j_test = j + j_move[k]
        if ispass(i_test, j_test):
            dfs(i_test, j_test)



def ispass(i, j):
    if 0 <= i < h and 0 <= j <w  and data[i][j] == 1 and visited[i][j] == 0:
        return True
    return False


i_move = [0, 0, -1, 1, -1, -1, 1, 1]
j_move = [-1, 1, 0, 0, -1, 1, -1, 1]


while 1:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    else:
        data = [list(map(int, input(). split())) for _ in range(h)]
        visited = [[0 for _ in range(w)] for _ in range(h)]
        cnt = 0
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 1 and visited[i][j] == 0:
                    cnt += 1
                    dfs(i, j)
        print(cnt)
