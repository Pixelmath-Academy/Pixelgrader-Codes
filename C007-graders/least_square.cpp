#include<bits/stdc++.h>
using namespace std;
int main(){
	int m,n;
	cin>>m>>n;
	int cnt=0;
	while(m>0 and n>0){
		if(m>n){
			cnt+=(m/n);
			m%=n;
		}
		else{
			cnt+=(n/m);
			n%=m;
		}
	}
	cout<<cnt;
	return 0;
}
