import sys
sys.stdin = open('지뢰 찾기.txt')


def check(i, j):
    tem = 0
    for k in range(8):
        i_test = i + i_move[k]
        j_test = j + j_move[k]
        if ispass(i_test, j_test):
            if my_map[i_test][j_test] != '.':
                tem += int(my_map[i_test][j_test])
    if tem >= 10:
        data[i][j] = 'M'
    else:
        data[i][j] = str(tem)


def ispass(i, j):
    if 0 <= i < N and 0 <= j < N:
        return True
    return False


i_move = [0, 0, -1, 1, -1, -1, 1, 1]
j_move = [-1, 1, 0, 0, -1, 1, -1, 1]

N = int(input())
my_map = [input() for _ in range(N)]
data = [['0' for _ in range(N)] for _ in range(N)]
for i in range(len(my_map)):
    for j in range(len(my_map[i])):
        if my_map[i][j] == '.':
            check(i, j)
        else:
            data[i][j] = '*'
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end="")
    print()