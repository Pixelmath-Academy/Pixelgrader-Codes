#include<bits/stdc++.h>
using namespace std;

void findPaths(vector<vector<int>>& graph, int current, int destination, vector<int>& path, vector<vector<int>>& allPaths, vector<bool>& visited) {
    visited[current] = true;
    path.push_back(current);

    if(current == destination) {
        allPaths.push_back(path);
    } else {
        for(int neighbor : graph[current]) {
            if(!visited[neighbor]) {
                findPaths(graph, neighbor, destination, path, allPaths, visited);
            }
        }
    }

    path.pop_back();
    visited[current] = false;
}

int main() {
    int n,m;
    cin>>n>>m;
    vector<vector<int>> graph(n);
    for(int i=0;i<m;i++){
        int u,v;
        cin>>u>>v;
        graph[u].push_back(v);
    }
    for(auto &x:graph){
        sort(x.begin(),x.end());
    }
    vector<vector<int>> allPaths;
    vector<int> path;
    vector<bool> visited(n,false);

    findPaths(graph,0,n-1,path,allPaths,visited);
    sort(allPaths.begin(),allPaths.end());
    if(!allPaths.empty()){
        for(auto &p:allPaths){
            for(int i=0;i<p.size();i++){
                if(i>0) cout<<" ";
                cout<<p[i];
            }
            cout<<"\n";
        }
    } else {
        cout<<"No path found from 0 to "<<n-1<<"\n";
    }
    return 0;
}