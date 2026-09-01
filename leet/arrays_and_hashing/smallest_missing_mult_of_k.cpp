// https://leetcode.com/problems/smallest-missing-multiple-of-k

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        unordered_set<int> a;

        for (int x : nums) {
            if (x % k == 0) 
                a.insert(x);
        }

        int x = k;
        while (true) {
            if (x % k == 0 && !a.count(x))
                return x;
            x += k;
        }
        return -1;
    }
};