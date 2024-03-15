/*
* @acwing app=acwing.cn id=1232 lang=C++
*
* 1230. K倍区间
*/

// @acwing code start
#include<bits/stdc++.h>
using namespace std;

const int N = 100010;

int n, k;
int arr[N] = { 0 };
long long brr[N] = { 0 };

int main()
{
	long long sum = 0;
	int tmp;
	cin >> n >> k;
	for (int i = 1; i <= n; i++)
	{
		scanf("%d", &tmp);
		arr[i] = (arr[i - 1] + tmp) % k;
		brr[arr[i]]++;
	}
	for (int i = 0; i < k; i++)
	{
		sum += (brr[i]) * (brr[i] - 1) / 2;
	}
	cout << sum + brr[0];
	return 0;
}

// @acwing code end