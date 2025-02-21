#include<bits/stdc++.h>
using namespace std;
const int MOD=1e9+7;
typedef long long ll;
int main(){
    int m,n;
    cin>>m>>n;
    vector<vector<ll>> dp(m+1,vector<ll>(n+1,0));
    dp[1][1]=1;
    for(int i=1;i<=m;i++){
        for(int j=1;j<=n;j++){
            if(i==1 and j==1) continue;
            if(i>1){
                dp[i][j]+=dp[i-1][j];
                dp[i][j]%=MOD;
            }
            if(j>1){
                dp[i][j]+=dp[i][j-1];
                dp[i][j]%=MOD;
            }
        }
    }
    cout<<dp[m][n];
}