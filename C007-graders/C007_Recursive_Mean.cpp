#include<bits/stdc++.h>
using namespace std;
vector<int> v;
double findMean(int n){
    if(n==1){
        return v[0];
    }
    return (v[n-1]+(n-1)*findMean(n-1))/n;
}
int main(){
    int n;
    cin>>n;
    v.resize(n);
    for(int i=0;i<n;i++){
        cin>>v[i];
    }
    cout<<fixed<<setprecision(6)<<findMean(n)<<"\n";
    int new_element;
    cin>>new_element;
    v.push_back(new_element);
    cout<<fixed<<setprecision(6)<<findMean(n+1)<<"\n";

    return 0;
}