import sys
sys.stdin = open('격자판_input.txt')

def dfs(x, y, result):

    result += str(data[x][y])

    if len(result) == 7:
        R.append(result)

    else:
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if -1 < nx < 4 and -1 < ny < 4:
                dfs(nx, ny, result)


T = int(input())

for tc in range(1, T+1):
    R=[]
    data = [list(map(int, input().split())) for _ in range(4)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        for j in range(4):
            result = ''
            dfs(i, j, result)

    a=set(R)
    print("#{} {}".format(tc,len(a)))
