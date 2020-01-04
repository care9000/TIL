import sys
sys.stdin = open('17143_낚시왕.txt')

# R(세로), C(가로), M(상어 수)

R, C, M = map(int, input().split())

# r(상어_세로), c(상어_가로), s(상어 속력), d(이동방향), z(상어 크기)

shark_info = [list(map(int, input().split())) for _ in range(M)]

person = 1
fish = M
Caught_fish_size = 0
fish_life_list = [1] * M
if M == 0:
    print(0)
else:
    while person < C + 1 and fish > 0:

        # 상어가 있을 경우 상어 캐치

        location = 987654321
        shark_location = 0

        for i in range(len(shark_info)):
            if shark_info[i][4]:
                if shark_info[i][3] == 1 or shark_info[i][3] == 2:
                    if shark_info[i][1] < person:
                        shark_info[i][4] = 0
                        shark_info[i][2] = 0
                        fish -= 1
                if shark_info[i][1] == person:
                    if location > shark_info[i][0]:
                        shark_location = i
                        location = shark_info[i][0]
        if location != 987654321:
            shark_info[shark_location][0] = -1
            shark_info[shark_location][1] = -1
            Caught_fish_size += shark_info[shark_location][4]
            shark_info[shark_location][4] = 0
            shark_info[shark_location][2] = 0
            fish -= 1
        if fish == 0:
            break


        # 상어 위치 이동
        for i in range(len(shark_info)):
            # 상어의 크기가 0 이 아니라면
            if shark_info[i][4]:
                # d = 1 이면 위 d = 2 면 아래 d = 3 이면 오른쪽 d = 4 이면 왼쪽
                move = 0
                if shark_info[i][3] == 1 or shark_info[i][3] == 2:
                    while move < (shark_info[i][2] % (R * 2)) - 1 :
                        move += 1
                        # 위로 향할 때
                        if shark_info[i][3] == 1:
                            shark_info[i][0] -= 1
                            if shark_info[i][0] == 0:
                                shark_info[i][0] = 2
                                shark_info[i][3] = 2
                        # 아래로 항할 때
                        elif shark_info[i][3] == 2:
                            shark_info[i][0] += 1
                            if shark_info[i][0] == R + 1:
                                shark_info[i][0] = R - 1
                                shark_info[i][3] = 1

                        # 오른쪽으로 향할 때
                        elif shark_info[i][3] == 3:
                            shark_info[i][1] += 1
                            if shark_info[i][1] == C + 1:
                                shark_info[i][1] = C - 1
                                shark_info[i][3] = 4
                        # 왼쪽으로 향할 때
                        elif shark_info[i][3] == 4:
                            shark_info[i][1] -= 1
                            if shark_info[i][1] == 0:
                                shark_info[i][1] = 2
                                shark_info[i][3] = 3
                if shark_info[i][3] == 3 or shark_info[i][3] == 4:
                    while move < (shark_info[i][2] % (C * 2)) - 1:
                        move += 1
                        # 위로 향할 때
                        if shark_info[i][3] == 1:
                            shark_info[i][0] -= 1
                            if shark_info[i][0] == 0:
                                shark_info[i][0] = 2
                                shark_info[i][3] = 2
                        # 아래로 항할 때
                        elif shark_info[i][3] == 2:
                            shark_info[i][0] += 1
                            if shark_info[i][0] == R + 1:
                                shark_info[i][0] = R - 1
                                shark_info[i][3] = 1

                        # 오른쪽으로 향할 때
                        elif shark_info[i][3] == 3:
                            shark_info[i][1] += 1
                            if shark_info[i][1] == C + 1:
                                shark_info[i][1] = C - 1
                                shark_info[i][3] = 4
                        # 왼쪽으로 향할 때
                        elif shark_info[i][3] == 4:
                            shark_info[i][1] -= 1
                            if shark_info[i][1] == 0:
                                shark_info[i][1] = 2
                                shark_info[i][3] = 3
        #상어 위치가 같을 경우 큰상어가 작은상어 먹음
        for i in range(len(shark_info) - 1):
            if shark_info[i][4]:
                for j in range(i + 1, len(shark_info)):
                    if shark_info[j][4]:
                        if shark_info[i][0] == shark_info[j][0] and shark_info[i][1] == shark_info[j][1]:
                            if shark_info[i][4] > shark_info[j][4]:
                                shark_info[j][4] = 0
                                shark_info[j][0] = -1
                                shark_info[j][1] = -1
                                shark_info[j][2] = 0
                            else:
                                shark_info[i][4] = 0
                                shark_info[i][0] = -1
                                shark_info[i][1] = -1
                                shark_info[i][2] = 0
        person += 1
        print(shark_info)
    print(Caught_fish_size)