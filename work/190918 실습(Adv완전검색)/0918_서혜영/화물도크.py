import sys
sys.stdin = open('화물도크_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    day = [0] * 25

    # print(data)

    data = sorted(data)

    car = 0
    for j in range(len(data)-1, -1, -1):
        t = data[j][1] - data[j][0]
        cnt = 0
        for k in range(t+1): #t = 0,1
            if day[data[j][0] + k] == 0:
                cnt += 1
        if cnt == t or cnt == t+1:
            for k in range(t+1):
                day[data[j][0] + k] = 1
            car += 1

    print('#{} {}'.format(tc, car))
