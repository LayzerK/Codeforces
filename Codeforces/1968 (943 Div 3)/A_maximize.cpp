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
  int x;
  cin >> x;
  int val = 0;
  int y = 0;
  for(int i = 1; i < x; i++){
    if(gcd(x, i) + i > val){
      //cout << "here" << "\n";
      val = gcd(x,i) + i;
      y = i;
    }
  }
  cout << y << "\n";
  
}

int main(){
  int tc;
  
  cin >> tc;

  while(tc--){
    solve();
  }
  return 0;
}