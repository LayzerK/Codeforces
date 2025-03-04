#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> adj;
vector<int> backtrack;
int n, m;
int bfs(int start){
  deque<pair<int, int>> q;
  q.push_back(make_pair(start, 1));
  vector<bool> visited(n, false);
  visited[start] = true;
  while(!q.empty()){
    pair<int, int> curr = q.front();
    q.pop_front();

    for(int nei : adj[curr.first]){
      if(visited[nei]){
        continue;
      }
      visited[nei] = true;
      backtrack[nei] = curr.first;
      if(nei == n-1){
        return curr.second + 1;
      }
      q.push_back(make_pair(nei, curr.second + 1));
    }
  }
  return -1;
}

void solve(){
  cin >> n >> m;
  adj.resize(n, vector<int>());
  backtrack.resize(n, -1);
  for(int i = 0; i < m; i++){
    int a,b; cin >> a >> b;
    a--;b--;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  int cost = bfs(0);
  if(cost != -1){
    cout << cost << endl;

    int curr = n-1;
    vector<int> ans;
    while(curr != -1){
      ans.push_back(curr);
      curr = backtrack[curr];
    }
    while(!ans.empty()){
      curr = ans.back();
      ans.pop_back();
      cout << curr + 1 << " ";
    }
  }
  else{
    cout << "IMPOSSIBLE" << endl;
  }



}

int main(){
  solve();
  return 0;
}