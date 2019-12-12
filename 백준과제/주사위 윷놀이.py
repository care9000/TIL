import sys
sys.stdin = open('주사위 윷놀이.txt')


bfs()



order = list(map(int, input().split()))
count = [0] * 5
for i in range(10):
    count[order[i] - 1] += 1

my_map = [-1, 2, 4, 6, 8, 10, 12, 14, 16, 18,
          20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
          40, 0, 0, 0, 0, 0, 10, 13, 16, 19,
          25, 30, 35, 40, 0, 0, 0, 0, 0, 20,
          22, 24, 25, 30, 35, 40, 0, 0, 0, 0,
          0, 30, 28, 27, 26, 25, 30, 35, 40, 0,
          0, 0, 0, 0,
          ]
visited = [0] * 4
my_max = 0
bfs(0, 0, 0)
print(my_max)



