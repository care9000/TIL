import sys
sys.stdin = open('장훈이_input.txt')

def powerset(n, k, current_sum):

    # if current_sum > B:
    #     compare.append(current_sum)

    if n == k:          # Basis Part
        printSet(n, current_sum)

    else:               # Inductive Part
        A[k] = 1
        powerset(n, k+1, current_sum + height[k])
        A[k] = 0
        powerset(n, k+1, current_sum)

def printSet(n, current_sum):
    result = 0
    for i in range(n):
        if A[i] == 1:
            result += height[i]

    if result >= B:
        compare.append(current_sum)



T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split()) # N명, 높이 B
    A = [0 for _ in range(N)]
    height = list(map(int, input().split()))
    compare = []
    # print(N, B)
    # print(height)

    powerset(N, 0, 0)
    # print(compare)
    min = 0xffffff # 16진수로 큰값
    for i in range(len(compare)):
        if compare[i] - B <= min:
            min = compare[i] - B

    print('#{} {}'.format(tc, min))