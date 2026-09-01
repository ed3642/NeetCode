// https://leetcode.com/problems/map-of-highest-peak

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    using pii = pair<int, int>;
    using vvb = vector<vector<bool>>;

    int n;
    int m;

    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {

        n = isWater.size();
        m = isWater[0].size();
        vector<pii> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        vector<vector<bool>> visited(n, vector<bool>(m, false)); 
        deque<pii> q;
        int depth = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (isWater[i][j] == 1) {
                    q.push_back({i, j});
                    visited[i][j] = true;
                }
            }
        }

        while (!q.empty()) {
            int sz = q.size();

            for (int _ = 0; _ < sz; _++) {
                auto [i, j] = q.front();
                q.pop_front();

                isWater[i][j] = depth;

                for (auto [di, dj] : directions) {
                    int ni = i+di;
                    int nj = j+dj;
                    if (isIn(ni, nj) && !visited[ni][nj]) {
                        q.push_back({ni, nj});
                        visited[ni][nj] = true;
                    }
                }
            }
            depth++;
        }

        return isWater;
    }

    bool isIn(int i, int j) {
        return 0 <= i && i < n && 0 <= j && j < m;
    }
};