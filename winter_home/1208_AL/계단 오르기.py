import sys
sys.stdin = open('계단 오르기.txt')

def bfs(now, chance, my_tem):
    global my_max
    info = now
    q = []
    q.append((info, chance, my_tem))
    i = 0
    while len(q) != i:
        location = q[i][0]
        my_chance = q[i][1]
        my_sum = q[i][2]
        if location == N - 1:
            if my_max < my_sum:
                my_max = my_sum
        else:
            if my_chance < 2:
                for j in range(2):
                    if j == 0:
                        if stair_score[location + 1][1] < my_sum + stair[location + 1]:
                            q.append((location + 1, my_chance + 1, my_sum + stair[location + 1]))
                            stair_score[location + 1][1] = my_sum + stair[location + 1]
                    elif j == 1 and location + 2 < N:
                        if stair_score[location + 2][0] < my_sum + stair[location + 2]:
                            q.append((location + 2, 1, my_sum + stair[location + 2]))
                            stair_score[location + 2][0] = my_sum + stair[location + 2]
            else:
                if location + 2 < N:
                    if stair_score[location + 2][0] < my_sum + stair[location + 2]:
                        q.append((location + 2, 1, my_sum + stair[location + 2]))
                        stair_score[location + 2][0] = my_sum + stair[location + 2]


        i += 1

N = int(input())
stair = [int(input()) for _ in range(N)]
stair_score = [[0] * 2 for _ in range(N)]

my_max = 0
bfs(-1, 0, 0)
print(my_max)
