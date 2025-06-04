
 #include <iostream>
 #include <vector>
 #include <queue>
 
 using namespace std;
 
 const int INF = 1e9;
 const int DX[4] = {0, 1, 0, -1};
 const int DY[4] = {1, 0, -1, 0};
 
 int main() {
     ios::sync_with_stdio(false);
     cin.tie(nullptr);
 
     int R, C;
     if (!(cin >> R >> C)) return 0;
 
     vector<string> grid(R);
     for (int i = 0; i < R; ++i) cin >> grid[i];
 
     vector<vector<int>> dist(R, vector<int>(C, -1));     
     queue<pair<int, int>> q;                           
     vector<pair<int, int>> bases;                      
 
     for (int i = 0; i < R; ++i)
         for (int j = 0; j < C; ++j) {
             if (grid[i][j] == '@') {
                 q.emplace(i, j);
                 dist[i][j] = 0; 
             }
             if (grid[i][j] == '!') bases.emplace_back(i, j);
         }
 
     while (!q.empty()) {
         int x = q.front().first;
         int y = q.front().second;
         q.pop();
 
         for (int d = 0; d < 4; ++d) {
             int nx = x + DX[d], ny = y + DY[d];
             if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;    
             if (grid[nx][ny] == '#' || dist[nx][ny] != -1) continue;  
             dist[nx][ny] = dist[x][y] + 1;
             q.emplace(nx, ny);
         }
     }
 
     for (auto p : bases) {
         int t = dist[p.first][p.second];
         cout << t << '\n';   
     }
     return 0;
 }
 