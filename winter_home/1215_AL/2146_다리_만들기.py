import sys
sys.stdin = open('2146_다리_만들기.txt')

import collections

def distance():
    global min_bridge
    for i in range(len(island_location) - 1):
        for ii in range(len(island_location[i])):
            for j in range(i + 1, len(island_location)):
                for jj in range(len(island_location[j])):
                    tem_distance = abs(island_location[i][ii][0] - island_location[j][jj][0]) + abs(island_location[i][ii][1] - island_location[j][jj][1])
                    if min_bridge > tem_distance:
                        min_bridge = tem_distance
                    if min_bridge == 2:
                        return

def bfs(i, j, num):
    q = collections.deque([])
    q.append([i, j])
    visited[i][j] = 1
    island[i][j] = num
    tem.append([i, j])
    while len(q):
        location = q.popleft()
        i_location = location[0]
        j_location = location[1]
        for move in range(4):
            i_tem = i_location + i_move[move]
            j_tem = j_location + j_move[move]
            if ispass(i_tem, j_tem) and island[i_tem][j_tem]:
                visited[i_tem][j_tem] = 1
                island[i_tem][j_tem] = num
                q.append([i_tem, j_tem])
                tem.append([i_tem, j_tem])


def ispass(i, j):
    if -1 < i < N and -1 < j < N and visited[i][j] == 0:
        return True
    return False

i_move = [-1, 1, 0, 0]
j_move = [0, 0, -1, 1]


N = int(input())

island = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(N)] for _ in range(N)]

island_num = 0
island_location = []
for i in range(N):
    for j in range(N):
        if island[i][j] and visited[i][j] == 0:
            tem = []
            island_num += 1
            bfs(i, j, island_num)

            island_location.append(tem[:])

min_bridge = 987654321

distance()
print(min_bridge - 1)