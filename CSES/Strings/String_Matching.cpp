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
  string s;
  string pattern;
  cin >> s;
  cin >> pattern;
  int n = s.size();
  int m = pattern.size();

  if(m > n){
    cout << 0;
    return;
  }

  long long patHash = 0;
  const int base = 9973;
  const int mod = 1e9 + 7;

  vector<long long> pows(n);
  vector<long long> hashes(n+1);

  pows[0] = 1;
  for(int i = 1; i < n; i++){
    pows[i] = (pows[i-1] * base) % mod;
  }

  for(int i = 0; i < m; i++){
    patHash = (patHash +(pattern[i] - 'a' + 1) * pows[i]) % mod;
  }
  for(int i = 0; i < n; i++){
    hashes[i+1] = (hashes[i] + (s[i] - 'a' + 1) * pows[i]) % mod;
  }

  int ans = 0;

  for(int i = 0; i+m-1 < n; i++){
    long long subHash = (hashes[i+m] + mod - hashes[i]) % mod;
    //cout << subHash << "\n";
    //cout << (patHash * pows[i]) % mod << "\n";
    //cout << (subHash == (patHash * pows[i]) % mod);
    if(subHash == (patHash * pows[i]) % mod){
      ans += 1;
    }
  }
  cout << ans;



  
}

int main(){
  solve();
} 