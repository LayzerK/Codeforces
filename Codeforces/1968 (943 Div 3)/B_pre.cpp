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
  int n; int m; cin >> n; cin >> m;
  string a; cin >> a;
  string b; cin >> b;

  int left = 0;
  int right = 0;

  while(left < a.size() && right < b.size()){
    if(a[left] == b[right]){
      left += 1;
      right += 1;
    }
    else{
      right += 1;
    }
  }
  cout << left << "\n";
}

int main(){
  int tc;
  
  cin >> tc;

  while(tc--){
    solve();
  }
  return 0;
}