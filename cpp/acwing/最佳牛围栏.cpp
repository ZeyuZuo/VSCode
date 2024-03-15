#define _CRT_SECURE_NO_WARNINGS 1
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

#define N 100010
int n, f;
int a[N];
double tmp[N] = { 0 };

bool check(double mid)
{
	for (int i = 1; i <= n; i++)
		tmp[i] = tmp[i - 1] + a[i] - mid;
	double Min = 0;
	for (int i = 0, j = f; j <= n; j++, i++)
	{
		Min = min(Min, tmp[i]);
		if (tmp[j] >= Min)
			return true;
	}
	return false;
}

int main()
{
	cin >> n >> f;
	for (int i = 1; i <= n; i++)
		scanf("%d", &a[i]);
	double l = 0, r = 2000;
	while (r - l > 1e-5)
	{
		double mid = (r + l) / 2;
		if (check(mid))
			l = mid;
		else
			r = mid;
	}
	printf("%d", (int)floor(r * 1000));
	return 0;
}