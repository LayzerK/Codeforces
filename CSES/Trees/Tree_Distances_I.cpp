#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> adj;
int n;
vector<int> dist;


pair<int, int> far(int start){
  deque<pair<int, int>> q;
  q.push_back(make_pair(start, 0));
  int fd = -1;
  int f = -1;
  vector<int> visited(n, 0);
  visited[start] = 1;
  while(!q.empty()){
    pair<int, int> curr = q.front();
    q.pop_front();
    f = curr.first;
    fd = curr.second;

    for(int nei : adj[f]){
      if(visited[nei] == 0){
        visited[nei] = 1;
        q.push_back(make_pair(nei, fd+1));
      }
    }
  }

  return make_pair(f, fd);
}

void bfs(int start){
  deque<pair<int, int>> q;
  q.push_back(make_pair(start, 0));
  int fd = -1;
  int f = -1;
  vector<int> visited(n, 0);
  visited[start] = 1;
  while(!q.empty()){
    pair<int, int> curr = q.front();
    q.pop_front();
    f = curr.first;
    fd = curr.second;

    dist[f] = max(dist[f], fd);

    for(int nei : adj[f]){
      if(visited[nei] == 0){
        visited[nei] = 1;
        q.push_back(make_pair(nei, fd+1));
      }
    }
  }
}

void solve(){
  cin >> n;
  adj.resize(n, vector<int>());
  dist.resize(n, 0);
  for(int i = 0; i < n - 1; i++){
    int a, b;
    cin >> a >> b;
    a--; b--;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  pair<int, int> p1 = far(0);
  pair<int, int> p2 = far(p1.first);
  pair<int, int> p3 = far(p2.first);

  bfs(p2.first);
  bfs(p3.first);

  for(int d : dist){
    cout << d << " ";
  }
}

int main(){
  solve();
  return 0;
} 