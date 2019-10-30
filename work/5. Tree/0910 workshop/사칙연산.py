import sys
sys.stdin = open('사칙연산_input.txt')

def post_pre(T): # 후위
    if T !=0:
        post_pre(tree[T][0])
        post_pre(tree[T][1])
        cal_idx.append(T)
        # print('{}'.format(T), end=" ")

T = 10

for tc in range(1, T+1):
    N = int(input())
    data = [input().split() for _ in range(N)]

    tree = [[0] * 4 for _ in range(N + 1)]

    operator = '-+/*'
    # print(data)

    cal_idx = []

    for i in range(len(data)):
        A = data[i]
        if len(A) == 4:
            tree[int(A[0])][3] = A[1] # 연산자 입력
            # 부모 입력
            tree[int(A[2])][2] = int(A[0])
            tree[int(A[3])][2] = int(A[0])
            # 자식 입력
            tree[int(A[0])][0] = int(A[2])
            tree[int(A[0])][1] = int(A[3])

        elif len(A) == 2:
            tree[int(A[0])][3] = int(A[1])

    # [print(i, tree[i]) for i in range(len(tree))]

    post_pre(1)

    # print(cal_idx)

    stack = []
    cnt = 0

    for j in cal_idx:
        if str(tree[j][3]) not in operator:
            stack.append(tree[j][3])

        elif tree[j][3] in operator:
            if tree[j][3] == '-':
                a = stack.pop(0)
                b = stack.pop(0)
                c = a - b
                stack.append(c)

    print('#{} {}'.format(tc, stack[0]))



