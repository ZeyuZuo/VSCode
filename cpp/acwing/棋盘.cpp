#define _CRT_SECURE_NO_WARNINGS 1
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

#define N 2010

int n, m;
int a[N][N] = { 0 }, b[N];

int main()
{
	cin >> n >> m;
	while (m--)
	{
		int x1, y1, x2, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int i = y1; i <= y2; i++)
		{
			a[x1][i] ^= 1;
			a[x2 + 1][i] ^= 1;
		}
	}
	for (int i = 1; i <= n; i++)
		b[i] = a[1][i];
	for (int i = 1; i <= n; i++)
		printf("%d", b[i]);
	printf("\n");
	for (int i = 2; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			b[j] = b[j] ^ a[i][j];
			printf("%d", b[j]);
		}
		printf("\n");
	}
	return 0;
}