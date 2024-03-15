/*
* @acwing app=acwing.cn id=1240 lang=C++
*
* 1238. 日志统计
*/

// @acwing code start
#include<bits/stdc++.h>
#define N 100010
using namespace std;


int n, d, k;
map<int, vector<int>> maps;
int cnt[N] = { 0 };
bool ans[N];

int main()
{
    cin >> n >> d >> k;
    int ts, id;
    for (int i = 0; i < n; i++)
    {
        scanf("%d%d", &ts, &id);
        if (maps.find(ts) == maps.end())
            maps.insert(pair<int, vector<int>>(ts, vector<int>(1, id)));
        else
            maps.find(ts)->second.push_back(id);
    }
    /*for (auto it = maps.begin(); it != maps.end(); it++)
    {
        cout << it->first << ":" << endl;
        for (int i = 0; i < it->second.size(); i++)
            cout << it->second[i] << " ";
        cout << endl;
    }*/
    auto lit = maps.begin();
    auto rit = maps.begin();
    while (rit != maps.end() && rit->first < lit->first + d)
    {
        for (int i = 0; i < rit->second.size(); i++)
        {
            cnt[rit->second[i]]++;
            if (cnt[rit->second[i]] >= k)
                ans[rit->second[i]] = true;
        }
        rit++;
    }
    while (rit != maps.end())
    {
        for (int i = 0; i < lit->second.size(); i++)
            cnt[lit->second[i]]--;
        lit++;
        while (rit != maps.end() && rit->first < lit->first + d)
        {
            for (int i = 0; i < rit->second.size(); i++)
            {
                cnt[rit->second[i]]++;
                if (cnt[rit->second[i]] >= k)
                    ans[rit->second[i]] = true;
            }
            rit++;
        }
    }
    for (int i = 0; i < N; i++)
        if (ans[i])
            cout << i << endl;
    return 0;
}

// @acwing code end