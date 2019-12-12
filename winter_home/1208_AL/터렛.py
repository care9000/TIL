import sys
sys.stdin = open('터렛.txt')

T = int(input())

for tc in range(T):
    x1, y1, r1, x2, y2, r2, = map(int, input().split())
    pre1 = []
    pre2 = []
    for i in range(0, r1 + 1):

        pre1_x = (x1 - i)
        pre1_y = (y1 - r1 + i)
        if (pre1_x, pre1_y) not in pre1:
            pre1.append((pre1_x, pre1_y))

        pre1_x = (x1 + i)
        pre1_y = (y1 - r1 + i)
        if (pre1_x, pre1_y) not in pre1:
            pre1.append((pre1_x, pre1_y))

        pre1_x = (x1 - i)
        pre1_y = (y1 + r1 - i)
        if (pre1_x, pre1_y) not in pre1:
            pre1.append((pre1_x, pre1_y))

        pre1_x = (x1 + i)
        pre1_y = (y1 + r1 - i)
        if (pre1_x, pre1_y) not in pre1:
            pre1.append((pre1_x, pre1_y))
    for i in range(0, r2 + 1):

        pre2_x = (x2 - i)
        pre2_y = (y2 - r2 + i)
        if (pre2_x, pre2_y) not in pre2:
            pre2.append((pre2_x, pre2_y))

        pre2_x = (x2 + i)
        pre2_y = (y2 - r2 + i)
        if (pre2_x, pre2_y) not in pre2:
            pre2.append((pre2_x, pre2_y))

        pre2_x = (x2 - i)
        pre2_y = (y2 + r2 - i)
        if (pre2_x, pre2_y) not in pre2:
            pre2.append((pre2_x, pre2_y))

        pre2_x = (x2 + i)
        pre2_y = (y2 + r2 - i)
        if (pre2_x, pre2_y) not in pre2:
            pre1.append((pre2_x, pre2_y))
    cnt = 0
    for i in range(len(pre1)):
        if pre1 == pre2:
            cnt = -1
            break
        if pre1[i] in pre2:
            cnt += 1
    print(cnt)