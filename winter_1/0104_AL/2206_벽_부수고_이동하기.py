import sys
sys.stdin = open('2206_벽_부수고_이동하기.txt')

import collections
def bfs(i, j):
    global result
    q = collections.deque([])
    q.append([i, j, 1, 1])
    visited[i][j] = 1
    while len(q):
        location = q.popleft()
        x = location[0]
        y = location[1]
        distance = location[2]
        chance = location[3]
        if distance > result:
            return
        for k in range(4):
            x_tem = x + dx[k]
            y_tem = y + dy[k]
            if ispass(x_tem, y_tem):
                if my_map[x_tem][y_tem] == 0:
                    visited[x_tem][y_tem] = distance + 1
                    if x_tem == N - 1 and y_tem == M - 1:
                        result = distance + 1
                        return
                    q.append([x_tem, y_tem, distance + 1, chance])
                else:
                    if chance:
                        if visited[x_tem][y_tem] == 0:
                            visited[x_tem][y_tem] = distance + 1
                            if x_tem == N - 1 and y_tem == M - 1:
                                result = distance + 1
                                return
                            q.append([x_tem, y_tem, distance + 1, chance - 1])


def ispass(i, j):
    if -1 < i < N and -1 < j < M:
        return True
    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


N, M = map(int, input().split())
dummy = [input() for _ in range(N)]

my_map = [[0 for _ in range(M)] for _ in range(N)]
wall_location_list = []
for i in range(N):
    for j in range(M):
        my_map[i][j] = int(dummy[i][j])

result = 987654321
visited = [[0 for _ in range(M)] for _ in range(N)]
bfs(0, 0)
if result != 987654321:
    print(result)
else:
    print(-1)
