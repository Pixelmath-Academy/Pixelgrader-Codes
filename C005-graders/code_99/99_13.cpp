#include <iostream>
#include <vector>
using namespace std;

int main() {
    int m;
    cin >> m;

    if (m == 0) {
        cout << 1 << endl;
        return 0;
    }
    if (m == 1) {
        cout << 2 << endl; // "0", "1"
        return 0;
    }

    long long dp[m + 1][2][2] = {};
    dp[1][0][0] = 1;
    dp[1][1][0] = 1; 

    for (int i = 2; i <= m; i++) {
        for (int a = 0; a <= 1; a++) {
            for (int b = 0; b <= 1; b++) {
                long long val = dp[i - 1][a][b];
                dp[i][b][0] += val;
                if (!(a == 1 && b == 1)) {
                    dp[i][b][1] += val;
                }
            }
        }
    }

    long long total = 0;
    for (int a = 0; a <= 1; a++)
        for (int b = 0; b <= 1; b++)
            total += dp[m][a][b];

    cout << total << endl;
}
