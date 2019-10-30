import sys
sys.stdin = open("행렬찾기_input.txt")

def size(i, j):
    w_cnt = 0
    h_cnt = 0
    for a in range(j, N):
        if data[i][a] != 0:
            w_cnt += 1
        else:
            break

    for b in range(i, N):
        if data[b][j] != 0:
            h_cnt += 1
        else:
            break

    for s1 in range(i, i+w_cnt):
        for s2 in range(j, j+h_cnt):
            data[j][i] = 0

    s = w_cnt * h_cnt
    matrix_info.append([s, h_cnt, w_cnt])



T = int(input())
for tc in range(1,T+1):
   N = int(input())
   visited = [[0] * N for _ in range(N)]
   data = [list(map(int,input().split())) for _ in range(N)]

   matrix_info = []

   for i in range(N):
       for j in range(N):
           if data[i][j] !=0:
              size(i, j)

   print(tc)
   print(matrix_info)