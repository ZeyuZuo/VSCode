#define _CRT_SECURE_NO_WARNINGS 1
#include<iostream>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

#define N 1000000010
typedef long long LL;
int n, len;
int a[100010], b[100010];

bool compare(vector<int>& a, vector<int>& b)
{
	return a[0] < b[0];
}

vector<vector<int>> merge(vector<vector<int>>& list)
{
	sort(list.begin(), list.end(), compare);
	vector<vector<int>> result;
	result.push_back(list[0]);
	for (int i = 1; i < list.size(); i++)
	{
		if (list[i][0] <= result.back()[1] + 1)
			result.back()[1] = max(list[i][1], result.back()[1]);
		else
			result.push_back(list[i]);
	}
	return result;
}

bool check(int mid)
{
	vector<vector<int>> tmp;

	for (int i = 0; i < n; i++)
	{
		vector<int> f;
		if (mid < b[i])
			continue;
		int dis = mid - b[i];
		f.push_back(max(1, a[i] - dis));
		f.push_back(min(len, a[i] + dis));
		tmp.push_back(f);
	}
	if (tmp.empty())
		return false;
	vector<vector<int>> result = merge(tmp);
	if (result.size() == 1)
		if (result[0][0] == 1 && result[0][1] == len)
			return true;
	return false;
}

int main()
{
	int Max = -1;
	cin >> n >> len;
	for (int i = 0; i < n; i++)
	{
		scanf("%d%d", &a[i], &b[i]);
		Max = max(Max, b[i]);
	}
	Max += len;
	int l = 1, r = Max;
	while (l < r)
	{
		int mid = (r - l) / 2 + l;
		// printf("%d\n", mid);
		if (!check(mid))
			l = mid + 1;
		else
			r = mid;
	}
	printf("%d", r);
	return 0;
}