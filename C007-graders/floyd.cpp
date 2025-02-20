#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,m;
    cin>>n>>m;
    const int INF=1e9;
    vector<vector<int>> dist(n,vector<int>(n,INF));
    for(int i=0;i<n;i++) dist[i][i]=0;
    for(int i=0;i<m;i++){
        int a,b,c;
        cin>>a>>b>>c;
        dist[a][b]=c;
    }
    for(int k=0;k<n;k++){
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(dist[i][k]<INF&&dist[k][j]<INF){
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j]);
                }
            }
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(dist[i][j]==INF) cout<<"-1 ";
            else cout<<dist[i][j]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}