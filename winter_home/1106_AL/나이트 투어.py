import sys
sys.stdin = open('나이트 투어.txt')
a = [input() for _ in range(36)]
data = [[0 for _ in range(2)] for _ in range(36)]
visited = [[0 for _ in range(6)] for _ in range(6)]

for i in range(len(a)):
    for j in range(len(a[i])):
        if j == 0:
            if a[i][0] == 'A':
                data[i][0] = 0
            elif a[i][0] == 'B':
                data[i][0] = 1
            elif a[i][0] == 'C':
                data[i][0] = 2
            elif a[i][0] == 'D':
                data[i][0] = 3
            elif a[i][0] == 'E':
                data[i][0] = 4
            else:
                data[i][0] = 5
        else:
            data[i][1] = int(a[i][1])
# print(data)
flag = 1
for i in range(len(data)-1):
    if visited[data[i][0]][data[i][1]-1] == 0:
        visited[data[i][0]][data[i][1]-1] = 1
        if abs(data[i][0] - data[i + 1][0]) + abs(data[i][1] - data[i + 1][1]) == 3:
            if abs(data[i][0] - data[i + 1][0]) == 2 and abs(data[i][1] - data[i + 1][1]) == 1:
                pass
            elif abs(data[i][0] - data[i + 1][0]) == 1 and abs(data[i][1] - data[i + 1][1]) == 2:
                pass
            else:
                flag = 0
                break
        else:
            flag = 0
            break
    else:
        flag = 0
        break
if abs(data[35][0] - data[0][0]) + abs(data[35][1] - data[0][1]) == 3 and visited[data[35][0]][data[35][1]-1] == 0:
    if abs(data[35][0] - data[0][0]) == 2 and abs(data[35][1] - data[0][1]) == 1:
        pass
    elif abs(data[35][0] - data[0][0]) == 1 and abs(data[35][1] - data[0][1]) == 2:
        pass
    else:
        flag = 0
else:
    flag = 0

if flag == 1:
    print('Valid')
else:
    print('Invalid')
# [print(visited[i]) for i in range(len(visited))]
# print(visited[2][1])