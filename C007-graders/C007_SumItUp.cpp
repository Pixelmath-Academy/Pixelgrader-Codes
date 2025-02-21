#include<bits/stdc++.h>
using namespace std;
vector<int> vec;
int k,cnt;
void cal(int idx,int cur){
	if(cur==k){
		cnt++;
		return;
	}
	if(idx>=vec.size()||cur>k){
		return;
	}
	cal(idx+1,cur+vec[idx]);
	cal(idx+1,cur);
}
int main(){
	int n;
	cin>>k>>n;
	for(int i=0;i<n;i++){
		int x;
		cin>>x;
		vec.push_back(x);
	}
	cnt=0;
	cal(0,0);
	cout<<cnt;
	return 0;
}
