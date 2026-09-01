#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // O(n + m)
    int kmp(const string& elems, const string& lookingFor) {
        return matcher(elems, lookingFor);
    }

private:
    vector<int> get_lsp(const string& pattern) {
        int N = (int)pattern.size();
        vector<int> lsp(N, 0);
        int mtc = 0;

        for (int i = 1; i < N; i++) {
            while (mtc > 0 && pattern[mtc] != pattern[i]) {
                mtc = lsp[mtc-1];
            }
            if (pattern[mtc] == pattern[i]) {
                mtc++;
            }
            lsp[i] = mtc;
        }

        return lsp;
    }

    int matcher(const string& s, const string& pattern) {
        int N = (int)s.size();
        int M = (int)pattern.size();
        vector<int> lsp = get_lsp(pattern);
        int mtc = 0;

        for (int i = 0; i < N; i++) {
            while (mtc > 0 && s[i] != pattern[mtc]) {
                mtc = lsp[mtc-1];
            }
            if (s[i] == pattern[mtc]) {
                mtc++;
            }
            if (mtc == M) {
                return i-M+1;
            }
        }

        return -1;
    }
};