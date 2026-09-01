// https://leetcode.com/problems/longest-increasing-subsequence/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {

        vector<int> order;

        for (int i = 0; i < nums.size(); i++) {
            int insertI = lower_bound(order.begin(), order.end(), nums[i])-order.begin();
            if (insertI >= order.size()) 
                order.push_back(nums[i]);
            else {
                order[insertI] = nums[i];
            }
        }

        return order.size();
    }
};