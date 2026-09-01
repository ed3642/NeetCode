// https://leetcode.com/problems/two-sum/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> seen;

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            int need = target-x;
            if (seen.count(need)) {
                return {i, seen[need]};
            }
            seen[x] = i;
        }

        return {-1, -1}; // shouldnt happen by problem statement
    }
};