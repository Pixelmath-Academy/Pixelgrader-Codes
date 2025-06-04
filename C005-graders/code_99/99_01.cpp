#include <iostream>
#include <algorithm>
using namespace std;

int n,a,b;
int grid[11][11];
int mm=0;

void brute(int x, int y, int sum) {
    if (x > a || y > b) return;
    sum += grid[x][y];
    if (x == a && y == b) {
        mm = max(mm, sum);
        return;
    }
    brute(x+1, y, sum);
    brute(x,y+1,sum); 
}

int main() {
    cin >> n >> a >> b;
    if (a > n|| b > n) {
        cout << 0 << endl;
        return 0;
    }

    for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) cin >> grid[i][j];

    brute(1, 1, 0);
    cout << mm << endl;
    return 0;
}
