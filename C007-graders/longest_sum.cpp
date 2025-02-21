#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    vector<int> vec(n);
    for(int i=0;i<n;i++){
        cin>>vec[i];
    }
    vector<int> dp(n);
    int max_sum=0;
    for(int i=0;i<n;i++){
        dp[i]=vec[i];
        for(int j=0;j<i;j++){
            if(vec[i]>vec[j]){
                dp[i]=max(dp[i],dp[j]+vec[i]);
            }
        }
        max_sum=max(max_sum,dp[i]);
    }
    cout<<max_sum;
    return 0;
}