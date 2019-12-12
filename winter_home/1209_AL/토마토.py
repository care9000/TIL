import sys
sys.stdin = open("토마토.txt")
import collections

def bfs(i, j):
    for move in range(4):
        i_tem = i + i_move[move]
        j_tem = j + j_move[move]
        if -1 < i_tem < N and -1 < j_tem < M and visited[i_tem][j_tem] == 0 and tomato_box[i_tem][j_tem] == 0:
            visited[i_tem][j_tem] = 1
            q.append([i_tem, j_tem])

# 4 방향 이동가능 리스트
i_move = [0, 0, -1, 1]
j_move = [-1, 1, 0, 0]


M, N = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(N)]

ripe_list = collections.deque([])
unripe_count = 0
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            ripe_list.append([i, j])
        elif tomato_box[i][j] == 0:
            unripe_count += 1

# 날짜 초기화
day = 0

if unripe_count:
    visited = [[0 for _ in range(M)] for _ in range(N)]
    # 덜익은 tomato가 있을 때 까지 실행

    while unripe_count:
        now = unripe_count
        day += 1
        q = []
        flag = 0
        while len(ripe_list):
            i, j = ripe_list.popleft()
            visited[i][j] = 1
            bfs(i, j)
        for tomato in q:
            unripe_count -= 1
            ripe_list.append([tomato[0], tomato[1]])
        if now == unripe_count and unripe_count:
            day = -1
            break

        if len(ripe_list) == 0:
            break
print(day)






