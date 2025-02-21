#include<bits/stdc++.h>
using namespace std;
int main(){
	long long a[51];
	int n;
	cin>>n;
	a[0]=1,a[1]=2,a[2]=3,a[3]=4,a[4]=5,a[5]=28;
	for(int i=6;i<=n;i++){
		a[i]=2*a[i-1]-a[i-6];
	}
	cout<<a[n];
	return 0;
}
