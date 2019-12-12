import sys

sys.stdin = open('미로 탐색.txt')
import collections
N, M = map(int ,input().split())
dunmmy = [list(input()) for _ in range(N)]


def bfs(i, j):
    q = collections.deque([])
    q.append([i, j])
    # i = 0
    while 0 != len(q):
        # print(q)
        info = q.popleft()
        # 현재 위치와 cnt를 뽑아옴
        i_location = info[0]
        j_location = info[1]
        # if i_location == N - 1 and j_location == M - 1:
        #     return

        for move in range(4):
            i_temp = i_location + i_move[move]
            j_temp = j_location + j_move[move]
            if -1 < i_temp < N and -1 < j_temp < M and mini_map[i_temp][j_temp] == 1 and visited[i_temp][j_temp] > visited[i_location][j_location]:
                visited[i_temp][j_temp] = visited[i_location][j_location] + 1
                if i_temp == N - 1 and j_temp == M - 1:
                    return
                q.append([i_temp, j_temp])
        # i += 1


# 이동 가능한 함수 인지 비교
def ispass(i, j):
    if -1 < i < N and -1 < j < M and mini_map[i][j] == 1:
        return True
    return False



# 네방향 움직 일 수 있으므로 이동 함수 생성
i_move = [0, 0, -1, 1]
j_move = [-1, 1, 0, 0]


# 맵 구성
mini_map = [[0] * M for _ in range(N)]
visited = [[987654321] * M for _ in range(N)]
visited[0][0] = 1
for i in range(N):
    for j in range(M):
        mini_map[i][j] = int(dunmmy[i][j])

bfs(0, 0,)
print(visited[-1][-1])
# [print(visited[i]) for i in range(len(visited))]