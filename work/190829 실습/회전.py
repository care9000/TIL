import sys
sys.stdin = open('회전_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    for i in range(M):
        a = num_list.pop(0)
        num_list.append(a)

    print('#{} {}'.format(tc, num_list[0]))