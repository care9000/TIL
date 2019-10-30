import sys
sys.stdin = open('이진힙_input.txt')


def compare(s):
    if s!=0:
        if tree[s][3] < tree[tree[s][2]][3]:
            tree[s][3], tree[tree[s][2]][3] = tree[tree[s][2]][3], tree[s][3]
            compare(tree[s][2])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    tree = [[0] * 4 for _ in range(N+1)]
    sorting_idx = []

    for i in range(1, N//2 + 1):
        if i*2 <= N:
            tree[i][0] = i*2
            tree[i*2][2] = i

        if i*2 + 1 <= N:
            tree[i][1] = (i*2) + 1
            tree[(i*2) + 1][2] = i

    print(tree)


    [print(i, tree[i]) for i in range(len(tree))]


    for k in range(len(nums)):
        tree[k+1][3] = nums[k]
        compare(k+1)

    [print(i, tree[i]) for i in range(len(tree))]

    parents_a = []  # a부모들

    c = 1  # a 조상들
    while c != 0:
        c = tree[N][2]
        parents_a.append(c)
        N = c

    print(parents_a)
    result = 0
    for l in parents_a:
        result += tree[l][3]

    print('#{} {}'.format(tc, result))