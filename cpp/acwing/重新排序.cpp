#define _CRT_SECURE_NO_WARNINGS 1
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

#define N 100010

typedef long long LL;
int n, m;
LL a[N];
int b[N] = { 0 };
int cnt[N] = { 0 };

bool compare(LL x, LL y)
{
	return x > y;
}

int main()
{
	cin >> n;
	for (int i = 1; i <= n; i++)
		scanf("%lld", &a[i]);
	int l, r;
	LL sum2 = 0, sum1 = 0;
	cin >> m;
	while (m--)
	{
		scanf("%d%d", &l, &r);
		b[l]++;
		b[r + 1]--;
	}
	for (int i = 1; i <= n; i++)
		b[i] = b[i - 1] + b[i];
	for (int i = 1; i <= n; i++)
		sum1 += a[i] * b[i];
	sort(a + 1, a + n + 1, compare);
	sort(b + 1, b + n + 1, compare);
	for (int i = 1; i <= n; i++)
		sum2 += a[i] * b[i];
	cout << sum2 - sum1;
	return 0;
}