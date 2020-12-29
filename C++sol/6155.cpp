#include <iostream>

using namespace std;

int main()
{
    unsigned long long n, m, l;
    cin >> n;
    m = 1;
    l=n;
    while(n--)
    {
        m *=2;
    }
    if(l<1)
        cout<<0;
    else
        cout << m-1;
}