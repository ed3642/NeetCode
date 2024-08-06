public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> seen = [];

        for (int i = 0; i < nums.Length; i++) {
            int need = target - nums[i];
            if (seen.TryGetValue(need, out int need_i)) {
                return [need_i, i];
            }
            seen[nums[i]] = i;
        }

        return [];
    }
}