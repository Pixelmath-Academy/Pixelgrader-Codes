#include <iostream>
using namespace std;

const int MAX = 105;
char grid[MAX][MAX];
bool visited[MAX][MAX];
int R, C, sr, sc, cc = 0;

int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};

void dfs(int x, int y) {
    if (x < 1 || x > R || y < 1 || y > C) return;
    if (grid[x][y] == '#' || visited[x][y]) return;
    visited[x][y] = true;
    cc++;
    for (int d = 0; d < 4; d++) {
        dfs(x +dx[d], y + dy[d]);
    }
}

int main() {
    cin >>R>>C>>sr>>sc;
    for (int i = 1; i<=R; i++)
        for (int j = 1; j<= C; j++)
            cin >> grid[i][j];

    dfs(sr,sc);
    cout << cc << '\n';
    return 0;
}
