def Max(a,b):
    if a>b:
        return a
    return b
def Min(a,b):
    if a>b:
        return b
    else:
        return a
ans=["NO","YES"]
T=int(input())
while T:
    T-=1
    N=int(input())
    A=input().split()
    A,B=int(A[0]),int(A[1])
    for i in range(N-1):
        a=input().split()
        a,b=int(a[0]),int(a[1])
        A,B=Max(a,A),Min(b,B)
    print(ans[A<=B])