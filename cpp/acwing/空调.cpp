#define _CRT_SECURE_NO_WARNINGS 1
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

#define N 100010

int n;
int a[N] = { 0 }, b[N];

int main()
{
	cin >> n;
	for (int i = 1; i <= n; i++)
		scanf("%d", &a[i]);
	for (int i = 1; i <= n; i++)
		scanf("%d", &b[i]);
	for (int i = 1; i <= n; i++)
		a[i] -= b[i];
	for (int i = 1; i <= n; i++)
		b[i] = a[i] - a[i - 1];
	int x = 0, y = 0;
	for (int i = 1; i <= n; i++)
		cout << b[i] << endl;
	for (int i = 1; i <= n; i++)
	{
		if (b[i])
			x += b[i];
		else
			y -= b[i];
	}
	cout << max(x, y);
	return 0;
}