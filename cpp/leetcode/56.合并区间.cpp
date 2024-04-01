/*
 * @lc app=leetcode.cn id=56 lang=cpp
 *
 * [56] 合并区间
 */

/**
 * @author: Zeyu Zuo
 * @date: 2024-04-01 22:02:23
 */
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

// @lc code=start
class Solution {
public:
    static bool compare(vector<int> a, vector<int> b){
        return a[0] < b[0];
    }

    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), compare);
        vector<vector<int>> result;
        result.push_back(intervals[0]);

        for (int i = 1; i < intervals.size(); i++)
            if (intervals[i][0] <= result.back()[1])
                result.back()[1] = max(result.back()[1], intervals[i][1]);
            else
                result.push_back(intervals[i]);

        return result;
    }
};
// @lc code=end

