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
void solve(){
  int n; int m; int k;
  cin >> n; cin >> m; cin >> k;

  int big = ceil(float(n) / m);

  if(n - big > k){
    cout << "Yes" << "\n";
  }
  else{
    cout << "No" << "\n";
  }
}

int main(){
  int tc;
  
  cin >> tc;

  while(tc--){
    solve();
  }
  return 0;
}