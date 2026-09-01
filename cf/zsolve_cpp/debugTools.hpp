#include <vector>
#include <string>

using namespace std;

template <class T>
void printVec(const vector<T>& v, bool showIndex = false, string sep = " ") {
    if (!showIndex) {
        for (int i = 0; i < (int) v.size(); i++) {
            cout << v[i];
            if (i + 1 < (int) v.size()) cout << sep;
        }
        cout << '\n';
        return;
    }

    for (int i = 0; i < (int) v.size(); i++) {
        cout << i << " " << v[i] << '\n';
    }
}
