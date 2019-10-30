import sys
sys.stdin = open('babygin_input.txt')

def printArr(data, n):
    global flag
    check = 0

    if data[0]==data[1] and data[1]==data[2]:
        check+=1
    if data[3]==data[4] and data[4]==data[5]:
        check+=1

    if data[0]+1==data[1] and data[1]+1==data[2]:
        check+=1
    if data[3]+1 ==data[4] and data[4]+1 ==data[5]:
        check+=1

    if check ==2:
        flag =1
        return

def perm(arr, n, k):
    if flag == 1:
        return

    if n == k:
        printArr(arr, n)

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(arr, n, k+1)
            arr[k], arr[i] = arr[i], arr[k]


T = int(input())

data = [list(map(int, input().split())) for _ in range(T)]

print(data)

flag = 0

for i in range(T):
    temp = data[i]
    perm(temp, len(temp), 0)


    if flag == 1:
        print('baby-gin')
    else:
        print('응 아니야')



