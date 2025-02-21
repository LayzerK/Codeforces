#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> adj;
vector<int> colors;
vector<int> subtrees;

set<int> dfs(int curr, int par){
  set<int> large = {colors[curr]};

  for(int child : adj[curr]){
    if(child == par){
      continue;
    }

    set<int> small = dfs(child, curr);

    if(small.size() > large.size()){
      large.swap(small);
    }
    large.merge(small);
  }

  colors[curr] = large.size();
  return large;
}
void solve(){
  int n;
  cin >> n;

  colors.assign(n, 0);
  subtrees.assign(n, 0);
  adj.assign(n, vector<int>());

  for(int i = 0; i < n; i++){
    cin >> colors[i];
  }

  for(int i = 0; i < n - 1; i++){
    int a, b;
    cin >> a >> b;
    a--; b--;

    adj[a].push_back(b);
    adj[b].push_back(a);
  }
  dfs(0, -1);

  for(int i = 0; i < n; i++){
    cout << colors[i] << " ";
  }
}


int main(){
  solve();
  return 0;
}