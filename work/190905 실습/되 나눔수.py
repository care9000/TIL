import sys
sys.stdin = open('되 나눔수_input.txt')

T = int(input())

for tc in range(1,T+1):
    # 약수의 갯수를 구하고  그 갯수로 나누어 떨어지는 애들 구하기
    a, b = map(int, input().split())

    data = [i for i in range(a, b+1)]
    result = 0
    c = []

    for i in range(len(data)):
        cnt = 0
        for j in range(1, data[i]+1):
            if data[i] % j == 0:
                cnt += 1
        c.append(cnt)

    for i in range(len(data)):
        if data[i] % c[i] == 0:
            result += 1

    print(result)