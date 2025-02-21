#include <bits/stdc++.h>
using namespace std;
int main(){
    cin.tie(NULL)->sync_with_stdio(false);
    string a,b;
    cin>>a>>b;
    int x = a.length();
    int y = b.length();
    if (x>y){
        cout<<x;
    }
    else if(x<y){
        cout<<y;
    }
    else if(x=y){
        cout<<x;
    }
    return 0;
}
