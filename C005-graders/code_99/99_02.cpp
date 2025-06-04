#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct T {
    int w,v;
    double r;
};

bool cmp(const T &a, const T &b) {
    return a.r >b.r;
}

int main() {
    int n;
    double cap;
    cin >>n>>cap;

    T a[100005];

    for (int i = 0; i < n; ++i) cin >> a[i].w;
    for (int i = 0; i < n; ++i) cin >> a[i].v;
    for (int i = 0; i < n; ++i) a[i].r = 1.0 * a[i].v/a[i].w;

    sort(a,a+ n,cmp);

    double ans = 0;
    for (int i = 0; i < n && cap > 0; ++i) {
        if (cap >= a[i].w) {
            cap -= a[i].w;
            ans += a[i].v;
        } else {
            ans += cap * a[i].r;
            cap =0;
        }
    }

    printf("%.6f\n",ans);
    return 0;
}
