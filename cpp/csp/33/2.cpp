/**
 * @author: Zeyu Zuo
 * @date: 2024-04-03 19:35:16
 */
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

set<string> s1;
set<string> s2;

string lower(string s)
{
    for (int i = 0; i < s.length(); i++)
        if (s[i] >= 'a' && s[i] <= 'z')
            s[i] -= 'a' - 'A';
    return s;
}

int main()
{
    int n, m;
    cin >> n >> m;
    string tmp;
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        s1.insert(lower(tmp));
    }
    for (int i = 0; i < m; i++)
    {
        cin >> tmp;
        s2.insert(lower(tmp));
    }
    set<string> jiao;
    set<string> bing;
    for (auto it = s2.begin(); it != s2.end(); it++)
    {
        bing.insert(*it);
        if (s1.find(*it) != s1.end())
        {
            jiao.insert(*it);
        }
    }
    for (auto it = s1.begin(); it != s1.end(); it++)
    {
        bing.insert(*it);
    }
    cout << jiao.size() << endl << bing.size();
    return 0;
}