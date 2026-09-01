// https://leetcode.com/problems/cheapest-flights-within-k-stops

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    using vi = vector<int>;
    using vvi = vector<vector<int>>; 
    using tiii = tuple<int, int, int>;
    using pii = pair<int, int>;
    const int INF = INT32_MAX;

    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // SPFA with optimizations, but need to keep track of <dist, flights>
        // optimization 1: put promising candidates at the front
        // optimization 2: dont go deeper than dst
        // optimization 3: prune candidates worse than best

        vector<vector<pii>> g(n);
        vvi distance(n, vi(k+2, INF)); // distance[node][stops]
        deque<tiii> q = {{0, 0, src}}; // distance, stops, node

        for (auto &f : flights) {
            int u = f[0];
            int v = f[1];
            int w = f[2];
            g[u].push_back({v, w});
        }

        distance[src][0] = 0;
        int res = INF;

        while (!q.empty()) {
            auto [d, stops, u] = q.front();
            q.pop_front();

            if (u == dst) { // op 2
                res = min(res, d);
                continue;
            } 

            for (auto &[v, w] : g[u]) {
                int candD = d+w;
                if (candD >= res) continue; // op 3
                if (stops-1 < k && candD < distance[v][stops+1]) {
                    distance[v][stops+1] = candD;
                    if (q.size() > 0 && candD < distance[get<2>(q.front())][stops+1]) // op 1
                        q.push_front({candD, stops+1, v});
                     else 
                        q.push_back({candD, stops+1, v});
                }
            }  
        }
        return res != INF ? res : -1;
    }
};

class Solution {
public:
    using T3 = tuple<int, int, int>;
    using P = pair<int, int>;
    const int INF = INT32_MAX;

    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // SPFA

        vector<vector<P>> g(n);
        vector<int> distance(n, INF);
        deque<T3> q = {{0, 0, src}}; // distance, stops, node

        for (auto &f : flights) {
            int u = f[0];
            int v = f[1];
            int w = f[2];
            g[u].push_back({v, w});
        }

        distance[src] = 0;

        while (!q.empty()) {
            auto [d, stops, u] = q.front();
            q.pop_front();

            for (auto &[v, w] : g[u]) {
                int candD = d+w;
                if (stops-1 < k && candD <= distance[v]) {
                    q.push_back({candD, stops+1, v});
                    distance[v] = candD;
                }
            }  
        }
        int res = distance[dst];
        return res != INF ? res : -1;
    }
};

class Solution {
public:
    using T3 = tuple<int, int, int>;
    using P = pair<int, int>;
    const int INF = INT32_MAX;

    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // modified djikstra 

        vector<vector<P>> g(n);
        priority_queue<T3, vector<T3>, greater<T3>> pq; // min pq
        vector<int> distance(n, INF);
        vector<int> nodeStops(n, INF);

        for (auto &f : flights) {
            int u = f[0];
            int v = f[1];
            int w = f[2];
            g[u].push_back({v, w});
        }

        pq.push({0, 0, src}); // distances, stops, node
        distance[src] = 0;

        while (!pq.empty()) {
            auto [d, stops, u] = pq.top();
            pq.pop();
            
            if (u == dst) {
                return d;
            }
            if (stops > nodeStops[u]) continue; // prune paths that get here with more flights
            nodeStops[u] = stops;

            for (auto &[v, w] : g[u]) {
                int candD = d+w;
                if (stops-1 < k) {
                    pq.push({candD, stops+1, v});
                    distance[v] = candD;
                }
            }
        }
        return -1;
    }
};
