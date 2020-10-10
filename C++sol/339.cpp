#include <iostream>
using namespace std;
int main () {
    int n, k;
    while (cin >> n and n!=0) {
        k = n;
        for (int i = 2; i*i <= n; i++) {
            if (n % i == 0) {
                while (n % i == 0) {
                    n/= i;
                }
                k-=k/i;
            }
        }
        if (n > 1) {
            k-=k/n;
        }
        cout << k << endl;
    }
    return 0;   
}