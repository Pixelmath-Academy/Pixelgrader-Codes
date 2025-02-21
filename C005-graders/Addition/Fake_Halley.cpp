#include <bits/stdc++.h>
using namespace std;

void solve() {
    string s;
    cin>>s;
    int remainder=0,sz=s.size();
    for(int i=0;i<sz;i++){
    	remainder*=10;
    	remainder+=(s[i]-'0');
    	remainder%=75;
	}
	if(remainder==0) cout<<"YES\n";
	else cout<<"NO\n";
}

int main() {
    int t;
    cin>>t;
    while(t--){
    	solve();
	}
    return 0;
}