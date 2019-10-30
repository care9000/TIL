import sys

sys.stdin = open("노드의합_input.txt")

def post_pre(T): # 후위
    if T != 0:
        post_pre(tree[T][0])
        post_pre(tree[T][1])
        tree[T][3] += tree[tree[T][0]][3] + tree[tree[T][1]][3]

T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]
    tree = [[0] * 4 for i in range(N + 1)]

    # print(info)

    for i in range(1, N//2 + 1):
        if i*2 <= N:
            tree[i][0] = i*2
            tree[i*2][2] = i

        if i*2 + 1 <= N:
            tree[i][1] = (i*2) + 1
            tree[(i*2) + 1][2] = i


    for j in range(len(info)):
        A = info[j]
        tree[A[0]][3] = A[1]


    post_pre(1)

    # [print(i, tree[i]) for i in range(len(tree))]

    result = tree[L][3]

    print('#{} {}'.format(tc, result))