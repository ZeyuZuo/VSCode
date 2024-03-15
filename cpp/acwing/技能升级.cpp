#define _CRT_SECURE_NO_WARNINGS 1
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;

#define N 100010
typedef long long LL;

int n, m;
int a[N], b[N];

bool check(int mid)
{
	int sum = 0;
	for (int i = 0; i < n; i++)
	{
		if (a[i] < mid)
			continue;
		int tmp = (a[i] - mid) / b[i] + 1;
		sum += tmp;
	}
	if (sum > m)
		return true;
	return false;
}

LL cal(int x)
{
	LL sum = 0;
	for (int i = 0; i < n; i++)
	{
		if (a[i] < x)
			continue;
		LL start = a[i];
		LL times = (a[i] - x) / b[i];
		LL end = a[i] - times * b[i];
		LL tmp = (start + end) / 2 * (times + 1);
		// cout << tmp << endl;
		sum += tmp;
	}
	return sum;
}

int main()
{
	cin >> n >> m;
	int l = 0, r = 0;
	for (int i = 0; i < n; i++)
	{
		scanf("%d%d", &a[i], &b[i]);
		r = max(r, a[i]);
	}
	while (l < r)
	{
		int mid = l + r + 1 >> 1;
		if (check(mid))
			l = mid ;
		else
			r = mid - 1;
	}
	cout << r << endl;
	LL ans = cal(r+1);
	cout << ans;
	return 0;
}