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
void dfs(vector<vector<int>>& adj, vector<int>& used, int curr, int par){
  //cout << curr << endl;
  for(int child : adj[curr]){
    if(child == par){
      continue;
    }
    dfs(adj, used, child, curr);
    //cout << " here  " << child << "   " << curr << endl;
    if(used[curr] == 0 && used[child] == 0){
      used[curr] = 1;
      used[child] = 1;
    }
  }
}
void solve(){
  int n;
  cin >> n;
  vector<vector<int>> adj(n);
  for(int i = 0; i < n - 1; i++){
    int a; int b;
    cin >> a; cin >> b;
    a--; b--;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }
  vector<int> used(n, 0);
  dfs(adj, used, 0, -1);
  cout << accumulate(used.begin(), used.end(), 0)/2;
}

int main(){
  solve();
  return 0;
}