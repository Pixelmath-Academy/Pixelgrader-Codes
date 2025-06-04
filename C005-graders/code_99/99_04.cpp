#include <iostream>
#include <cmath>
using namespace std;

int n,ans = 0;
int col[13];

bool isSafe(int row, int c) {
    for (int i = 1; i < row; ++i) {
        if (col[i] == c || abs(col[i] - c) == abs(i - row))
            return false;
    }
    return true;
}

void recur(int row) {
    if (row > n) {
        ans++;
        return;
    }
    for (int c = 1; c <= n; ++c) {
        if (isSafe(row, c)) {
            col[row] = c;
            recur(row+1);
        }
    }
}

int main() {
    cin >> n;
    recur(1);
    cout<<ans<< '\n';
    return 0;
}
