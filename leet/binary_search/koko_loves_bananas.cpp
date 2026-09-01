#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        function<bool(int)> works = [&](int sp) {
            int t = 0;
            for (int num : piles) {
                t += (num+sp-1)/sp;
                if (t > h) return false;
            }
            return true;
        };

        int n = piles.size();
        int l = 1;
        int r = *max_element(piles.begin(), piles.end());

        while (l < r) {
            int m = l+(r-l)/2;

            if (works(m)) {
                r = m;
            } else {
                l = m+1;
            }
        }

        return l;
    }
};

class Solution {
public:
    using vi = vector<int>;
    using ll = long long;
    int limit;

    int minEatingSpeed(vector<int>& piles, int h) {
        limit = h;
        ll sum = 0;
        for (int x : piles) sum += x;

        int n = piles.size();
        int l = 1;
        ll r = sum*n;

        while (l < r) {
            ll m = l+(r-l)/2;

            if (works(m, piles)) {
                r = m;
            } else {
                l = m+1;
            }
        }

        return l;
    }

    bool works(ll sp, vi& piles) {
        int t = 0;
        for (int num : piles) {
            t += (num+sp-1)/sp;
            if (t > limit) return false;
        }
        return true;
    }
};