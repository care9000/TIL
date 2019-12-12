import sys
sys.stdin = open('호텔 방 번호.txt')

try:
    while True:
        N, M = map(int, input().split())
        data = [str(i) for i in range(N, M + 1)]

        cnt = 0
        for i in range(len(data)):
            flag = 0
            for j in range(len(data[i])-1):
                for k in range(j+1,len(data[i])):
                    if data[i][j] == data[i][k]:
                        flag = 1
                        break
            if flag == 0:
                cnt += 1
        print(cnt)
except:
    pass
