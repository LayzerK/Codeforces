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
  int n; cin >> n;
  string prefs; cin >> prefs;
  int RH = 0;
  for(int i = 0; i < n; i++){
    if (prefs[i] == '1'){
      RH += 1;
    }
  }
  int LH = 0;
  int ans = n+1;
  if(RH >= ceil(float(n)/2)){
    ans = 0;
  }
  for(int i = 0; i < n; i++){
    int Lcap = (i+1) - ceil(float((i+1))/2);
    int Rreq = ceil(float((n-i-1))/2);

    if(prefs[i] == '1'){
      RH -= 1;
      LH += 1;
    }
    //cout << LH << "   " << RH << "   " << Lcap << "   " << Rreq << "\n";
    if (LH <= Lcap and RH >= Rreq and abs(float(n/2) - (i+1)) < abs(float(n)/2 - ans)){
      //cout << "here  " << i+1 << "\n";
      ans = i+1;
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