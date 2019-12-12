import sys
sys.stdin = open('14501_퇴사.txt')

def check_schedule():
    global max_cost
    day_list = [0] * N
    cost = 0
    for i in range(N):
        if A[i] == 1:
            start_day = schedule[i][2]
            for j in range(schedule[i][0]):
                if  start_day + j < N and day_list[start_day + j] == 0:
                    day_list[start_day + j] += 1
                else:
                    return
            cost += schedule[i][1]
    if max_cost < cost:
        max_cost = cost



def PowerSet(N, m):
    if N == m:
        check_schedule()

    else:
        A[m] = 1
        PowerSet(N, m + 1)
        A[m] = 0
        PowerSet(N, m + 1)

N = int(input())

schedule = [list(map(int, input().split())) for _ in range(N)]

day = 0
for i in range(len(schedule)):
    schedule[i].append(day)
    day += 1

A = [0] * N
max_cost = 0
PowerSet(N, 0)
print(max_cost)