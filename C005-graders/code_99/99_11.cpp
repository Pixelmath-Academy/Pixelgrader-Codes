#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;
using ll = long long;
const ll INF = 4e18;

struct Edge { int to; ll w; };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<vector<Edge>> g(N + 1);
    for (int i = 0; i < M; ++i) {
        int u, v;
        ll w;
        cin >> u >> v >> w;
        g[u].push_back({v, w});
    }

    vector<pair<ll, ll>> dist(N + 1, {INF, INF});
    typedef tuple<ll, int, int> State;
    priority_queue<State, vector<State>, greater<State>> pq;

    dist[1].first = 0;
    pq.push(make_tuple(0, 1, 0)); 

    while (!pq.empty()) {
        ll d;
        int u, used;
        tie(d, u, used) = pq.top(); pq.pop();

        ll& cur_dist = used ? dist[u].second : dist[u].first;
        if (d != cur_dist) continue;

        for (auto e : g[u]) {
            int v = e.to;
            ll w = e.w;
            ll& target_dist = used ? dist[v].second : dist[v].first;

            if (target_dist > d + w) {
                target_dist = d + w;
                pq.push(make_tuple(target_dist, v, used));
            }

            if (!used && dist[v].second > d) {
                dist[v].second = d;
                pq.push(make_tuple(d, v, 1));
            }
        }
    }

    ll res = min(dist[N].first, dist[N].second);
    cout << (res >= INF ? -1 : res) << '\n';
    return 0;
}
