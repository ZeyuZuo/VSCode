#define _CRT_SECURE_NO_WARNINGS 1
#include<iostream>
#include<vector>
#include<string>
using namespace std;

int dp[1001][1001] = { 0 };
int main()
{
   int N, V;
   cin >> N >> V;
   int* v = new int[N + 1];
   int* w = new int[N + 1];
   int* s = new int[N + 1];
   for (int i = 1; i <= N; i++)
       cin >> v[i] >> w[i] >> s[i];
   for (int i = 0; i <= V; i++)
       dp[1][i] = min(i / v[1], s[1]) * w[1];
   for (int i = 2; i <= N; i++)
   {
       for (int j = 0; j <= V; j++)
       {
           dp[i][j] = dp[i - 1][j];
           for (int t = 1; (t * v[i] <= j) && (t <= s[i]); t++)
               dp[i][j] = max(dp[i][j], dp[i - 1][j - v[i] * t] + t * w[i]);
       }
   }
   cout << dp[N][V];
   return 0;
}