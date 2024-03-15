#include<bits/stdc++.h>
using namespace std;

const int N = 5000010;

int n;
string s;
int a[N] = { 0 };


int solve()
{
	int ans = -1;
	for (int i = 1; i <= n; i++)
	{
		a[i] = s[i - 1] - '0' + a[i - 1];
	}
	int m;
	if (n % 2)
		m = (n + 1) / 2;
	else
		m = n / 2;
	for (int i = 0, j = m; j <= n; i++, j++)
	{
		ans = max(ans, a[j] - a[i]);
	}
	return ans;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> n >> s;
		// cout << n << " " << s << endl;
		int ans = solve();
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}