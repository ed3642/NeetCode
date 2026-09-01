// https://leetcode.com/problems/range-sum-query-mutable

#include <bits/stdc++.h>
using namespace std;

class NumArray {
public:

    vector<int>& arr;
    vector<int> t;
    int n;

    NumArray(vector<int>& nums) : arr(nums) { // need to bind arr to nums at construction time
        n = nums.size();
        t = vector<int>(n+1, 0);

        // initialize tree in O(n)
        for (int i = 1; i <= n; i++) {
            t[i] = nums[i-1];
        }
        for (int i = 1; i <= n; i++) {
            int j = i+(i & -i);
            if (j <= n)
                t[j] += t[i];
        }
    }
    
    void update(int index, int val) {
        int dx = val-arr[index];
        arr[index] = val;
        treeUpdate(index+1, dx);
    }
    
    int sumRange(int left, int right) {
        return query(right+1) - query(left);
    }

    int query(int i) {
        int sum = 0;
        while (i > 0) {
            sum += t[i];
            i -= i & -i;
        }
        return sum;
    }

    void treeUpdate(int i, int dx) {
        while (i <= n) {
            t[i] += dx;
            i += i & -i;
        }
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */