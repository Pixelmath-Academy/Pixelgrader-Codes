#include <iostream>
#include <queue>
using namespace std;

const int MAX = 105;
char grid[MAX][MAX];
bool visited[MAX][MAX];
int R, C;

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

bool bfs(int sx, int sy) {
    queue<pair<int, int>> q;
    q.push({sx, sy});
    visited[sx][sy] = true;

    while (!q.empty()) {
        pair<int, int> p = q.front(); q.pop();
        int x = p.first, y = p.second;

        for (int d = 0; d < 4; ++d) {
            int nx = x + dx[d], ny = y + dy[d];
            if (nx < 1 || nx > R || ny < 1 || ny > C) continue;
            if (visited[nx][ny] || grid[nx][ny] == '#') continue;
            if (grid[nx][ny] == '!') return true;

            visited[nx][ny] = true;
            q.push(make_pair(nx, ny));
        }
    }
    return false;
}


int main() {
    cin >> R >> C;
    for (int i = 1; i <= R; ++i)
        for (int j = 1; j <= C; ++j)
            cin >> grid[i][j];

    for (int i = 1; i <= R; ++i)
        for (int j = 1; j <= C; ++j)
            if (grid[i][j] == '@' && !visited[i][j])
                if (bfs(i, j)) {
                    cout << "YES\n";
                    return 0;
                }

    cout << "NO\n";
    return 0;
}
