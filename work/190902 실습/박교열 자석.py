def iswall(i,j):
    if i<0 or j<0 or i>=100 or j>=100:
        return True
    return False


import sys
sys.stdin=open("자석_input.txt")
T=10

i_move=[-1,1]
j_move=[0,0]

# 1이내려가 2가 올라가
for tc in range(1,T+1):
    N= int(input())
    data= [list(map(int,input().split())) for _ in range(100)]
    # for N in range(100):
    for i in range(99):
        for j in range(100):
            if data[i][j]==1:
                # if iswall(i+1,j)==False:
                if data[i+1][j]==2:
                    data[i][j]=1
                elif data[i+1][j]==1 or data[i+1][j]==4:
                    data[i][j]=1
                else:
                    data[i][j]=4

            if data[i+1][j]==2:
                # if iswall(i-1,j)==False:
                if data[i][j]==1: #인덱싱..!
                    data[i+1][j]=2
                elif data[i][j]==2 or data[i][j]==5:
                    data[i+1][j]=2
                else:
                    data[i+1][j]=5
        for i in range(99):
            for j in range(100):

                if data[i][j]==4:
                    data[i+1][j]=1
                    data[i][j]=0
                elif data[i+1][j] == 5:
                    data[i][j] = 2
                    data[i+1][j] = 0
                elif data[i][j]==3:
                    data[i][j]=0

    for i in range(len(data)):
        if data[0][i]==2:
            data[0][i]=0
        elif data[99][i]==1:
            data[99][i]=0
    cnt=0
    for i in range(99):
        for j in range(100):
            if data[i][j]==1:
                if data[i+1][j]==2:
                    cnt+=1
    print(cnt)

    # for i in range(100):
    #     print(data[i])