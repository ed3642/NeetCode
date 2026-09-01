#include <bits/stdc++.h>
using namespace std;

// Note: Python's self.arr[i][0] implies elements are pair-like (tuple/list).
// Translated using pair<int, int>; swap the type if your elements differ.
class QuickSelect {
public:
    // get the kth elem from the arr if it was sorted in avg(n) and O(n^2)
    QuickSelect(vector<pair<int, int>>& arr, int k)
        : arr(arr), k(k) {
        quickselect(0, (int)arr.size() - 1); // kth elem is now in right place
    }

private:
    vector<pair<int, int>>& arr;
    int k;

    int partition(int l, int r) {
        int pivot_i = l + rand() % (r - l + 1);
        swap(arr[pivot_i], arr[r]);
        int pivot = arr[r].first;
        int placer_i = l;

        for (int i = l; i < r; i++) {
            if (arr[i].first <= pivot) {
                swap(arr[placer_i], arr[i]);
                placer_i += 1;
            }
        }

        swap(arr[placer_i], arr[r]);

        return placer_i;
    }

    void quickselect(int l, int r) {
        if (l >= r) {
            return;
        }

        int pivot_i = partition(l, r);
        if (pivot_i == k) {
            return;
        } else if (pivot_i < k) {
            quickselect(pivot_i + 1, r);
        } else {
            quickselect(l, pivot_i - 1);
        }
    }
};