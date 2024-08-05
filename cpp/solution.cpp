#include <vector>
#include <unordered_map>

using namespace std;
// https://leetcode.com/problems/two-sum/

class Solution {
public:
    // my first c++ leetcode
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen = {
            {nums[0], 0}
        };
        
        for (int i = 1; i < nums.size(); i++) {
            int need = target - nums[i];
            if (seen.find(need) != seen.end()) {
                return {seen[need], i};
            }
            seen[nums[i]] = i;
        }

        return {};
    }
};