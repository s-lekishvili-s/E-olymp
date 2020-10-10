#include <iostream>
using namespace std;
int main() {
	long i, n, m, res;
	scanf("%ld %ld", &n, &m);
	if (n >= m) res = 0;
	else
	{
		for (res = i = 1; i <= n; i++) res = (res * i) % m;
	}
	printf("%ld\n", res);
	return 0;
}