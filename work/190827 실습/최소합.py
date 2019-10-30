import sys
sys.stdin = open('최소합_input.txt')

# def printArr(n):
#     permutation = []
#
#     for i in range(n):
#         permutation.append(arr[i])
#
#     min_sum(permutation)

def perm(n, k, current_sum):
    global min_value

    if current_sum > min_value:
        return

    if k == n:
        if current_sum < min_value:
            min_value = current_sum

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1, current_sum + data[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k] # 다시 제자리로 돌려놔야한다.

# def min_sum(sum_list):
#
#     global min_value
#
#     sum_list = sum_list
#     sum_value = 0
#
#
#     for b in range(len(sum_list)):
#         sum_value += data[b][sum_list[b]]
#
#
#     if sum_value >= min_value:
#         return min_value
#
#     else:
#         min_value = sum_value

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(N)]
    min_value = 987654321

    perm(N, 0, 0)

    print('#{} {}'.format(tc, min_value))

