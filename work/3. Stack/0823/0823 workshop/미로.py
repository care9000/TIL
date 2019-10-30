import sys
sys.stdin = open('미로_input.txt')

def dfs(x, y):
    visited[x][y] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for z in range(4):
        testx = x + dx[z]
        testy = y + dy[z]

        # if testx < 0 or testx == N:
        #     continue
        # if testy < 0 or testy == N: #여기서 N은 16
        #     continue
        #     #컨티뉴를 쓰면 위에 for문으로 올라가서 다음 방향을 탐색한다.

        if -1 < testx < 16 and -1 < testy < 16:
            if arr[testx][testy] == '3' and visited[testx][testy] == 0:
                dfs(testx, testy)
            elif arr[testx][testy] == '0' and visited[testx][testy] == 0:
                dfs(testx, testy)



T = 10

for tc in range(1, T+1):
    t = int(input())
    arr = []
    visited = [[0]*16 for _ in range(16)]

    for _ in range(16):
        a = list(input())
        arr.append(a)
    result = 0

    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2' and visited[i][j] == 0:
                dfs(i, j)
            if arr[i][j] == '3' and visited[i][j] == 1:
                result += 1
                break


    print('#{} {}'.format(tc, result))