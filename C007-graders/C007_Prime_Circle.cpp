#include<bits/stdc++.h>
using namespace std;
int n,total=0;
vector<int> circle;
vector<bool> used;
bool is_prime(int num){
    if(num<2) return false;
    for(int i=2;i<=sqrt(num);i++){
        if(num%i==0) return false;
    }
    return true;
}
void cal(int pos){
    if(pos==n and is_prime(circle[pos-1]+circle[0])){
        total++;
        return;
    }
    for(int i=2;i<=n;i++){
        if(!used[i] and is_prime(circle[pos-1]+i)){
            circle[pos]=i;
            used[i]=true;
            cal(pos+1);
            used[i]=false;
        }
    }
}
int main(){
    cin>>n;
    circle.resize(n);
    used.resize(n+1);
    circle[0]=1;
    used[1]=true;
    cal(1);
    cout<<total;
    return 0;
}