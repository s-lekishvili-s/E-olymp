#include <iostream>
#include <vector>
#include <string.h>
using namespace std;
int m, n, d[1 << 10][1 << 10];
long a[12][1 << 10];
int bit(int x, int pos)
{
	if (pos < 0) return 0;
	return (x & (1 << pos));
}
void go(int p1, int p2, int pos)
{
	if (pos == m)
	{
		d[p1][p2] = 1;
		return;
	}
	if (bit(p1, pos) == 0)
	{
		go(p1, p2 + (1LL << pos), pos + 1);
		if (pos < m - 1 && bit(p1, pos + 1) == 0) go(p1, p2, pos + 2);
	}
	else go(p1, p2, pos + 1);
}

int main() {
	int i, p1, p2;
	scanf("%d %d", &m, &n);
	memset(d, 0, sizeof(d));
	memset(a, 0, sizeof(a));
	for (i = 0; i < (1 << m); i++) go(i, 0, 0);
	a[1][0] = 1;
	for (i = 2; i <= n + 1; i++)
		for (p1 = 0; p1 < (1 << m); p1++)
		{
			a[i][p1] = 0;
			for (p2 = 0; p2 < (1 << m); p2++) a[i][p1] += a[i - 1][p2] * d[p2][p1];
		}

	printf("%ld\n", a[n + 1][0]);
	return 0;
}