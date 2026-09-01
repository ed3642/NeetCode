// https://leetcode.com/problems/edit-distance

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string w1;
    string w2;
    int n;
    int m;
    vector<vector<int>> memo;

    int minDistance(string word1, string word2) {
        w1 = word1;
        w2 = word2;
        n = w1.size();
        m = w2.size();
        memo.assign(n+1, vector<int>(m+1, -1));

        return dp(0, 0);
    }

    // min edit distance from w1 to w2
    int dp(int i, int j) {
        if (memo[i][j] != -1) 
            return memo[i][j];
            
        if (i >= n) 
            return m-j;
        if (j >= m)
            return n-i;
        
        if (w1[i] == w2[j]) {
            int res = dp(i+1, j+1);
            memo[i][j] = res;
            return res;
        }
        int res = min({
            dp(i, j+1),
            dp(i+1, j),
            dp(i+1, j+1)
        })+1;
        memo[i][j] = res;
        return res;
    }
};