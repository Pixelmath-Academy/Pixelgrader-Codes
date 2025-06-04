#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; 
    if (!(cin >> n)) return 0;
    vector<int> a(n);
    for (int &x : a) cin >> x;

    unordered_set<int> sums;
    for (int mask = 0; mask < (1 << n); ++mask) {
        int s = 0;
        for (int i = 0; i < n; ++i)
            if (mask & (1 << i)) s += a[i];
        sums.insert(s);
    }
    cout << sums.size() << '\n';
    return 0;
}
