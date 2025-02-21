#include<bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;
using namespace std;
int main(){
    int n;
    cin>>n;
    vector<long long> dp(max(n,5)+1,0);
    dp[0]=dp[1]=dp[2]=dp[3]=1;
    dp[4]=2;
    for(int i=5;i<=n;i++){
        dp[i]=(dp[i-1]+dp[i-4])%MOD;
    }
    cout<<dp[n];
}
