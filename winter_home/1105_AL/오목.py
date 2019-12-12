import sys
sys.stdin = open('오목.txt')


def check(i, j, ch):
    global flag, i_result, j_result
    i_check = i
    j_check = j
    for k in range(4):
        i_test = i + i_move[k]
        j_test = j + j_move[k]
        cnt = 0
        i_check = i
        j_check = j
        if is_pass(i_test, j_test, ch):
            if i - i_move[k] < 0 or i - i_move[k] == 19 or j - j_move[k] == 19 or j - j_move[k] < 0 or data[i - i_move[k]][j - j_move[k]] != ch:
                for l in range(4):
                    i_check = i_check + i_move[k]
                    j_check = j_check + j_move[k]
                    if is_pass(i_check, j_check, ch):
                        cnt += 1
                    else:
                        break
                if cnt == 4:
                    if i_check + i_move[k] < 0 or i_check + i_move[k] == 19 or j_check + j_move[k] < 0 or j_check + j_move[k] == 19 or data[i_check + i_move[k]][j_check + j_move[k]] != ch:
                        flag = ch
                        i_result = i + 1
                        j_result = j + 1
                        break




def is_pass(i, j, ch):
    if 0 <= i < 19 and 0 <= j < 19 and data[i][j] == ch:
        return True
    return False



data = [list(map(int, input().split())) for _ in range(19)]
i_move = [0, 1, -1, 1]
j_move = [1, 0, 1, 1]
flag = 0
i_result = 0
j_result = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != 0:
            check(i, j, data[i][j])
        if flag != 0:
            break


if flag != 0:
    print(flag)
    print(i_result, j_result)
else:
    print(flag)