import sys
sys.stdin = open('이진탐색_input.txt')

def bs(pages, goal):
    l = 1
    r = pages
    c = (l + r) // 2
    cnt = 0
    while l != c or r != c:

        if goal > c:
            l = c
            cnt += 1

        elif goal < c:
            r = c
            cnt += 1

        elif c == goal:
            cnt += 1
            return cnt

        c = (l + r) // 2


T=int(input())
for tc in range(T):
    p, a, b = map(int, input().split())

    result = ''

    if bs(p, a) < bs(p, b):
        result += 'A'
    elif bs(p, a) > bs(p, b):
        result += 'B'
    else:
        result += '0'

    print('#{} {}'.format(tc+1, result))