import sys
sys.stdin = open('유기농 배추.txt')

import collections

def bfs(i, j):
    global worm
    q = collections.deque([])
    q.append([i, j])
    while len(q):
        location = q.popleft()
        for move in range(4):
            i_tem = location[0] + i_move[move]
            j_tem = location[1] + j_move[move]
            if ispass(i_tem, j_tem):
                visited[i_tem][j_tem] = worm
                q.append([i_tem, j_tem])

# 갈 수 있는지 파악
def ispass(i, j):
    if -1 < i < N and -1 < j < M and farm[i][j] and visited[i][j] == 0:
        return True
    return False

# 4방향 확인
i_move = [0, 0, -1, 1]
j_move = [-1, 1, 0, 0]

T = int(input())
for tc in range(1, T + 1):
    # M(가로), N(세로), K(배추의 개수)
    M, N, K = map(int, input().split())
    cabbage_location = [list(map(int, input().split())) for _ in range(K)]
    farm = [[0 for _ in range(M)] for _ in range(N)]
    for i in cabbage_location:
        farm[i[1]][i[0]] = 1

    # 방문 체크
    visited = [[0 for _ in range(M)] for _ in range(N)]
    worm = 0
    for cabbage in cabbage_location:
        if farm[cabbage[1]][cabbage[0]] == 1 and visited[cabbage[1]][cabbage[0]] == 0:
            visited[cabbage[1]][cabbage[0]] = 1
            worm += 1
            bfs(cabbage[1], cabbage[0])
    print(worm)