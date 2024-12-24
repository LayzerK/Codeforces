#include <bits/stdc++.h>
using namespace std;
vector<int> vals;
vector<vector<int>> adj;
vector<int> start_time;
vector<int> end_time;
int timer;
void euler(int curr){
  start_time[curr] = timer++;
  for(auto child : adj[curr]){
    euler(child);
  }
  end_time[curr] = timer;
}

void solve(){
  timer = 0;
  int n;
  cin >> n;
  vals.resize(n, 0);
  adj.resize(n);
  start_time.resize(n, 0);
  end_time.resize(n, 0);
  for(int child = 1; child < n; child++){
    int par; cin >> par;
    adj[--par].push_back(child);
  }
  for(int i = 0; i < n; i++){
    int pay; cin >> pay;
    vals[i] = pay;
  }
  int q;
  cin >> q;
  euler(0);


}

int main(){
  int tc;
  
  cin >> tc;

  while(tc--){
    solve();
  }
  return 0;
}