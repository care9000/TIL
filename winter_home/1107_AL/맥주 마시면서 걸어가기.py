import sys
sys.stdin = open('맥주 마시면서 걸어가기.txt')

def bublesorted(a):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i][0] + a[i][1] > a[j][0] + a[j][1]:
                a[i], a[j] = a[j], a[i]
T = int(input())
for tc in range(T):
    n = int(input())
    hp = 100
    data = [list(map(int,input().split())) for _ in range(n + 2)]
    bublesorted(data)
    for i in range(len(data) - 1):
        x = data[i + 1][0] - data[i][0]
        y = data[i + 1][1] - data[i][1]
        if x + y > 1000:
            hp = 0
            break
    if hp == 0:
        print('sad')
    else:
        print('happy')