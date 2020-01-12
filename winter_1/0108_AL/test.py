def mst_kruskal():
    mst=[]
    mst_cost=0
    while len(mst)<V:
        if len(info)!=0:
            u,v,val=info.pop(0)
        if Find_Set(u) != Find_Set(v):
            Union(u,v)
            mst.append((u,v))
            mst_cost+=val
    return mst_cost


def Find_Set(a):
    if a==PI[a]:
        return a
    else:
        return Find_Set(PI[a])

def Union(a,b):
    if a<b:
        PI[Find_Set(b)]=Find_Set(a)
    else:
        PI[Find_Set(a)]=Find_Set(b)


T=int(input())
for tc in range(1,T+1):
    V,E=map(int,input().split())
    info=[list(map(int,input().split())) for _ in range(E)]
    info.sort(key=lambda x: x[2]) # 오름차순 정렬
    PI = list(range(V + 1))
    a = mst_kruskal()
    print("#{} {}".format(tc,a))