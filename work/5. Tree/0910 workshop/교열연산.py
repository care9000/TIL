import sys
sys.stdin=open("사칙연산_input.txt")

def postorder(node):
    global result
    if node !=0:
        postorder(Tree[node][0])
        postorder(Tree[node][1])
        if Tree[node][3]=="+":
            Tree[node][4]=Tree[Tree[node][0]][4]+Tree[Tree[node][1]][4]
        elif Tree[node][3]=="-":
            Tree[node][4]=Tree[Tree[node][0]][4]-Tree[Tree[node][1]][4]
        elif Tree[node][3]=="*":
            Tree[node][4]=Tree[Tree[node][0]][4]*Tree[Tree[node][1]][4]
        elif Tree[node][3]=="/":
            Tree[node][4]=Tree[Tree[node][0]][4]//Tree[Tree[node][1]][4]



T=10
op=['+','-','*','/']
for tc in range(1,T+1):
    N=int(input())
    Tree=[[0]*5 for _ in range(N+1)]
    info=[input().split() for _ in range(N)]
    for i in range(len(info)):
        if info[i][1]  not in op:
            Tree[int(info[i][0])][3]=int(info[i][1])
            Tree[int(info[i][0])][4] = int(info[i][1])
        else:
            Tree[int(info[i][0])][3]=info[i][1]
            Tree[int(info[i][0])][0]=int(info[i][2])
            Tree[int(info[i][0])][1] = int(info[i][3])
            Tree[int(info[i][2])][2]=int(info[i][0])
            Tree[int(info[i][3])][2] = int(info[i][0])


    result=0
    postorder(1)
    print("#{} {}".format(tc,int(Tree[1][4])))