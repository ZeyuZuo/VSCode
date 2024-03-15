#define _CRT_SECURE_NO_WARNINGS 1
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

#define N 100010

int n;
int a[N], b[N], c[N];

bool compare(int x, int y)
{
	return x < y;
}

int main()
{
	cin >> n;
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	for (int i = 0; i < n; i++)
		scanf("%d", &b[i]);
	for (int i = 0; i < n; i++)
		scanf("%d", &c[i]);
	sort(a, a + n, compare);
	sort(b, b + n, compare);
	sort(c, c + n, compare);
	long long sum = 0;
	for (int i = 0; i < n; i++)
	{
		// cout << b[i] << endl;
		int l = 0, r = n;
		while (l < r)
		{
			int mid = (r - l) / 2 + l;
			if (a[mid] < b[i])
				l = mid + 1;
			else
				r = mid;
		}
		// cout << r << endl;
		long long x = r;
		l = 0; r = n;
		while (l < r)
		{
			int mid = (r - l) / 2 + l;
			if (c[mid] <= b[i])
				l = mid + 1;
			else
				r = mid;
		}
		// cout << r << endl;
		// cout << n - r << endl;
		long long y = n - r;
		sum += x * y;
		// cout << sum << endl << endl;
	}
	cout << sum << endl;
	return 0;
}