import sys
sys.stdin = open('공통조상_input.txt')

def post_pre(T): # 후위
    global cnt
    if T != 0:
        post_pre(tree[T][0])
        post_pre(tree[T][1])
        cnt += 1


T = int(input())

for tc in range(1, T+1):
    V, E, a, b = map(int, input().split()) # 정점, 간선, a, b 공통조상
    data = list(map(int, input().split()))
    tree = [[0]*3 for _ in range(V+1)]

    for i in range(0, len(data), 2):
        if tree[data[i]][0] == 0:
            tree[data[i]][0] = data[i+1] # 자식표시
            tree[data[i+1]][2] = data[i]

        else:
            tree[data[i]][1] = data[i+1]
            tree[data[i + 1]][2] = data[i]

    # [print(i, tree[i]) for i in range(len(tree))]

    parents_a = [] # a부모들
    parents_b = [] # b부모들

    c = 1 # a 조상들
    while c != 0:
        c = tree[a][2]
        parents_a.append(c)
        a = c

    d = 1 # b 조상들
    while d != 0:
        d = tree[b][2]
        parents_b.append(d)
        b = d
    # print(parents_a)
    # print(parents_b)

    parents = 0
    for j in range(len(parents_a)):
        if parents_a[j] in parents_b:
            parents = parents_a[j]
            break

    # print(parents)
    cnt = 0
    post_pre(parents)
    # print(cnt)

    print('#{} {} {}'.format(tc, parents, cnt))