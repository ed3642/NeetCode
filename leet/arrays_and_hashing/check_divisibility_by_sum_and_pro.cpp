// https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

class Solution {
public:
    bool checkDivisibility(int n) {
        int s = 0;
        int p = 1;
        int d = 0;
        int num = n;

        while (num > 0) {
            d = num % 10;
            s += d;
            p *= d;
            num /= 10;
        }

        return n % (s+p) == 0;
    }
};