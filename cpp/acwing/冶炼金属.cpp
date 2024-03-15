#define _CRT_SECURE_NO_WARNINGS 1
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

#define N 10010
int n;
int a[N], b[N];
double c[N];

bool checkL(int mid)
{
	for (int i = 0; i < n; i++)
	{
		if (!(floor(a[i] * 1.0 / mid) <= b[i]))
			return false;
	}
	return true;
}

bool checkR(int mid)
{
	for (int i = 0; i < n; i++)
	{
		if (!(floor(a[i] * 1.0 / mid) >= b[i]))
			return false;
	}
	return true;
}

int main()
{
	cin >> n;
	double s = 1 << 30, t = -1;;
	int l, r, ll, rr;
	for (int i = 0; i < n; i++)
		scanf("%d%d", &a[i], &b[i]);
	for (int i = 0; i < n; i++)
	{
		c[i] = a[i] * 1.0 / b[i];
		s = min(s, c[i]);
		t = max(t, c[i]);
	}
	ll = (int)floor(s); rr = (int)ceil(t);
	l = 1; r = rr;
	// cout << ll << " " << rr << endl;
	while (l < r)
	{
		int mid = (r - l) / 2 + l;
		// cout << mid << endl;
		if (!checkL(mid))
			l = mid + 1;
		else
			r = mid;
	}
	cout << r << " ";
	l = 1; r = rr;
	while (l < r)
	{
		int mid = l + r + 1 >> 1;
		// cout << l << " " << r << " " << mid << endl;
		if (checkR(mid))
			l = mid;
		else
			r = mid - 1;
	}
	cout << r;
	return 0;
}