#include <bits/stdc++.h>
using namespace std;
vector<int> sizes;
vector<long long> dp;
vector<vector<int>> adj;
int n;

long long dfs(int curr, int par){
  long long dist = 0;
  for(int child : adj[curr]){
    if(child == par){
      continue;
    }
    dist += dfs(child, curr) + sizes[child];
  }
  return dist;
}
void reroot(int curr, int par){
  long long curr_dist = dp[curr];
  for(int child : adj[curr]){
    if (child == par){
      continue;
    }
    long long closer = sizes[child];
    long long farther = n - closer;
    dp[child] = curr_dist - closer + farther;
    //cout << closer << " " << farther << " H E RE " << child << " " << curr << endl;
    reroot(child, curr);
  }
}

int subtree(int curr, int par){
  sizes[curr] = 1;
  for(int child : adj[curr]){
    if(child == par){
      continue;
    }
    sizes[curr] += subtree(child, curr);
  }
  return sizes[curr];
}

  void solve(){
    cin >> n;
    sizes.resize(n, 0);
    dp.resize(n, 0);
    adj.resize(n, vector<int>());
    for(int i = 0; i < n-1; i++){
      int a, b; cin >> a >> b;
      a--;b--;
      adj[a].push_back(b);
      adj[b].push_back(a);
    }
    subtree(0, -1);
    dp[0] = dfs(0, -1);
    reroot(0, -1);
    for(long long dist : dp){
      cout << dist << " ";
    }
  }


  int main(){
    solve();
    return 0;
  }