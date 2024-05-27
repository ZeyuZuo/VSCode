/**
 * @author: Zeyu Zuo
 * @date: 2024-05-16 17:16:11
 */
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

// 9 7 7 7 5 5

class Solution {
public:

    long long numberOfWeeks(vector<int>& milestones) {
        LL longest = *max_element(milestones.begin(), milestones.end());
        LL rest = accumulate(milestones.begin(), milestones.end(), 0LL) - longest;
        return longest > rest + 1 ? 2 * rest + 1 : longest + rest;
    }
};