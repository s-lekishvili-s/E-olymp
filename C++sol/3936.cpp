#include <iostream>

using namespace std;

void hanoi(int n, int f, int t, int a)
{
	if (n == 0) return;
	hanoi(n - 1, f, a, t);
	printf("%d %d\n", f, t);
	hanoi(n - 1, a, t, f);
}

int main() {
	int n; cin >> n;
	hanoi(n, 1, 2, 3);
	return 0;
}