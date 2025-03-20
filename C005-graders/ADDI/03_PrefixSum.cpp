#include <iostream>
using namespace std;

int ps[100005];

int main(){
    int n, x, start, stop;
    cin >> n;
    for(int i=1; i<=n; i++){
        cin >> x;
        ps[i] = ps[i-1] + x;
    }
    cin >> start >> stop;
    cout << ps[stop] - ps[start-1];
    return 0;
}