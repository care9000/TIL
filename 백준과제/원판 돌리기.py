import sys

sys.stdin = open('원판 돌리기.txt')
import collections
#N 개의 원판 M개의 원판내의 숫자 T개의 원판 회전
N, M, T = map(int, input().split())

# N개의 원판 받기
disk = list(collections.deque(map(int, input().split())) for _ in range(N))
# 회전시킬 원판 ( 1번쨰의 원판을 시계/반시계 방향으로 (3번째숫자)만큼 회전)
my_try = [list(map(int ,input().split())) for _ in range(T)]
#회전 시작
for i in range(T):
    # 회전 시킬 원판의 갯수(my_try 의 0번째 변수의 배수)
    mul_disk_list = []
    mul_num = 1
    while 1:
        if mul_num * my_try[i][0] <= len(disk):
            mul_disk_list.append(my_try[i][0] * mul_num)
        else:
            break
        mul_num += 1
    # 시계 회전
    if my_try[i][1] == 0:
        for mul_disk in mul_disk_list:
            # 몇번 회전 할 건지
            for _ in range(my_try[i][2]):
                dummy = disk[mul_disk - 1].pop()
                disk[mul_disk - 1].appendleft(dummy)
    # 반시계 회전
    else:
        for mul_disk in mul_disk_list:
            for _ in range(my_try[i][2]):
                dummy = disk[mul_disk - 1].popleft()
                disk[mul_disk - 1].append(dummy)
    # 인접에 있는지 확인
    check_list = [[0] * M for _ in range(N)]
    # 첫번째 원판 확인
    for j in range(M):
        #양옆 확인
        if disk[0][j] != 0:
            if disk[0][j] == disk[0][j - 1]:
                check_list[0][j] = 1
            elif disk[0][j] == disk[0][(j + 1) % M]:
                check_list[0][j] = 1
            # 바깥쪽 원판 확인
            elif disk[0][j] == disk[1][j]:
                check_list[0][j] = 1
    # 가운데 원판 확인
    for k in range(1, N - 1):
        for j in range(M):
            if disk[k][j] != 0:
                if disk[k][j] == disk[k][j - 1]:
                    check_list[k][j] = 1
                elif disk[k][j] == disk[k][(j + 1) % M]:
                    check_list[k][j] = 1
                # 바깥쪽 원판 확인
                elif disk[k][j] == disk[k + 1][j]:
                    check_list[k][j] = 1
                # 안쪽 원판확인
                elif disk[k][j] == disk[k - 1][j]:
                    check_list[k][j] = 1

    # 마지막 원판 확인
    for j in range(M):
        if disk[-1][j] != 0:
        #양옆 확인
            if disk[-1][j] == disk[-1][j - 1]:
                check_list[-1][j] = 1
            elif disk[-1][j] == disk[-1][(j + 1) % M]:
                check_list[-1][j] = 1
            # 바깥쪽 원판 확인
            elif disk[-1][j] == disk[-2][j]:
                check_list[-1][j] = 1
    # flag를 새워서 인접이 없을경우 평균값조정을 위해 설정
    flag = 0
    # print(check_list)
    # print(disk)
    # [print(disk[a]) for a in range(N)]
    # print()
    # 만약 인접이 있으면 0으로 만들기
    for a in range(N):
        for b in range(M):
            if check_list[a][b] == 1:
                disk[a][b] = 0
                flag = 1
    # 인접이 없으면 평균보다 작으면 + 1 크면 - 1 해줌
    if flag == 0:
        my_tem = 0
        cnt = 0
        for a in range(N):
            for b in range(M):
                if disk[a][b] != 0:
                    my_tem += disk[a][b]
                    cnt += 1
        if cnt != 0:
            my_avg = my_tem / cnt
            for a in range(N):
                for b in range(M):
                    if disk[a][b] > my_avg:
                        disk[a][b] -= 1
                    elif disk[a][b] != 0 and disk[a][b] < my_avg:
                        disk[a][b] += 1
    # [print(disk[a]) for a in range(N)]
    # print()




my_sum = 0
for i in range(N):
    for j in range(M):
        if disk[i][j] != 0:
            my_sum += disk[i][j]
print(my_sum)

