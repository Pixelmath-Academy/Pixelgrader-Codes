#include<bits/stdc++.h>
using namespace std;
int main(){
	int n,k,a,b;
	cin>>n>>k>>a>>b;
	if(k<=a) cout<<k;
	else if(k<=a+b) cout<<a;
	else cout<<a-k+a+b;
	return 0;
}