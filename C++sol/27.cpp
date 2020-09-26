#include <iostream>
using namespace std;
int main(){
    unsigned long in_val, tmp_val, power = 1;
    cin >> in_val;
    tmp_val = in_val;
    while(tmp_val){
        tmp_val /= 2;
        power *= 2;
    }
    tmp_val = in_val;
    unsigned long max_val = in_val;
    do{
        in_val = in_val << 1;
        in_val = in_val % power + (in_val >= power ? 1 : 0);
        if (max_val < in_val) max_val = in_val;
    }while (tmp_val != in_val );
    cout << max_val << endl;
    
    return 0;
}