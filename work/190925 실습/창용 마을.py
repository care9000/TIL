import sys
sys.stdin = open('창용마을_input.txt')

def dfs(x):
    people[x] = cnt

    for i in range(1, N+1):
        if couple[x][i] == 1 and people[i] == 0:
            dfs(i)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 사람수 N

    data = [list(map(int, input().split())) for _ in range(M)]
    couple = [[0] * (N+1) for _ in range(N+1)] # 짝지 표시
    people = [0] * (N+1) # 방문표시

    # print(data)


    for i in range(len(data)):
        x = data[i][0]
        y = data[i][1]
        couple[x][y], couple[y][x] = 1, 1

    # print(couple)

    cnt = 0

    for i in range(1, N+1):
        if people[i] == 0:
            cnt += 1
            dfs(i)

    print('#{} {}'.format(tc, cnt))