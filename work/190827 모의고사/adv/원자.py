import sys
sys.stdin = open('원자_input.txt')


def s_move(big_data):
    if len(big_data) == 0:
        return energy_sum

    for i in range(len(big_data)):
        if big_data[i][2] == 0:
            big_data[i][1] += 0.5

        elif big_data[i][2] == 1: # 하
            big_data[i][1] -= 0.5

        elif big_data[i][2] == 2: # 좌
            big_data[i][0] -= 0.5

        elif big_data[i][2] == 3: # 우 x증가
            big_data[i][0] += 0.5



def check(big_data):
    global energy_sum

    if len(big_data) == 0:
        return energy_sum

    for i in range(len(big_data)):
        standx = big_data[i][0]
        standy = big_data[i][1]
        for j in range(i+1, len(big_data)):
            if standx == big_data[j][0] and standy == big_data[j][1]:
                energy_sum += big_data[i][3]
                energy_sum += big_data[j][3]
                big_data.remove(big_data[i])
                big_data.remove(big_data[j])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 1000 for _ in range(1000)]
    big_data = []
    energy_sum = 0

    for i in range(N):
        data = list(map(int, input().split()))
        big_data.append(data)

    for i in range(2):
        s_move(big_data)
        check(big_data)

    print('#{} {}'.format(tc, energy_sum))


