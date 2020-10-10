def F(x):
    return len(x)>0
def P(x):
    return x>0
N=int(input())
K=list(filter(F,input().split()))
K=list(map(float,K))
K=list(filter(P,K))
if len(K)==0:
    print("Not Found")
else:
    ans=sum(K)/len(K)
    print("%.2f" % ans)