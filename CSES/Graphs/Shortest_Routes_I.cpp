#include <bits/stdc++.h>
using namespace std;
void solve(){
  int n, m; cin >> n >> m;
  vector<vector<pair<int, long long>>> adj(n, vector<pair<int, long long>>());
  vector<long long> costs(n, LLONG_MAX);
  costs[0] = 0;
  for(int i = 0; i < m; i++){
    int start, end; long long cost; cin >> start >> end >> cost;
    start--; end--;
    adj[start].emplace_back(end, cost);
  }
  priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> heap;
  heap.emplace(0, 0);
  while(!heap.empty()){
    auto[curr_cost, curr] = heap.top();
    heap.pop();
    if(curr_cost > costs[curr]){
      continue;
    }
    for(auto [nei, nei_cost] : adj[curr]){
      long long new_cost = curr_cost + nei_cost;
      if(new_cost < costs[nei]){
        heap.emplace(new_cost, nei);
        costs[nei] = new_cost;
      }
    }
  }
  for(long long cost : costs){
    cout << cost << " ";
  }
}

int main(){
  solve();
  return 0;
}