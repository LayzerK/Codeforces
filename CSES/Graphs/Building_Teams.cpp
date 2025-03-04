#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> adj;
vector<int> colors;
int n, m;

bool bipartite(int start){
  colors[start] = 1;
  deque<int> q;
  q.push_back(start);

  while(!q.empty()){
    int curr = q.front();
    q.pop_front();
    for(int nei : adj[curr]){
      if(colors[nei] == colors[curr]){
        return false;
      }
      else if(colors[nei] == -1){
        colors[nei] = 1 ^ colors[curr];
        q.push_back(nei);
      }
    }
  }

  return true;
}

void solve(){
  cin >> n >> m;
  adj.resize(n, vector<int>());
  colors.resize(n, -1);
  for(int i = 0; i < m; i++){
    int a,b;
    cin >> a >> b;
    a--; b--;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  for(int i = 0; i < n; i++){
    if(colors[i] == -1){
      if(!bipartite(i)){
        cout << "IMPOSSIBLE";
        return;
      }
    }
  }

  for(int i = 0; i < n; i++){
    cout << colors[i] + 1 << " ";
  }
}


int main(){
  solve();
  return 0;
}