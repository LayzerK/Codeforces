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
  int n; long long k; cin >> n; cin >> k;
  arr.assign(n, 0);
  for(int i = 0; i < n; i++){
    cin >> arr[i];
  }

  int left = 0;
  int right = n - 1;
  int ans = 0;
  while(left < right){
    if(arr[left] <= arr[right]){
      int cost = arr[left] * 2;
      if(k+1 < cost){
        break;
      }
      k -= cost;
      arr[right] -= arr[left];
      left += 1;
    }
    else{
      int cost = arr[right] * 2;
      if(k < cost){
        break;
      }
      k -= cost;
      arr[left] -= arr[right];
      right -= 1;
    }
    ans += 1;
  }
  if(left == right and arr[left] <= k){
    ans += 1;
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