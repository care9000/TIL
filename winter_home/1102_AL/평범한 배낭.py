import sys
sys.stdin = open('평범한 배낭.txt')


def Pem(n,m,my_sum,weight):
    global my_value
    if weight <= M:
        if n == m and my_value < my_sum:
            print(my_value)
            my_value = my_sum
        else:
            if my_value < my_sum :
                my_value = my_sum
            for i in range(m+1,len(data)):
                data[i], data[m] = data[m], data[i]
                if weight + data[m][0] <=M:
                    Pem(n,m+1,data[m][1]+my_sum,weight+data[m][0])
                data[i], data[m] = data[m], data[i]

N, M = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(N)]
my_value=-1
data=[]
for i in range(len(a)):
    if a[i][0]<=M:
        data.append(a[i])

Pem(N,0,0,0)
print(my_value)