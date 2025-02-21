#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pii;
vector<vector<pii>> adj;
vector<int> dist;
void dijkstra(int s, int n){
    priority_queue<pii,vector<pii>,greater<pii>> pq;
    dist.assign(n+1,INT_MAX);
    dist[s]=0;
    pq.push({0,s});
    while(!pq.empty()){
        int d=pq.top().first,u=pq.top().second;
        pq.pop();
        if(d>dist[u]) continue;
        for(auto edge:adj[u]){
            int v=edge.first,w=edge.second;
            if(dist[u]+w<dist[v]){
                dist[v]=dist[u]+w;
                pq.push({dist[v],v});
            }
        }
    }
}
int main(){
    int n,m,s,t;
    cin>>n>>m>>s>>t;
    adj.resize(n+1);
    for(int i=0;i<m;i++){
        int u,v,w;
        cin>>u>>v>>w;
        adj[u].push_back({v,w});
        //adj[v].push_back({u,w});
    }
    dijkstra(s,n);
    if(dist[t]==INT_MAX){
        cout<<"-1";
    }
    else{
        cout<<dist[t];
    }
    return 0;
}
