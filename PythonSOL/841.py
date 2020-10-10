N=int(input())
A=(N+2)*[(N+2)*[0]]
A[0]=A[N+1]=(N+2)*[-1]
for i in range(1,N+1):
    A[i]=[-1]+N*[0]+[-1]
Di=(0,1,0,-1)
Dj=(1,0,-1,0)
M,i,j,m=0,1,0,0
while M<N*N:
    M+=1
    if A[i+Di[m]][j+Dj[m]]:
        m=(m+1)%4;
    i+=Di[m]
    j+=Dj[m]
    A[i][j]=M
for i in range(1,N+1):
    for j in range(1,N+1):
        print(A[i][j],end=' ')
    print()