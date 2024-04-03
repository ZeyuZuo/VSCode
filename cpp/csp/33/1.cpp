/**
 * @author: Zeyu Zuo
 * @date: 2024-04-03 19:35:26
 */
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
#define N 1000
int num[N] = { 0 };
int sum[N] = { 0 };
int main()
{
    int n, m, s, t;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        cin >> s;
        int is[N] = { 0 };
        for (int j = 0; j < s; j++)
        {
            cin >> t;
            sum[t]++;
            if (!is[t])
            {
                num[t]++;
                is[t] = 1;
            }
        }
    }
    for (int i = 1; i <= m; i++)
    {
        cout << num[i] << " " << sum[i] << endl;
    }
    return 0;
}