import sys
sys.stdin = open('subtree_input.txt')

def post_pre(T): # 후위
    global cnt
    if T != 0:
        post_pre(tree[T][0])
        post_pre(tree[T][1])
        cnt += 1

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(E+2)]

    # print(data)

    for i in range(0, len(data), 2):
        if tree[data[i]][0] == 0:
            tree[data[i]][0] = data[i+1] # 왼쪽자식
            tree[data[i+1]][2] = data[i] # 부모
        else:
            tree[data[i]][1] = data[i+1] # 오른쪽자식
            tree[data[i+1]][2] = data[i] # 부모

    # [print(j, tree[j]) for j in range(len(tree))]

    cnt = 0
    post_pre(N)

    print('#{} {}'.format(tc, cnt))
