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
  int n;
  cin >> n;
  arr.assign(n, 0);
  for(int i = 0; i < n; i++){
    cin >> arr[i];
  }

  int left = 0;
  int ans = n;
  for(int right = 0; right < n; right++){
    if(arr[right] != arr[0]){
      ans = min(ans, right-left);
      left = right + 1;
    }
  }
  ans = min(ans, n-left);
  if(ans == n){
    cout << -1 << "\n";
  }
  else{
    cout << ans << "\n";
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