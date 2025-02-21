#include <bits/stdc++.h>
using namespace std;

int main(){
    int a,b,c,d,k,i,j;
    cin>>a>>b>>c>>d;
    cin>>k;
    if(k=1){
        if(a>b){i=a;}
        else{i=b;}
        if(c>d){j=c;}
        else{j=d;}
    }
    else if(k=2){
        if(a>c){i=a;}
        else{i=c;}
        if(b>d){j=b;}
        else{j=d;}
    }
    if(i<j){cout<<i;}
    else {cout<<j;}

    return 0;
}