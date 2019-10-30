import sys
sys.stdin = open("2자리 소수_input.txt")

T = int(input())
for tc in range(1,T+1):
    a, b = map(int, input().split())

    data = [str(i) for i in range(a,b+1)]
    real = [11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

    dd = []
    cnt = 0
    for i in range(len(data)):
        bb = []
        for j in range(len(data[i])):
            for x in range(j+1,len(data[i])):
                    sosu = int(data[i][j]+data[i][x])
                    if sosu in real:
                        if sosu not in bb:
                            bb.append(sosu)

        dd.append(bb)
    sol =0
    for i in range(len(dd)):
        sol += len(dd[i])

    print(sol)