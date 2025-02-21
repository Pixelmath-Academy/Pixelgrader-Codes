#include<bits/stdc++.h>
using namespace std;
const int N=2e4+5;
int a[N];
bool knows[N];

void spread_info(int k){
	if(knows[k]) return;
	knows[k]=true;
	spread_info(a[k]);
}
int main(){
	int n,k;
	cin>>n>>k;
	for(int i=1;i<=n;i++){
		cin>>a[i];
		knows[i]=false;
	}
	spread_info(k);
	int cnt=0;
	for(int i=1;i<=n;i++){
		if(!knows[i]) cnt++;
	}
	cout<<cnt;
}