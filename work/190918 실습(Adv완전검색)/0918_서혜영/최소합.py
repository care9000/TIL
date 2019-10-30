import sys
sys.stdin = open('최소합_input.txt')

def dfs(x, y, value):
    global min_sum

    if value >= min_sum: #가지치기
        return

    if x == N-1 and y == N-1: #종료조건

        # if value < min_sum:
        min_sum = value
        return

    for z in range(2): # 이건 그냥..
        testx = x + dx[z]
        testy = y + dy[z]
        if -1 < testx < N and -1 <testy < N:
            dfs(testx, testy, value + data[testx][testy])


T = int(input())

dx = [0, 1]
dy = [1, 0]

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # print(N)
    # print(data)

    min_sum = 98756543
    cur_sum = data[0][0]

    dfs(0, 0, cur_sum)

    print('#{} {}'.format(tc, min_sum))