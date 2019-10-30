import sys
sys.stdin = open('길찾기_input.txt')

def dfs(x):
    visited[x] = 1

    for k in range(len(road_map[x])):
        if road_map[x][k] == 1:
            dfs(k)



T = 10

for tc in range(1, T+1):
    N, E = map(int, input().split())
    datas = list(map(int, input().split()))
    visited = [0] * 100
    road_map = [[0]*100 for _ in range(100)]
    road_info = []
    for i in range(0, len(datas), 2):
        road_info.append([datas[i], datas[i+1]])

    for j in range(len(road_info)):
        road_map[road_info[j][0]][road_info[j][1]] = 1

    dfs(0)

    flag = 0
    if visited[99] == 1:
        flag = 1

    print('#{} {}'.format(tc, flag))