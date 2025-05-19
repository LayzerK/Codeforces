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
vector<int> cost;

void solve(){
  int n; int m;
  cin >> n; cin >> m;
  cost.assign(n, 0);
  long long ends[m];
  long long mn_swap = INT32_MAX;
  long long swap_cost = 0;
  for(int i = 0; i < n; i++){
    cin >> cost[i];
    if(i < m){
      ends[i] = cost[i];
    }
  }
  for(int i = 0; i < n; i++){
    int pass;
    cin >> pass;
    cost[i] = min(cost[i], pass);
  }
  for(int i = m-1; i >= 0; i--){
    mn_swap = min(mn_swap, swap_cost + ends[i]);
    swap_cost += cost[i];
  }
  long long ans = mn_swap;
  for(int i = m; i < n; i++){
    ans += cost[i];
  }
  cout << ans << "\n";
}

int main(){
  int tc;
  
  cin >> tc;

  while(tc--){
    solve();
  }
  return 0;
}