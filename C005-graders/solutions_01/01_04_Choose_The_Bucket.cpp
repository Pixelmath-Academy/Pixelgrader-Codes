#include <iostream>
using namespace std;

int main(){
    int k,n;
    cin>>k >> n;
    if(k%n==0) cout<<n;
    else cout<< k%n;
    return 0;
}