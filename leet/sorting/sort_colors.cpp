#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        // 2 0 1
        // 1 0 2
        // classic dutch flag
        int n = nums.size();
        int l = 0;
        int r = n-1;
        int i = 0;

        for (int i = 0; i <= r;) {
            if (nums[i] == 0) {
                swap(nums[i], nums[l]);
                l++;
                i++;
            } else if (nums[i] == 2) {
                swap(nums[i], nums[r]);
                r--;
            } else {
                i++;
            }
        }
    }
};