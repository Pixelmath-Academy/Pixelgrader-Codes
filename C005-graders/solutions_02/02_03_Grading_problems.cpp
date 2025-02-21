#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    if (n>=0 && n<=100){
    if (n>=80) cout<<"4";
    else if (n>=60) cout<<"3";
    else if (n>=40) cout<<"2";
    else if (n>=0) cout<<"1";
    }
else {cout<<"Invalid";}
    return 0;
}
