import sys
sys.stdin = open('이진탐색_input.txt')

def cen_pre(T): # 중위
    if T != 0:
        cen_pre(tree[T][0])
        input_idx.append(T)
        # print('{}'.format(T), end=" ")
        cen_pre(tree[T][1])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [[0] * 4 for _ in range(N + 1)]

    input_idx = []
    for i in range(1, N//2 + 1):
        if i*2 <= N:
            tree[i][0] = i*2
            tree[i*2][2] = i

        if i*2 + 1 <= N:
            tree[i][1] = (i*2) + 1
            tree[(i*2) + 1][2] = i
    #
    # [print(j, tree[j]) for j in range(len(tree))]

    cen_pre(1)
    print(input_idx)

    for j in range(len(input_idx)):
        tree[input_idx[j]][3] = j+1

    [print(j, tree[j]) for j in range(len(tree))]
    a = N // 2
    print('#{} {} {}'.format(tc, tree[1][3], tree[a][3]))
