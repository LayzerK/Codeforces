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
  int mn = INT_MAX;
  map <int, int> freqs;
  for(auto & num : arr){
    freqs[num] += 1;
    mn = min(mn, num);
  }
  bool valid = false;

  for(auto & num : freqs){
    if(num.first % mn > 0){
      valid = true;
      break;
    }
  }
  if(freqs[1] > 1){
    cout << "NO" << "\n";
  }
  else if(freqs[mn] > 1){
    if(valid){
      cout << "YES" << "\n";
    }
    else{
      cout << "NO" << "\n";
    }
  }
  else{
    cout << "YES" << "\n";
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