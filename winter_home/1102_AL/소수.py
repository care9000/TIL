import sys
sys.stdin =open('소수.txt')
N, M =map(int, input().split())
data = []
for i in range(N, M+1):
    data.append(i)
result = []
if 2 in data:
    result.append(2)
for i in range(len(data)):
    flag = 0
    a = int((data[i]) ** (1 / 2))

    for j in range(2,a+2,1):
        if data[i] % j == 0:
            flag = 1
            break
    if flag == 0:
        if data[i] != 1:
            result.append(data[i])
for i in range(len(result)):
    print(result[i])