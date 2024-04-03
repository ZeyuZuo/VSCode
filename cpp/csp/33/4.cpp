/**
 * @author: Zeyu Zuo
 * @date: 2024-04-03 19:36:19
 */
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
int n, m, c;
map<int, int> maps;

void check(int num)
{
    int preNum = -1;
    int proNum = -1;
    auto it = maps.find(num);
    if (it == maps.end())
        return;
    if (it->second >= 5)
    {
        if (it == maps.end())
            exit(0);

        if (it != maps.begin())
        {
            auto pre = --it;
            pre->second++;
            preNum = pre->first;
            it++;
        }
        auto pro = ++it;
        if (pro != maps.end())
        {
            pro->second++;
            proNum = pro->first;
        }
        maps.erase(num);
    }
    if (preNum != -1)
        check(preNum);
    if (proNum != -1)
        check(proNum);
}

void fun(int p)
{
    auto it = maps.find(p);
    it->second++;
    check(p);
}

int main()
{
    cin >> c >> m >> n;
    int p;
    int pos, num;
    for (int i = 0; i < m; i++)
    {
        scanf("%d%d", &pos, &num);
        maps[pos] = num;
    }
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &p);
        fun(p);
        cout << maps.size() << endl;
    }
    return 0;
}