import sys
sys.stdin = open('회문2_input.txt')

for test in range(10):
   T = int(input())
   arr = [[0 for _ in range(100)] for _ in range(100)]
   arr = [list(input()) for _ in range(100)]
   b = 0
   b2 = 0

   for N in range(100, 0, -1):
       for i in range(100-N+1):
           for j in range(100):
               cnt = 0
               cnt2 = 0
               for k in range(N//2):
                   if arr[i+k][j] != arr[i+N-1-k][j]:
                       break
                   else:
                       cnt += 1
               for x in range(N // 2):
                   if arr[j][i+x] != arr[j][i+N-1-x]:
                       break
                   else:
                       cnt2 += 1
               if cnt == N//2:
                   print("#%d %d" % (T, N))
                   b = 1
                   break
               if cnt2 == N // 2:
                   print("#%d %d" % (T, N))
                   b = 1
                   break
           if b == 1:
               break
       N -= 1
       if b == 1:
           break