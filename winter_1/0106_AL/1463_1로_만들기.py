import sys
sys.stdin = open('1463_1로_만들기.txt')

import collections
N = int(input())

cnt = 0
data = collections.deque([N])

info = [0 for _ in range(N + 1)]
info[N] = 1

a = 0
cnt = 0
while a != 1:
    a = data.popleft()
    for i in range(3):
        if i == 0 and a % 3 == 0 and info[a // 3] == 0:
            info[a // 3] = info[a] + 1
            data.append(a // 3)
        elif i == 1 and a % 2 == 0 and info[a // 2] == 0:
            info[a // 2] = info[a] + 1
            data.append(a // 2)
        else:
            if info[a - 1] == 0:
                info[a - 1] = info[a] + 1
                data.append(a - 1)
    cnt += 1
print(info[1] - 1)

