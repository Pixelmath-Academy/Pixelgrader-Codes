#include <iostream>
#include <vector>
using namespace std;

int main() {
    int m, k;
    cin >> m >> k;

    vector<vector<long long>> dp(m + 1, vector<long long>(k + 2, 0));
    dp[0][0] = 1;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j <= k; j++) {
            dp[i + 1][0] += dp[i][j];
            if (j < k) {
                dp[i + 1][j + 1] += dp[i][j];
            }
        }
    }

    long long result = 0;
    for (int j = 0; j <= k; j++) {
        result += dp[m][j];
    }
    cout << result << endl;
    return 0;
}
