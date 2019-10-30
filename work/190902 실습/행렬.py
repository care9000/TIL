import sys
sys.stdin = open("행렬찾기_input.txt")

def dfs(i, j):

    visited[i][j] = cnt

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for z in range(4):
        testx = i + dx[z]
        testy = j + dy[z]
        if -1 < testx < N and -1 < testy < N:
            if data[testx][testy] != 0 and visited[testx][testy] == 0:
                dfs(testx, testy)


T = int(input())
for tc in range(1,T+1):
   N = int(input())
   visited = [[0] * N for _ in range(N)]
   data = [list(map(int,input().split())) for _ in range(N)]

   cnt = 0
   result = []
   for i in range(N):
       for j in range(N):
           if data[i][j] != 0 and visited[i][j] == 0:
               cnt += 1
               dfs(i, j)

               sizex = 0
               sizey = 0
   # cnt_list = [0] + [0]*cnt
   # for a in range(N):
   #     for b in range(N):
   #         for c in range(1, cnt+1):
   #          if visited == c:
   #              cnt_list[c] += 1
               for a in range(N): #0
                   for b in range(N): #01234
                       if visited[a][b] == cnt:
                           for a1 in range(N-b):
                               if visited[a][b + a1] != 0:
                                   sizex += 1
                               elif visited[a][b + a1] == 0:
                                   break

                           for b1 in range(N-a):
                               if visited[a + b1][b] != 0:
                                   sizey += 1
                               elif visited[a + b1][b] == 0:
                                   break
                       # else:
                       #     continue
                       break
                   # break
               result.append([sizex, sizey])
   # print(data)
   # print(visited)
   print(cnt)
   # print(result)