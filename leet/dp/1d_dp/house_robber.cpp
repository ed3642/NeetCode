// https://leetcode.com/problems/house-robber

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    using vi = vector<int>; 
    inline int max(vi vec) { return *max_element(vec.begin(), vec.end()); }

    int rob(vector<int>& dp) {
        int n = dp.size();
        if (n == 1) return dp[0];
        dp[1] = max({dp[0], dp[1]});

        for (int i = 2; i < n; i++) {
            dp[i] = max({dp[i]+dp[i-2], dp[i-1]});
        }

        return dp[n-1];
    }
};