#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
 
vector<vector<int>> adj;
vector<ll> cnt;

void dfs(int curr, int par){
  if (adj[curr].size() == 1 && adj[curr][0] == par){
    cnt[curr] = 1;
  }
  else{
    for (auto nei: adj[curr]){
      if(nei != par){
        dfs(nei, curr);
        cnt[curr] += cnt[nei];
      }
    }
  }
}


void solve(){
  int n, q;
  cin >> n;

  adj.assign(n,vector<int>());

  for (int i = 0; i < n-1; i++){
    int u, v;

    cin >> u >> v;
    u--;
    v--;

    adj[u].push_back(v);
    adj[v].push_back(u);

  }

  cnt.assign(n, 0);

  dfs(0, -1);

  cin >> q;
  for (int i = 0; i<q;i++){
    int a,b;

    cin >> a >> b;
    a--;
    b--;

    ll res = cnt[a] * cnt[b];

    cout << res << '\n';
  }
}

int main(){
  int tc;

  cin >> tc;

  while (tc--){
    solve();
  }
  return 0;
}