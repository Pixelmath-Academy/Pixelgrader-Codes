#include <vector>
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;                cin >> n;
    long long x, best, cur;
    cin >> x;             best = cur = x; 
    for (int i = 2; i <= n; ++i) {
        cin >> x;
        cur  = max(x, cur + x);
        best = max(best, cur);
    }
    cout << best << '\n';
    return 0;
}
