#include <iostream>
using namespace std;

int main(){
    char s; int x;
    cin>>s>>x;
    char ans = 'A'+( s - 'A' + x )%26;
    cout<< ans;
    return 0;
}