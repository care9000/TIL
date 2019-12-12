import sys
sys.stdin =open('바이러스.txt')

def dfs(n):
    global com
    com[n] = 1
    for i in range(len(data[n])):
        if data[n][i] == 1 and com[i] == 0:
            dfs(i)



N =int(input())
M =int(input())
z = [list(map(int,input().split())) for _ in range(M)]
com = [0 for _ in range(N+1)]
data =[[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(len(z)):
    data[z[i][0]][z[i][1]] = 1
    data[z[i][1]][z[i][0]] = 1

com[1] = 1
for i in range(len(data[1])):
    if data[1][i] ==1 and com[i] == 0:
        dfs(i)

cnt = 0
for i in range(2,len(com)):
    if com[i] == 1:
        cnt += 1
print(cnt)