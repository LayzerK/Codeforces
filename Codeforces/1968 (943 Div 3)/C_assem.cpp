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
vector<int> arr;
void solve(){
  int n; cin >> n;
  arr.assign(n-1, 0);
  vector<int> ans;
  ans.assign(n, 0);
  for(int i = 0; i < n-1; i++){
    cin >> arr[i];
  }
  ans[0] = 500000;
  for(int i = 0; i < n-1; i++){
    ans[i+1] = ans[i] + arr[i];
  }
  for(int i = 0; i < n; i++){
    cout << ans[i] << " ";
  }
  cout << "\n";
}

int main(){
  int tc;
  
  cin >> tc;

  while(tc--){
    solve();
  }
  return 0;
}