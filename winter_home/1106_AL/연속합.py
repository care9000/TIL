import sys
sys.stdin = open('연속합.txt')
N = int(input())
data = list(map(int, input().split()))

result = 0
for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        tem = 0
        for k in range(i, j + 1):
            tem += data[k]
        if tem > result:
            result = tem


if result < data[-1]:
    result = data[-1]
print(result)