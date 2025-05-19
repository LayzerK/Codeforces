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
  int n;
  cin >> n;
  int sum = 0;
  int ones = 0;
  int twos = 0;
  for(int i = 0; i< n; i++){
    int num; cin >> num;
    if(num%3 == 1){
      ones += 1;
      sum = (sum+1)%3;
    }
    else if (num%3 == 2){
      twos += 1;
      sum = (sum + 2) % 3;
    }
  }

  if(sum == 0){
    cout << 0 << "\n";
  }
  else if(sum == 1){
    if(ones >= 1){
      cout << 1 << "\n";
    }
    else{
      cout << 2 << "\n";
    }
    }
  else{
    cout << 1 << "\n";
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