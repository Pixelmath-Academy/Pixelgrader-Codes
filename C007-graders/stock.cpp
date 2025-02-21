#include<bits/stdc++.h>
using namespace std;
int cal(vector<int>& prices){
    int n=prices.size();
    if(n==0) return 0;
    vector<int> profit1(n,0);
    vector<int> profit2(n,0);
    int min_price=prices[0];
    for(int i=1;i<n;i++){
        min_price=min(min_price,prices[i]);
        profit1[i]=max(profit1[i-1],prices[i]-min_price);
    }
    int max_price=prices[n-1];
    for(int i=n-2;i>=0;i--){
        max_price=max(max_price,prices[i]);
        profit2[i]=max(profit2[i+1],max_price-prices[i]);
    }
    int max_profit=0;
    for(int i=0;i<n;i++){
        max_profit=max(max_profit,profit1[i]+profit2[i]);
    }
    return max_profit;
}
int main(){
    int n;
    cin>>n;
    vector<int> prices(n);
    for(int i=0;i<n;i++){
        cin>>prices[i];
    }
    cout<<cal(prices);
    return 0;

}