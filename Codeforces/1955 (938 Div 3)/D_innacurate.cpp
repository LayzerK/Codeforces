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
  int n; int m; int k;
  cin >> n; cin >> m; cin >> k;
  arr.assign(n, 0);
  map<int, int> goal;
  map<int, int> cnts;
  for(int i = 0; i < n; i++){
    cin >> arr[i];
  }
  for(int i = 0; i < m; i++){
    int num;
    cin >> num;
    goal[num] += 1;
  }
  int match = 0;
  int left = 0;
  int ans = 0;
  for(int right = 0; right < n; right++){
    int num = arr[right];
    if(right-left+1 > m){
      int rem = arr[left];
      if(cnts[rem] <= goal[rem]){
        match -= 1;
      }
      cnts[rem] -= 1;
      left += 1;
    }

    if(cnts[num] < goal[num]){
      match += 1;
    }
    cnts[num] += 1;

    if(right-left+1 == m and match >= k){
      ans += 1;
    }
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