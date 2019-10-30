import sys
sys.stdin = open('중위순회_input.txt')

def cen_pre(T): # 중위
    if T !=0:
        cen_pre(tree[T][0])
        print('{}'.format(tree[T][3]), end='')
        cen_pre(tree[T][1])

T = 10


for tc in range(1, T+1):
    N = int(input())
    tree = [[0] * 4 for _ in range(N+1)]
    data = [list(map(str, input().split())) for _ in range(N)]

    for i in range(len(data)):
        if len(data[i]) == 2:
            tree[int(data[i][0])][3] = data[i][1]

        elif len(data[i]) == 3:
            tree[int(data[i][0])][3] = data[i][1] #정보넣기
            tree[int(data[i][2])][2] = int(data[i][0]) #부모넣기
            tree[int(data[i][0])][0] = int(data[i][2])

        elif len(data[i]) == 4:
            tree[int(data[i][0])][3] = data[i][1]
            tree[int(data[i][2])][2] = int(data[i][0]) # 왼쪽부모
            tree[int(data[i][3])][2] = int(data[i][0]) # 오른쪽부모
            tree[int(data[i][0])][0] = int(data[i][2]) # 왼쪽자식
            tree[int(data[i][0])][1] = int(data[i][3])

    # [print(j, tree[j]) for j in range(len(tree))]
    print('#{}'.format(tc), end=' ')
    cen_pre(1)
    print()