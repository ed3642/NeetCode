#include <bits/stdc++.h>
using namespace std;

class SparseTable {
public:
    // query indempotent operation on range in O(1)

    SparseTable(const vector<int>& arr) {
        int n = (int)arr.size();
        int k = n > 0 ? (int)floor(log2(n)) + 1 : 1;

        // table[j][i] = result of _merge over arr[i : i + 2^j]
        table.assign(k, vector<int>(n, _default()));
        if (n > 0) table[0] = arr;

        for (int j = 1; j < k; j++) {
            for (int i = 0; i <= n - (1 << j); i++) {
                table[j][i] = _merge(
                    table[j-1][i],
                    table[j-1][i + (1 << (j-1))]
                );
            }
        }

        log_table.assign(n + 1, 0);
        for (int i = 2; i <= n; i++) {
            log_table[i] = log_table[i / 2] + 1;
        }
    }

    int query(int l, int r) {
        // O(1) — only works because _merge is idempotent (two blocks can safely overlap)
        // if your operation is NOT idempotent, this overlap produces wrong answers
        int k = log_table[r - l + 1];
        return _merge(
            table[k][l],
            table[k][r - (1 << k) + 1]
        );
    }

private:
    vector<vector<int>> table;
    vector<int> log_table;

    int _default() {
        // identity/neutral value for your operation:
        // min:          return numeric_limits<int>::max();
        // max:          return numeric_limits<int>::min();
        // gcd:          return 0;
        // bitwise AND:  return (1 << 31) - 1    (all 1s)
        // bitwise OR:   return 0;
        return numeric_limits<int>::max();
    }

    int _merge(int a, int b) {
        // MUST be idempotent: _merge(x, x) == x (overlap between blocks is safe)
        // min:         return min(a, b);    idempotent ✓
        // max:         return max(a, b);    idempotent ✓
        // gcd:         return gcd(a, b);    idempotent ✓ (needs <numeric>)
        // bitwise AND: return a & b;              idempotent ✓
        // bitwise OR:  return a | b;               idempotent ✓
        // sum:         return a + b;               idempotent ✗ — use segment tree instead
        return min(a, b);
    }
};