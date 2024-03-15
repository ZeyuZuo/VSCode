#define _CRT_SECURE_NO_WARNINGS 1
#include<iostream>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

class Solution {
public:
   bool compare(vector<int> a, vector<int> b)
   {
       return a[0] < b[0];
   }

   vector<vector<int>> merge(vector<vector<int>>& intervals) {
       sort(intervals.begin(), intervals.end(), compare);
       vector<vector<int>> result;
       result.push_back(intervals[0]);

       for (int i = 1; i < intervals.size(); i++)
       {
           if (intervals[i][0] < result.back()[1])
           {
               result.back()[1] = max(result.back()[1], intervals[i][1]);
           }
           else
           {
               result.push_back(intervals[i]);
           }
       }

       return result;
   }

};