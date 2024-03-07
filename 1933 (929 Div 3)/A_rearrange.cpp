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
  for(int i = 0; i < n;i++){
    cin >> arr[i];
}
  sort(arr.begin(), arr.end());
  int total = accumulate(arr.begin(), arr.end(), 0);
  for (auto & num : arr){
    if(num < 0){
      total -= num * 2;
    }
  }
  cout << total << "\n";
  
}

int main(){
  int tc;
  
  cin >> tc;

  while(tc--){
    solve();
  }
  return 0;
}