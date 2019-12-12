import sys
sys.stdin = open('디저트 카페.txt')




i_move = [-1, -1, 1, 1]
j_move = [-1, 1, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(data)):
        for j in range(len(data[i])):
            info = []
            dfs(i, j)