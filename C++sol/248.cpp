#include <iostream>
using namespace std;
 
int main() {
    int n,a=0,sum=0;
    cin >> n;
    for(int i=0 ; i<n ; i++){
        a = a + 2;
        sum = sum + a;
    }
    cout << (sum+1) << endl;
    return 0;
}