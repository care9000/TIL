import sys
sys.stdin = open('2206_벽_부수고_이동하기.txt')

import collections

def bfs(i, j):
    visited[i][j] = 1
    q = collections.deque([])
    q.append([i, j])
    while len(q):
        location = q.popleft()
        i_location = location[0]
        j_location = location[1]
        for move in range(4):
            i_tem = i_location + i_move[move]
            j_tem = j_location + j_move[move]
            if ispass(i_tem, j_tem):
                visited[i_tem][j_tem] = visited[i_location][j_location] + 1
                if i_tem == N - 1 and j_tem == M - 1:
                    return
                q.append([i_tem, j_tem])



def ispass(i, j):
    if -1 < i < N and -1 < j < M and visited[i][j] == 0 and my_map[i][j] == 0:
        return True
    return False


i_move = [0, 0, -1, 1]
j_move = [-1, 1, 0, 0]




N, M = map(int, input().split())
my_map = [list(map(int, input())) for _ in range(N)]

wall_location_list = []
for i in range(N):
    for j in range(M):
        if my_map[i][j] == 1:
            wall_location_list.append([i, j])

min_distance = 987654321
for wall_location in wall_location_list:
    my_map[wall_location[0]][wall_location[1]] = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    bfs(0, 0)
    if min_distance > visited[-1][-1] and visited[-1][-1]:
        min_distance = visited[-1][-1]
    my_map[wall_location[0]][wall_location[1]] = 1


if min_distance == 987654321:
    min_distance = -1
print(min_distance)