#include <iostream>
using namespace std;

const int MAXN =100005;
long long f[MAXN];

int main() {
    int n, k;
    cin >> n >> k;

    long long sum = 0;
    for (int i = 1; i <= k; ++i) {
        cin >> f[i];
        sum+= f[i];
    }

    for (int i = k + 1; i <= n; ++i) {
        f[i] =sum;
        sum = sum+f[i]-f[i - k];
    }

    cout <<f[n] << '\n';
    return 0;
}