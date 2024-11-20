#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
#include <array>
using namespace std;
void dfs(vector<vector<int>>& adj, vector<int>& size, int par, int curr){
  for(int child : adj[curr]){
    dfs(adj, size, curr, child);
    size[curr] += size[child] + 1;
  }
}
void solve(){
  int n;
  cin >> n;
  int par;
  vector<vector<int>> adj(n);
  for(int i = 1; i < n; i++){
    cin >> par;
    par--;
    adj[par].push_back(i);
  }
  vector<int> sizes(n, 0);
  dfs(adj, sizes, -1, 0);
  for(int sz : sizes){
    cout << sz << " ";
  }
}
int main(){
  solve();
  return 0;
}