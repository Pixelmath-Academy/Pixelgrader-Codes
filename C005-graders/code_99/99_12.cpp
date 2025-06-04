#include <iostream>
#include <vector>
using namespace std;

int main() {
    int k;
    cin >> k;
    if (k == 0) {
        cout << 0 << endl;
        return 0;
    }
    vector<long long> dp(k + 1);
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i <= k; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    cout << dp[k] << endl;
    return 0;
}
