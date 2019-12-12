import sys
sys.stdin = open('탈옥.txt')
T = int(input())
for tc in range(1, T + 1):
    h, w = map(int, input().split())
    dummy = [input() for _ in range(h)]
    my_map = [[0 for _ in range(w)] for _ in range(h)]
    # 문은 2 사람은 9, 8  벽은 0 길은 1
    people = 9
    for i in range(len(my_map)):
        for j in range(len(my_map[i])):
            if dummy[i][j] == '*':
                my_map[i][j] = 0
            elif dummy[i][j] == '.':
                my_map[i][j] = 1
            elif dummy[i][j] == '#':
                my_map[i][j] = 2
            else:
                my_map[i][j] = people
                people -= 1
    [print(my_map[i]) for i in range(len(my_map))]