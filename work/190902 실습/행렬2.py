import sys
sys.stdin = open("행렬찾기_input.txt")

T = int(input())
for tc in range(1,T+1):
   N = int(input())
   visited = [[0] * N for _ in range(N)]
   data = [list(map(int,input().split())) for _ in range(N)]

   result = []
   cnt = 0

   for i in range(N):
       for j in range(N):
           if data[i][j] != 0:
               cnt += 1
               sizex = 0
               sizey = 0
               for a1 in range(N-i):
                   if data[i + a1][j] != 0:
                       sizey += 1
               for a2 in range(N-j):
                   if data[i][j + a2] != 0:
                       sizex += 1
               result.append([sizey, sizex])

               for b1 in range(i, i+sizey):
                   for b2 in range(j, j+sizex):
                       data[b2][b1] = 0


   print(cnt)
   print(result)