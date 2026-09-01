// https://leetcode.com/problems/combination-sum

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int>* candPtr;
    vector<vector<int>> combinations;
    vector<int> builder;
    int n;
    int target;

    vector<vector<int>> combinationSum(vector<int>& candidates, int t) {
        candPtr = &candidates;
        n = candidates.size();
        target = t;

        sort(candidates.begin(), candidates.end());
        
        bt(0, 0);
        return combinations;
    }

    void bt(int start, int sum) {
        if (start == n)
            return;
        if (sum == target)
            combinations.push_back(builder);
        
        vector<int>& candidates = *candPtr;
        for (int i = start; i < n; i++) {
            int c = candidates[i];
            if (c+sum <= target) {
                sum += c;
                builder.push_back(c);
                bt(i, sum);
                sum -= c;
                builder.pop_back();
            }
        }
    }
};