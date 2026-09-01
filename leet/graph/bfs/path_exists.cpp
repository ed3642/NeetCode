// https://leetcode.com/problems/find-if-path-exists-in-graph

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> al;
    vector<bool> visited;
    int dest;

    void dfs(int u) {
        if (visited[dest]) return;
        visited[u] = true;

        for (int v : al[u]) {
            if (!visited[v]) {
                dfs(v);
            }
        }
    }

    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        if (source == destination) return true;

        al.assign(n, {});
        visited.assign(n, false);
        dest = destination;

        for (auto &e : edges) {
            int u = e[0];
            int v = e[1];

            al[u].push_back(v);
            al[v].push_back(u);
        }

        dfs(source);

        return visited[dest];
    }
};

class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {

        if (source == destination) return true;

        vector<vector<int>> al(n);
        vector<bool> visited(n, false);
        deque<int> q = {source};

        for (auto &e : edges) {
            int u = e[0];
            int v = e[1];

            al[u].push_back(v);
            al[v].push_back(u);
        }

        visited[source] = true;
        while (!q.empty()) {
            
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                int u = q.front();
                q.pop_front();

                for (int v : al[u]) {
                    if (!visited[v]) {
                        if (v == destination) return true;
                        q.push_back(v);
                        visited[v] = true;
                    }
                }
            }
        }
        return false;
    }
};