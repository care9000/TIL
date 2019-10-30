import sys
sys.stdin = open("의석이_input.txt")

T = int(input())

for tc in range(1, T+1):
    data = [list(input()) for _ in range(5)]
    print(data)

    max_len = 0
    for a in range(5):
        if len(data[a]) > max_len:
            max_len = len(data[a])

    for b in range(5):
        if len(data[b]) != max_len:
            for c in range(max_len - len(data[b])):
                data[b].append('')

    result = []
    for i in range(len(data[0])): # 열 길이
        for j in range(5): #행 5
            result.append(data[j][i])

    p = ''.join(result)
    print('#{} {}'.format(tc, p))