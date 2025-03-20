#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<vector<long long> > matrix(n + 1, vector<long long>(n + 1, 0));
    vector<vector<long long> > ps(n + 1, vector<long long>(n + 1, 0));

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            cin >> matrix[i][j];
        }
    }

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + matrix[i][j];
        }
    }

    int r1, c1, r2, c2;
    cin >> r1 >> c1 >> r2 >> c2;

    if(r1 > r2) swap(r1, r2);
    if(c1 > c2) swap(c1, c2);

    long long result = ps[r2][c2]
                       - ps[r1 - 1][c2]
                       - ps[r2][c1 - 1]
                       + ps[r1 - 1][c1 - 1];

    cout << result << "\n";
    return 0;
}