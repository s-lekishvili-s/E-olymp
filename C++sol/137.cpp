#include <iostream>

using namespace std;

long GCD(long N,long M)
{
 if(M==0)return N;
 return GCD(M,N%M);
}

int main()
{
    int N,M,P;
    cin>>N>>P;
    while(--N)
    {
        cin>>M;
        P=GCD(P,M);
    }
    cout<<P;
}