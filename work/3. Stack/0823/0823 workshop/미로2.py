import sys
sys.stdin = open("미로_input.txt")

def dfs(i,j):
    visted[i][j]=1

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for s in range(4):
        nx = i + dx[s]
        ny = j + dy[s]

        if -1< nx < 16 and -1< ny < 16:
            if data[nx][ny]==0 and visted[nx][ny]==0:
                dfs(nx,ny)
            elif data[nx][ny]==3 and visted[nx][ny]==0:
                dfs(nx,ny)


T = 10
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(16)]

    visted = [[0]*16 for _ in range(16)]

    ple = 0
    for i in range(len(data)):
        for j in range(len(data)):

            if data[i][j]==2 and visted[i][j]==0:
                dfs(i,j)

            if data[i][j]==3 and visted[i][j]==1:
                ple = 1
                break

    print("#{} {}".format(tc,ple))
