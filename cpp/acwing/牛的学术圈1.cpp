#define _CRT_SECURE_NO_WARNINGS 1
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

#define N 100010

int n, L;
int a[N], b[N];

bool compare(int x, int y)
{
	return x < y;
}

bool check(int mid)
{
	for (int i = 1; i <= n; i++)
		b[i] = mid - a[i];
	int t = 0, sum = 0;
	sort(b + 1, b + n + 1, compare);
	for (int i = 1; i <= n && t < mid; i++)
	{
		t++;
		if (b[i] <= 0)
			continue;
		sum += b[i];
	}
	if (sum <= L)
		return true;
	return false;
}

int main()
{
	cin >> n >> L;
	for (int i = 1; i <= n; i++)
		scanf("%d", &a[i]);
	int l = 0, r = n;
	while (l < r)
	{
		int mid = (r + l + 1) / 2;
		if (check(mid))
			l = mid;
		else
			r = mid - 1;
	}
	cout << l;
	return 0;
}