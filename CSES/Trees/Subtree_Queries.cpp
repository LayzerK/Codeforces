#include <bits/stdc++.h>
using namespace std;
int timer = 0;

struct Fenny{
  vector<long long> bit;
  vector<int> vals;
  int size;

  Fenny(int n){
    this->size=n+1;
    bit.assign(n+1, 0);
    vals.assign(n, 0);
  }

  Fenny(vector<int> const &arr) : Fenny(arr.size()){
    for (int i = 0; i < size; i++){
      bit[i] += arr[i];
      int r = i + (i & (-i));
      if(r < size){
        bit[r] += bit[i];
      }
    }
  }

  long long sum(int idx) {
      long long ret = 0;
      for (++idx; idx > 0; idx -= idx & -idx)
          ret += bit[idx];
      return ret;
  }

  long long sum(int l, int r){
    return sum(r) - sum(l-1);
  }

  void update(int idx, int delta) {
    vals[idx] += delta;
    for (++idx; idx < size; idx += idx & -idx)
        bit[idx] += delta;
  }

  void set(int idx, int new_val){
    update(idx, new_val - vals[idx]);
  }
};

void dfs(vector<vector<int>>& adj, vector<int>& vals, vector<int>& starts, vector<int>& ends, int curr, int par){
  starts[curr] = timer++;
  for(auto child : adj[curr]){
    if(child == par){
      continue;
      }
    dfs(adj, vals, starts, ends, child, curr);
  }
  ends[curr] = timer;
  }


void solve(){
  int n; int q; cin >> n; cin >> q;
  vector<int> vals(n, 0);
  vector<vector<int>> adj(n);
  vector<int> starts(n, 0);
  vector<int> ends(n,0);
  for(int i = 0; i < n; i++){
    cin >> vals[i];
  }
  int a; int b;
  for(int i = 0; i < n-1; i++){
    cin >> a; cin >> b;
    a--;
    b--;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }
  dfs(adj, vals, starts, ends, 0, -1);
  Fenny fen = Fenny(n);
  for(int i = 0; i < n; i++){
    fen.set(starts[i], vals[i]);
  }


  for(int i = 0; i < q; i++){
    int type;
    int node;
    cin >> type;
    cin >> node;
    node--;

    int l = starts[node];
    int r = ends[node];
    if(type == 1){
      int new_val;
      cin >> new_val;
      fen.set(l, new_val);
      //fen.update(r+1, -delta);
    }
    else{
      long long sum = fen.sum(l, r-1);
      //cout << "IN QUERY" << endl;
      cout << sum << endl;
    }

  }
}

int main(){
  solve();
  return 0;
}