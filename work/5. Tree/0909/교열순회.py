import sys
sys.stdin=open("트리_input.txt")


def preorder(node):
    if node !=0:
        print("{}".format(node), end=" ")
        preorder(data[node][0])
        preorder(data[node][1])

def inorder(node):
    if node !=0:
        inorder(data[node][0])
        print("{}".format(node), end=" ")
        inorder(data[node][1])

def postorder(node):
    if node !=0:
        postorder(data[node][0])
        postorder(data[node][1])
        print("{}".format(node), end=" ")

def printTree():
    for i in range(1, N+1):
        print("%2d %2d %2d %2d" % (i,data[i][0],data[i][1],data[i][2]))



T=1
for tc in range(1,T+1):
    N=int(input())
    info=list(map(int,input().split()))
    data=[[0]*3 for _ in range(N+1)]
    for i in range(0,len(info),2):
        if data[info[i]][0]==0:
            data[info[i+1]][2]=info[i]
            data[info[i]][0]=info[i+1]

        else:
            data[info[i+1]][2]=info[i]
            data[info[i]][1] = info[i + 1]

    printTree()

    print("전위순회 : ",end="")
    preorder(1)
    print()

    print("중위순회 : ", end="")
    inorder(1)
    print()

    print("후위순회 : ", end="")
    postorder(1)
    print()
