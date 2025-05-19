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
  int n; int m;
  cin >> n; cin >> m; arr.assign(n, 0);
  int rem = 1;
  for(int i = 0; i < n; i++){
    cin >> arr[i];
  }
  string ops;
  cin >> ops;
  int left = 0;
  int right = n-1;
  int ans [n];
  int val = 1;
  for(auto c : ops){
    if(c == 'L'){
      left += 1;
    }
    else{
      right -= 1;
    }
  }
  for(int i = n-1; i >= 0; i--){
    if(ops[i] == 'L'){
      left -= 1;
      val = (val * arr[left] % m);
    }
    else{
      right += 1;
      val = (val * arr[right] % m);
    }
    ans[i] = val;
  }
  for(auto v : ans){
    cout << v << " ";
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