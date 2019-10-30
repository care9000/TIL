import sys
sys.stdin = open('종이_input.txt')

T = int(input())

for tc in range(1, 1+T):
    L2 = int(input())
    L1 = 20

    s1 = [[1 for _ in range(10)] for _ in range(20)]
    s2 = [[1 for _ in range(20)] for _ in range(20)]


    pages = [[0 for i in range(L2)] for _ in range(20)]

    for i in range(len(pages)):
        print('{} {}'.format(i, pages[i]))