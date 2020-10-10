T=int(input())
while T:
    T-=1
    S=input()
    N=len(S)
    S="D"+S+"DD"
    ans=0
    for i in range(1,N+1):
        if S[i]=='-' and S[i-1]!='S' and S[i+1]!='S' and S[i+1]!='B' and S[i+2]!='B':
            ans+=1
    print(ans)