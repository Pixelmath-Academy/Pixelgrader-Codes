#include<bits/stdc++.h>
using namespace std;
int n,k,ways;
vector<int> vec;
void cal(int start,int cnt){
    if(cnt==k){
        ways++;
        return;
    }
    for(int i=start;i<n;i++){
        cal(i+1,cnt+1);
    }
}
int main(){
    cin>>n>>k;
    if(k>n){
        cout<<0;
        return 0;
    }
    ways=0;
    cal(0,0);
    cout<<ways;
    return 0;
}