#include <bits/stdc++.h>
using namespace std;

class Solution {
public:

    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<double> st;
        vector<pair<int, int>> cars(n);
        for (int i = 0; i < n; i++) {
            cars[i] = {position[i], i};
        }
        sort(cars.begin(), cars.end());
        
        st.push_back(cars[n-1].second);
        for (int i = n-2; i > -1; i--) {
            int carFI = st.back(); // car in front
            int carI = cars[i].second;
            double arrivalTCurr = (double) (target-position[carI])/speed[carI];
            double arrivalTFront = (double) (target-position[carFI])/speed[carFI];
            if (arrivalTCurr > arrivalTFront) { // cars never collide
                st.push_back(carI);
            }
        }

        return st.size();
    }
};