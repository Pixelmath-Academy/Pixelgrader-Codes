#include<bits/stdc++.h>
using namespace std;
const int MOD=1e9+7;
int main(){
    int n,m;
    cin>>n>>m;
    vector<int> dp(n+1,0);
    dp[0]=1;
    long long window_sum=0;
    for(int i=1;i<=n;i++){
        window_sum=(window_sum+dp[i-1])%MOD;
        if(i-m-1>=0){
            window_sum=(window_sum-dp[i-m-1]+MOD)%MOD;
        }
        dp[i]=window_sum;
    }
    cout<<dp[n];
    return 0;
}