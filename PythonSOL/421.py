N,K=map(int,input().split())
ans=0;
N/=K
while N>1:
    ans+=1
    N/=K
print(ans)